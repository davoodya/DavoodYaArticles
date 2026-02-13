<?php
/**
 * ===========================
 * Admin Save Handler
 * ===========================
 * ذخیره تغییرات از پنل ادمین
 */

header('Content-Type: application/json; charset=utf-8');

define('COMMENTS_FILE', __DIR__ . '/../../data/user_comments.json');

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
    if (isset($comment['confirm'])) {
        $comment['confirm'] = (bool) $comment['confirm'];
    } else {
        $comment['confirm'] = false;
    }
}

$input = file_get_contents('php://input');
$data = json_decode($input, true);

if ($data === null && json_last_error() !== JSON_ERROR_NONE) {
    respondJson(400, ['success' => false, 'error' => 'داده‌های نامعتبر']);
}

if (!isset($data['comments']) || !is_array($data['comments'])) {
    respondJson(400, ['success' => false, 'error' => 'ساختار داده نامعتبر است']);
}

foreach ($data['comments'] as &$comment) {
    if (is_array($comment)) {
        normalizeComment($comment);
    }
}
unset($comment);

$error = '';
if (!ensureCommentsFile($error)) {
    respondJson(500, ['success' => false, 'error' => $error]);
}

$fp = fopen(COMMENTS_FILE, 'c+');
if (!$fp) {
    respondJson(500, ['success' => false, 'error' => 'خطا در باز کردن فایل']);
}

if (!flock($fp, LOCK_EX)) {
    fclose($fp);
    respondJson(500, ['success' => false, 'error' => 'خطا در قفل فایل']);
}

$json = json_encode(['comments' => $data['comments']], JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE);
if ($json === false) {
    flock($fp, LOCK_UN);
    fclose($fp);
    respondJson(500, ['success' => false, 'error' => 'خطا در تبدیل داده']);
}

rewind($fp);
if (!ftruncate($fp, 0)) {
    flock($fp, LOCK_UN);
    fclose($fp);
    respondJson(500, ['success' => false, 'error' => 'خطا در پاکسازی فایل']);
}

if (fwrite($fp, $json) === false) {
    flock($fp, LOCK_UN);
    fclose($fp);
    respondJson(500, ['success' => false, 'error' => 'خطا در ذخیره فایل']);
}

fflush($fp);
flock($fp, LOCK_UN);
fclose($fp);

respondJson(200, [
    'success' => true,
    'message' => 'تغییرات با موفقیت ذخیره شد',
]);
