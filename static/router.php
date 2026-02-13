<?php
/**
 * PHP Built-in Server Router Script
 * 
 * This script handles routing for PHP's built-in web server (php -S).
 * It serves static files and redirects 404 errors to the custom 404.html page.
 * 
 * Usage: php -S localhost:8080 -t public router.php
 * 
 * @package DavoodYa Hugo Site
 * @author Senior Backend Engineer
 * @date February 13, 2026
 */

// Get the requested URI
$requestUri = urldecode(parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH));

// Remove query string if present
$requestPath = strtok($requestUri, '?');

// Security: Prevent directory traversal attacks
if (strpos($requestPath, '..') !== false) {
    http_response_code(403);
    echo '403 Forbidden';
    exit;
}

// Get the document root (should be the public directory)
$documentRoot = $_SERVER['DOCUMENT_ROOT'];

// Build the full file path
$filePath = $documentRoot . $requestPath;

// ===========================
// Handle API requests (PHP files)
// ===========================
if (preg_match('/^\/api\//', $requestPath)) {
    $phpFile = $documentRoot . $requestPath;
    
    // If it's a PHP file in /api/ directory
    if (file_exists($phpFile) && pathinfo($phpFile, PATHINFO_EXTENSION) === 'php') {
        // Include and execute the PHP file
        chdir(dirname($phpFile));
        require $phpFile;
        exit;
    }
    
    // API endpoint not found
    http_response_code(404);
    header('Content-Type: application/json');
    echo json_encode([
        'error' => 'API endpoint not found',
        'path' => $requestPath
    ]);
    exit;
}

// ===========================
// Serve static files
// ===========================

// If requesting a directory, try index.html
if (is_dir($filePath)) {
    // Remove trailing slash if present
    $cleanPath = rtrim($requestPath, '/');
    
    // Try index.html in the directory
    $indexFile = $filePath . '/index.html';
    
    if (file_exists($indexFile)) {
        // Serve index.html with correct content type
        header('Content-Type: text/html; charset=UTF-8');
        readfile($indexFile);
        exit;
    }
    
    // If no index.html, treat as 404
    serve404();
}

// If file exists, serve it
if (file_exists($filePath) && is_file($filePath)) {
    // Get the file extension
    $extension = strtolower(pathinfo($filePath, PATHINFO_EXTENSION));
    
    // Set appropriate content type
    $mimeTypes = [
        'html' => 'text/html',
        'htm' => 'text/html',
        'css' => 'text/css',
        'js' => 'application/javascript',
        'json' => 'application/json',
        'xml' => 'application/xml',
        'jpg' => 'image/jpeg',
        'jpeg' => 'image/jpeg',
        'png' => 'image/png',
        'gif' => 'image/gif',
        'svg' => 'image/svg+xml',
        'webp' => 'image/webp',
        'ico' => 'image/x-icon',
        'woff' => 'font/woff',
        'woff2' => 'font/woff2',
        'ttf' => 'font/ttf',
        'eot' => 'application/vnd.ms-fontobject',
        'pdf' => 'application/pdf',
        'txt' => 'text/plain',
        'md' => 'text/markdown'
    ];
    
    if (isset($mimeTypes[$extension])) {
        header('Content-Type: ' . $mimeTypes[$extension]);
    }
    
    // Serve the file
    readfile($filePath);
    exit;
}

// ===========================
// Handle 404 - Serve custom 404.html
// ===========================

serve404();

/**
 * Serve the custom 404 page
 */
function serve404() {
    global $documentRoot;
    
    $custom404 = $documentRoot . '/404.html';
    
    // Set 404 status code
    http_response_code(404);
    
    // Serve custom 404 page if it exists
    if (file_exists($custom404)) {
        header('Content-Type: text/html; charset=UTF-8');
        readfile($custom404);
    } else {
        // Fallback to basic 404 message
        echo '<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>404 - صفحه یافت نشد</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 50px;
            background: #1a1a2e;
            color: #e4e4e4;
        }
        h1 { color: #00ff41; font-size: 3em; }
        p { font-size: 1.2em; margin: 20px 0; }
        a {
            color: #3aaddf;
            text-decoration: none;
            padding: 10px 20px;
            border: 2px solid #3aaddf;
            border-radius: 5px;
            display: inline-block;
            margin-top: 20px;
        }
        a:hover { background: #3aaddf; color: #000; }
    </style>
</head>
<body>
    <h1>404</h1>
    <p>صفحه مورد نظر یافت نشد</p>
    <a href="/">بازگشت به صفحه اصلی</a>
</body>
</html>';
    }
    
    exit;
}
