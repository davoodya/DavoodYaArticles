<?php
/**
 * Comments API
 */

// Clean output buffer
if (ob_get_level()) ob_end_clean();

// CORS Headers
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: GET, POST, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type');
header('Content-Type: application/json; charset=utf-8');

// Preflight
if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(200);
    exit;
}

// Config
define('COMMENTS_FILE', __DIR__ . '/../../data/user_comments.json');
define('ADMIN_EMAIL', 'davoodya40@gmail.com');

function loadComments() {
    if (!file_exists(COMMENTS_FILE)) {
        $data = ['comments' => []];
        file_put_contents(COMMENTS_FILE, json_encode($data, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE));
        return $data;
    }
    $content = file_get_contents(COMMENTS_FILE);
    $data = json_decode($content, true);
    return $data ?: ['comments' => []];
}

function saveComments($data) {
    $json = json_encode($data, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE);
    return file_put_contents(COMMENTS_FILE, $json) !== false;
}

function sanitize($input) {
    return htmlspecialchars(trim($input), ENT_QUOTES, 'UTF-8');
}

function validateEmail($email) {
    return filter_var($email, FILTER_VALIDATE_EMAIL) !== false;
}

function validateURL($url) {
    return empty($url) || filter_var($url, FILTER_VALIDATE_URL) !== false;
}

function generateID() {
    return uniqid('comment_', true) . '_' . time();
}

// GET - Retrieve comments
if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    if (!isset($_GET['article'])) {
        http_response_code(400);
        die(json_encode(['success' => false, 'error' => 'Missing article parameter']));
    }
    
    $articleSlug = sanitize($_GET['article']);
    $data = loadComments();
    
    $approved = array_filter($data['comments'], function($c) use ($articleSlug) {
        return isset($c['article_slug'], $c['confirmed']) && 
               $c['article_slug'] === $articleSlug && 
               $c['confirmed'] === true;
    });
    
    usort($approved, function($a, $b) {
        return strtotime($b['created_at']) - strtotime($a['created_at']);
    });
    
    $approved = array_map(function($c) {
        unset($c['email']);
        return $c;
    }, $approved);
    
    die(json_encode([
        'success' => true,
        'comments' => array_values($approved),
        'count' => count($approved)
    ]));
}

// POST - Submit comment
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $input = file_get_contents('php://input');
    $post = json_decode($input, true) ?: $_POST;
    
    $required = ['article_slug', 'name', 'email', 'comment'];
    foreach ($required as $field) {
        if (!isset($post[$field]) || empty(trim($post[$field]))) {
            http_response_code(400);
            die(json_encode(['success' => false, 'error' => "Missing $field"]));
        }
    }
    
    $articleSlug = sanitize($post['article_slug']);
    $name = sanitize($post['name']);
    $email = sanitize($post['email']);
    $website = sanitize($post['website'] ?? '');
    $commentText = sanitize($post['comment']);
    
    // Honeypot
    if (!empty($post['honeypot'])) {
        die(json_encode(['success' => true, 'message' => 'Thank you!']));
    }
    
    // Validate
    if (strlen($name) < 2 || strlen($name) > 100) {
        http_response_code(400);
        die(json_encode(['success' => false, 'error' => 'Invalid name length']));
    }
    
    if (!validateEmail($email)) {
        http_response_code(400);
        die(json_encode(['success' => false, 'error' => 'Invalid email']));
    }
    
    if (!validateURL($website)) {
        http_response_code(400);
        die(json_encode(['success' => false, 'error' => 'Invalid website URL']));
    }
    
    $length = mb_strlen($commentText, 'UTF-8');
    if ($length < 10 || $length > 2000) {
        http_response_code(400);
        die(json_encode(['success' => false, 'error' => 'Invalid comment length']));
    }
    
    $isAdmin = (strtolower($email) === strtolower(ADMIN_EMAIL));
    
    $comment = [
        'id' => generateID(),
        'article_slug' => $articleSlug,
        'name' => $name,
        'email' => $email,
        'website' => $website,
        'comment' => $commentText,
        'created_at' => date('Y-m-d H:i:s'),
        'confirmed' => $isAdmin,
        'ip_address' => $_SERVER['REMOTE_ADDR'] ?? 'unknown'
    ];
    
    $data = loadComments();
    $data['comments'][] = $comment;
    
    if (saveComments($data)) {
        $message = $isAdmin 
            ? 'دیدگاه شما با موفقیت ثبت و منتشر شد.' 
            : 'دیدگاه شما با موفقیت ثبت شد و پس از بررسی نمایش داده خواهد شد.';
        
        die(json_encode([
            'success' => true,
            'message' => $message,
            'is_admin' => $isAdmin
        ]));
    }
    
    http_response_code(500);
    die(json_encode(['success' => false, 'error' => 'Failed to save']));
}

http_response_code(405);
die(json_encode(['success' => false, 'error' => 'Method not allowed']));
