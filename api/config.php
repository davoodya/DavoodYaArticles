<?php
/**
 * Configuration for Comments System
 */

// Admin Settings
define('ADMIN_EMAIL', 'davoodya40@gmail.com');
define('ADMIN_PASSWORD', 'admin123'); // Change this to your secure password

// File Paths
define('COMMENTS_FILE', __DIR__ . '/../data/user_comments.json');

// Security Settings
define('MAX_COMMENT_LENGTH', 2000);
define('MIN_COMMENT_LENGTH', 10);
define('RATE_LIMIT_SECONDS', 60);
define('MAX_COMMENTS_PER_WINDOW', 3);
