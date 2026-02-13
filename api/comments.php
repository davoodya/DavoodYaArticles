<?php
/**
 * Comments API
 */

while (ob_get_level()) {
    ob_end_clean();
}

ob_start();

header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: GET, POST, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type');
header('Content-Type: application/json; charset=utf-8');

if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(200);
    exit;
}

define('COMMENTS_FILE', __DIR__ . '/../data/user_comments.json');
define('ADMIN_EMAIL', 'davoodya40@gmail.com');

function respondJson($status, $payload) {
    http_response_code($status);
    echo json_encode($payload, JSON_UNESCAPED_UNICODE);
    exit;
}

function ensureCommentsFile(&$error) {
    $dir = dirname(COMMENTS_FILE);
    if (!is_dir($dir)) {
        if (!mkdir($dir, 0755, true)) {
            $error = 'Failed to create data directory';
            return false;
        }
    }

    if (!file_exists(COMMENTS_FILE)) {
        $empty = json_encode(['comments' => []], JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE);
        if (file_put_contents(COMMENTS_FILE, $empty) === false) {
            $error = 'Failed to initialize comments file';
            return false;
        }
    }

    return true;
}

function normalizeComment(&$comment) {
    if (isset($comment['confrim']) && !isset($comment['confirm'])) {
        $comment['confirm'] = (bool) $comment['confrim'];
        unset($comment['confrim']);
    }
    if (isset($comment['confirmed']) && !isset($comment['confirm'])) {
        $comment['confirm'] = (bool) $comment['confirmed'];
        unset($comment['confirmed']);
    }
    if (isset($comment['created_at']) && !isset($comment['datetime'])) {
        $comment['datetime'] = $comment['created_at'];
        unset($comment['created_at']);
    }
    if (!isset($comment['confirm'])) {
        $comment['confirm'] = false;
    }
}

function loadComments(&$error) {
    if (!ensureCommentsFile($error)) {
        return null;
    }

    $fp = fopen(COMMENTS_FILE, 'c+');
    if (!$fp) {
        $error = 'Failed to open comments file';
        return null;
    }

    if (!flock($fp, LOCK_SH)) {
        fclose($fp);
        $error = 'Failed to lock comments file';
        return null;
    }

    $contents = stream_get_contents($fp);
    flock($fp, LOCK_UN);
    fclose($fp);

    $contents = trim($contents);
    if (substr($contents, 0, 3) === "\xEF\xBB\xBF") {
        $contents = substr($contents, 3);
    }

    $data = json_decode($contents, true);
    if (!is_array($data) || !isset($data['comments']) || !is_array($data['comments'])) {
        $data = ['comments' => []];
    }

    foreach ($data['comments'] as &$comment) {
        if (is_array($comment)) {
            normalizeComment($comment);
        }
    }
    unset($comment);

    return $data;
}

function appendComment($comment, &$error) {
    if (!ensureCommentsFile($error)) {
        return false;
    }

    $fp = fopen(COMMENTS_FILE, 'c+');
    if (!$fp) {
        $error = 'Failed to open comments file';
        return false;
    }

    if (!flock($fp, LOCK_EX)) {
        fclose($fp);
        $error = 'Failed to lock comments file';
        return false;
    }

    $contents = stream_get_contents($fp);
    $contents = trim($contents);
    if (substr($contents, 0, 3) === "\xEF\xBB\xBF") {
        $contents = substr($contents, 3);
    }
    $data = json_decode($contents, true);
    if (!is_array($data) || !isset($data['comments']) || !is_array($data['comments'])) {
        $data = ['comments' => []];
    }

    foreach ($data['comments'] as &$existing) {
        if (is_array($existing)) {
            normalizeComment($existing);
        }
    }
    unset($existing);

    $data['comments'][] = $comment;

    $json = json_encode($data, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE);
    if ($json === false) {
        flock($fp, LOCK_UN);
        fclose($fp);
        $error = 'Failed to encode comments';
        return false;
    }

    rewind($fp);
    if (!ftruncate($fp, 0)) {
        flock($fp, LOCK_UN);
        fclose($fp);
        $error = 'Failed to truncate comments file';
        return false;
    }

    if (fwrite($fp, $json) === false) {
        flock($fp, LOCK_UN);
        fclose($fp);
        $error = 'Failed to write comments file';
        return false;
    }

    fflush($fp);
    flock($fp, LOCK_UN);
    fclose($fp);

    return true;
}

function cleanText($value, $maxLen) {
    $value = trim((string) $value);
    $value = strip_tags($value);
    if (function_exists('mb_substr')) {
        return mb_substr($value, 0, $maxLen, 'UTF-8');
    }
    return substr($value, 0, $maxLen);
}

