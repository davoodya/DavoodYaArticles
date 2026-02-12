<?php
/**
 * ===========================
 * Admin Save Handler
 * ===========================
 * ذخیره تغییرات از پنل ادمین
 */

header('Content-Type: application/json; charset=utf-8');

// Configuration
define('COMMENTS_FILE', __DIR__ . '/../../data/user_comments.json');

// Get POST data
$input = file_get_contents('php://input');
$data = json_decode($input, true);

if ($data === null) {
    http_response_code(400);
    echo json_encode([
        'success' => false,
        'error' => 'داده‌های نامعتبر'
    ]);
    exit();
}

// Validate structure
if (!isset($data['comments']) || !is_array($data['comments'])) {
    http_response_code(400);
    echo json_encode([
        'success' => false,
        'error' => 'ساختار داده نامعتبر است'
    ]);
    exit();
}

// Save to file
$json = json_encode($data, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE);
$result = file_put_contents(COMMENTS_FILE, $json);

if ($result !== false) {
    echo json_encode([
        'success' => true,
        'message' => 'تغییرات با موفقیت ذخیره شد'
    ]);
} else {
    http_response_code(500);
    echo json_encode([
        'success' => false,
        'error' => 'خطا در ذخیره فایل'
    ]);
}
?>
