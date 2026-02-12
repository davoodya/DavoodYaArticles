<?php
/**
 * ===========================
 * Comments API for Hugo Site
 * ===========================
 * 
 * این API برای دریافت و ذخیره کامنت‌های کاربران طراحی شده است.
 * کامنت‌ها در فایل JSON ذخیره می‌شوند.
 */

// CORS Headers
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: GET, POST, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type');
header('Content-Type: application/json; charset=utf-8');

// Handle preflight request
if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(200);
    exit();
}

// Configuration
define('COMMENTS_FILE', __DIR__ . '/../data/user_comments.json');
define('ADMIN_EMAIL', 'davoodya40@gmail.com');
define('MAX_COMMENT_LENGTH', 2000);
define('MIN_COMMENT_LENGTH', 10);

/**
 * بارگذاری کامنت‌ها از فایل JSON
 */
function loadComments() {
    if (!file_exists(COMMENTS_FILE)) {
        $initialData = ['comments' => []];
        file_put_contents(COMMENTS_FILE, json_encode($initialData, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE));
        return $initialData;
    }
    
    $content = file_get_contents(COMMENTS_FILE);
    $data = json_decode($content, true);
    
    if ($data === null) {
        return ['comments' => []];
    }
    
    return $data;
}

/**
 * ذخیره کامنت‌ها در فایل JSON
 */
function saveComments($data) {
    $json = json_encode($data, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE);
    return file_put_contents(COMMENTS_FILE, $json) !== false;
}

/**
 * Sanitize input
 */
function sanitizeInput($input) {
    $input = trim($input);
    $input = stripslashes($input);
    $input = htmlspecialchars($input, ENT_QUOTES, 'UTF-8');
    return $input;
}

/**
 * اعتبارسنجی ایمیل
 */
function validateEmail($email) {
    return filter_var($email, FILTER_VALIDATE_EMAIL) !== false;
}

/**
 * اعتبارسنجی URL
 */
function validateURL($url) {
    if (empty($url)) {
        return true; // اختیاری است
    }
    return filter_var($url, FILTER_VALIDATE_URL) !== false;
}

/**
 * تولید ID یکتا
 */
function generateID() {
    return uniqid('comment_', true) . '_' . time();
}

/**
 * دریافت کامنت‌های تایید شده برای یک مقاله خاص
 */
function getComments() {
    if (!isset($_GET['article'])) {
        http_response_code(400);
        echo json_encode([
            'success' => false,
            'error' => 'پارامتر article الزامی است'
        ]);
        exit();
    }
    
    $articleSlug = sanitizeInput($_GET['article']);
    $data = loadComments();
    
    // فیلتر کردن کامنت‌های تایید شده برای این مقاله
    $approvedComments = array_filter($data['comments'], function($comment) use ($articleSlug) {
        return isset($comment['article_slug']) && 
               $comment['article_slug'] === $articleSlug && 
               isset($comment['confirmed']) && 
               $comment['confirmed'] === true;
    });
    
    // مرتب‌سازی بر اساس تاریخ (جدیدترین اول)
    usort($approvedComments, function($a, $b) {
        return strtotime($b['created_at']) - strtotime($a['created_at']);
    });
    
    // حذف ایمیل از نتیجه (امنیت)
    $approvedComments = array_map(function($comment) {
        unset($comment['email']);
        return $comment;
    }, $approvedComments);
    
    echo json_encode([
        'success' => true,
        'comments' => array_values($approvedComments),
        'count' => count($approvedComments)
    ]);
}

/**
 * ثبت کامنت جدید
 */