function validateEmail($email) {
    return filter_var($email, FILTER_VALIDATE_EMAIL) !== false;
}

function validateURL($url) {
    if ($url === '') {
        return true;
    }
    return filter_var($url, FILTER_VALIDATE_URL) !== false;
}

function generateID() {
    return uniqid('comment_', true) . '_' . time();
}

if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    if (!isset($_GET['article'])) {
        respondJson(400, ['success' => false, 'error' => 'Missing article parameter']);
    }

    $articleSlug = cleanText($_GET['article'], 200);
    if ($articleSlug === '') {
        respondJson(400, ['success' => false, 'error' => 'Missing article parameter']);
    }

    $error = '';
    $data = loadComments($error);
    if ($data === null) {
        respondJson(500, ['success' => false, 'error' => $error]);
    }

    $approved = array_filter($data['comments'], function ($comment) use ($articleSlug) {
        return isset($comment['article_slug'], $comment['confirm']) &&
            $comment['article_slug'] === $articleSlug &&
            $comment['confirm'] === true;
    });

    usort($approved, function ($a, $b) {
        return strtotime($b['datetime']) - strtotime($a['datetime']);
    });

    $approved = array_map(function ($comment) {
        unset($comment['email']);
        return $comment;
    }, $approved);

    respondJson(200, [
        'success' => true,
        'comments' => array_values($approved),
        'count' => count($approved),
    ]);
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $raw = file_get_contents('php://input');
    $post = [];
    if ($raw !== '') {
        $post = json_decode($raw, true);
        if ($post === null && json_last_error() !== JSON_ERROR_NONE) {
            respondJson(400, ['success' => false, 'error' => 'Invalid JSON payload']);
        }
    }
    if (!is_array($post) || empty($post)) {
        $post = $_POST;
    }

    $required = ['article_slug', 'name', 'email', 'comment'];
    foreach ($required as $field) {
        if (!isset($post[$field]) || trim((string) $post[$field]) === '') {
            respondJson(400, ['success' => false, 'error' => "Missing {$field}"]);
        }
    }

    if (!empty($post['honeypot'])) {
        respondJson(200, ['success' => true, 'message' => 'Thank you!']);
    }

    $articleSlug = cleanText($post['article_slug'], 200);
    $articleTitle = cleanText($post['article_title'] ?? '', 200);
    $articleUrl = cleanText($post['article_url'] ?? '', 300);
    $name = cleanText($post['name'], 100);
    $email = trim((string) $post['email']);
    $website = trim((string) ($post['website'] ?? ''));
    $commentText = cleanText($post['comment'], 2000);

    if ($articleSlug === '') {
        respondJson(400, ['success' => false, 'error' => 'Missing article_slug']);
    }

    if ($name === '' || (function_exists('mb_strlen') ? mb_strlen($name, 'UTF-8') : strlen($name)) > 100) {
        respondJson(400, ['success' => false, 'error' => 'Invalid name']);
    }

    if (!validateEmail($email)) {
        respondJson(400, ['success' => false, 'error' => 'Invalid email']);
    }

    if (!validateURL($website)) {
        respondJson(400, ['success' => false, 'error' => 'Invalid website URL']);
    }
    if ($articleUrl !== '' && !filter_var($articleUrl, FILTER_VALIDATE_URL) && strpos($articleUrl, '/') !== 0) {
        respondJson(400, ['success' => false, 'error' => 'Invalid article URL']);
    }

    if ($commentText === '' || (function_exists('mb_strlen') ? mb_strlen($commentText, 'UTF-8') : strlen($commentText)) > 2000) {
        respondJson(400, ['success' => false, 'error' => 'Invalid comment']);
    }

    $isAdmin = ($email === ADMIN_EMAIL);

    $comment = [
        'id' => generateID(),
        'article_slug' => $articleSlug,
        'article_title' => $articleTitle,
        'article_url' => $articleUrl,
        'name' => $name,
        'email' => $email,
        'website' => $website,
        'comment' => $commentText,
        'datetime' => date('Y-m-d H:i:s'),
        'confirm' => $isAdmin,
        'ip_address' => $_SERVER['REMOTE_ADDR'] ?? 'unknown',
    ];

    $error = '';
    if (appendComment($comment, $error)) {
        $message = $isAdmin
            ? 'دیدگاه شما با موفقیت ثبت و منتشر شد.'
            : 'پیام شما پس از تایید مدیر در قسمت دیدگاه ها نمایش داده خواهد شد.';

        respondJson(200, [
            'success' => true,
            'message' => $message,
            'is_admin' => $isAdmin,
        ]);
    }

    respondJson(500, ['success' => false, 'error' => $error ?: 'Failed to save']);
}

respondJson(405, ['success' => false, 'error' => 'Method not allowed']);