function submitComment() {
    // دریافت داده‌های POST
    $input = file_get_contents('php://input');
    $postData = json_decode($input, true);
    
    if ($postData === null) {
        // Fallback به $_POST برای form submission معمولی
        $postData = $_POST;
    }
    
    // اعتبارسنجی فیلدهای الزامی
    $requiredFields = ['article_slug', 'name', 'email', 'comment'];
    foreach ($requiredFields as $field) {
        if (!isset($postData[$field]) || empty(trim($postData[$field]))) {
            http_response_code(400);
            echo json_encode([
                'success' => false,
                'error' => "فیلد {$field} الزامی است"
            ]);
            exit();
        }
    }
    
    // Sanitize inputs
    $articleSlug = sanitizeInput($postData['article_slug']);
    $name = sanitizeInput($postData['name']);
    $email = sanitizeInput($postData['email']);
    $website = isset($postData['website']) ? sanitizeInput($postData['website']) : '';
    $commentText = sanitizeInput($postData['comment']);
    
    // Honeypot check
    if (isset($postData['honeypot']) && !empty($postData['honeypot'])) {
        // Bot detected - return success but don't save
        echo json_encode([
            'success' => true,
            'message' => 'دیدگاه شما با موفقیت ثبت شد و پس از بررسی نمایش داده خواهد شد.'
        ]);
        exit();
    }
    
    // اعتبارسنجی name
    if (strlen($name) < 2 || strlen($name) > 100) {
        http_response_code(400);
        echo json_encode([
            'success' => false,
            'error' => 'نام باید بین 2 تا 100 کاراکتر باشد'
        ]);
        exit();
    }
    
    // اعتبارسنجی email
    if (!validateEmail($email)) {
        http_response_code(400);
        echo json_encode([
            'success' => false,
            'error' => 'ایمیل معتبر نیست'
        ]);
        exit();
    }
    
    // اعتبارسنجی website
    if (!validateURL($website)) {
        http_response_code(400);
        echo json_encode([
            'success' => false,
            'error' => 'آدرس وبسایت معتبر نیست'
        ]);
        exit();
    }
    
    // اعتبارسنجی comment
    $commentLength = mb_strlen($commentText, 'UTF-8');
    if ($commentLength < MIN_COMMENT_LENGTH) {
        http_response_code(400);
        echo json_encode([
            'success' => false,
            'error' => 'دیدگاه باید حداقل ' . MIN_COMMENT_LENGTH . ' کاراکتر باشد'
        ]);
        exit();
    }
    
    if ($commentLength > MAX_COMMENT_LENGTH) {
        http_response_code(400);
        echo json_encode([
            'success' => false,
            'error' => 'دیدگاه نباید بیشتر از ' . MAX_COMMENT_LENGTH . ' کاراکتر باشد'
        ]);
        exit();
    }
    
    // بررسی اینکه آیا ادمین است یا نه
    $isAdmin = (strtolower($email) === strtolower(ADMIN_EMAIL));
    
    // ساخت شیء کامنت
    $comment = [
        'id' => generateID(),
        'article_slug' => $articleSlug,
        'name' => $name,
        'email' => $email, // ذخیره می‌شود اما در API نمایش داده نمی‌شود
        'website' => $website,
        'comment' => $commentText,
        'created_at' => date('Y-m-d H:i:s'),
        'confirmed' => $isAdmin, // اگر ادمین باشد، مستقیم تایید می‌شود
        'ip_address' => $_SERVER['REMOTE_ADDR'] ?? 'unknown'
    ];
    
    // بارگذاری کامنت‌های موجود
    $data = loadComments();
    
    // اضافه کردن کامنت جدید
    $data['comments'][] = $comment;
    
    // ذخیره
    if (saveComments($data)) {
        $message = $isAdmin 
            ? 'دیدگاه شما با موفقیت ثبت و منتشر شد.' 
            : 'دیدگاه شما با موفقیت ثبت شد و پس از بررسی نمایش داده خواهد شد.';
        
        echo json_encode([
            'success' => true,
            'message' => $message,
            'is_admin' => $isAdmin
        ]);
    } else {
        http_response_code(500);
        echo json_encode([
            'success' => false,
            'error' => 'خطا در ذخیره‌سازی دیدگاه'
        ]);
    }
}

// Route handling
$method = $_SERVER['REQUEST_METHOD'];

try {
    if ($method === 'GET') {
        getComments();
    } elseif ($method === 'POST') {
        submitComment();
    } else {
        http_response_code(405);
        echo json_encode([
            'success' => false,
            'error' => 'متد ' . $method . ' پشتیبانی نمی‌شود'
        ]);
    }
} catch (Exception $e) {
    http_response_code(500);
    echo json_encode([
        'success' => false,
        'error' => 'خطای سرور: ' . $e->getMessage()
    ]);
}
?>
