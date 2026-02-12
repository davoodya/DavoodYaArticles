<?php
/**
 * Admin Panel for Comments Management
 * با سیستم ورود ساده
 */

// Load configuration
require_once __DIR__ . '/config.php';

// Check if password submitted
$authenticated = false;
$error = '';

if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['password'])) {
    if ($_POST['password'] === ADMIN_PASSWORD) {
        session_start();
        $_SESSION['admin_authenticated'] = true;
        $authenticated = true;
    } else {
        $error = 'رمز عبور اشتباه است';
    }
} elseif (isset($_GET['logout'])) {
    session_start();
    session_destroy();
    header('Location: admin.php');
    exit;
} else {
    session_start();
    $authenticated = isset($_SESSION['admin_authenticated']) && $_SESSION['admin_authenticated'] === true;
}

// Show login form if not authenticated
if (!$authenticated) {
?>
<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ورود به پنل مدیریت</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Tahoma', 'Arial', sans-serif;
            background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 100%);
            color: #e0e0e0;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }

        .login-container {
            background: #0f0f0f;
            border: 1px solid rgba(0, 255, 65, 0.3);
            border-radius: 12px;
            padding: 40px;
            max-width: 400px;
            width: 100%;
            box-shadow: 0 10px 40px rgba(0, 255, 65, 0.1);
        }

        .login-title {
            color: #00ff41;
            text-align: center;
            margin-bottom: 30px;
            font-size: 1.8rem;
            text-shadow: 0 0 10px rgba(0, 255, 65, 0.5);
        }

        .login-subtitle {
            text-align: center;
            color: #808080;
            margin-bottom: 30px;
        }

        .form-group {
            margin-bottom: 20px;
        }

        .form-label {
            display: block;
            color: #b0b0b0;
            margin-bottom: 8px;
        }

        .form-input {
            width: 100%;
            padding: 12px;
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 5px;
            color: #e0e0e0;
            font-size: 1rem;
            transition: all 0.3s;
        }

        .form-input:focus {
            outline: none;
            border-color: #00ff41;
            box-shadow: 0 0 10px rgba(0, 255, 65, 0.2);
        }

        .btn-submit {
            width: 100%;
            padding: 12px;
            background: rgba(0, 255, 65, 0.1);
            border: 1px solid #00ff41;
            color: #00ff41;
            border-radius: 5px;
            cursor: pointer;
            font-size: 1rem;
            transition: all 0.3s;
            font-weight: bold;
        }

        .btn-submit:hover {
            background: rgba(0, 255, 65, 0.2);
            box-shadow: 0 0 10px rgba(0, 255, 65, 0.3);
            transform: translateY(-2px);
        }

        .error-message {
            background: rgba(255, 0, 0, 0.1);
            border: 1px solid #ff0000;
            color: #ff0000;
            padding: 12px;
            border-radius: 5px;
            margin-bottom: 20px;
            text-align: center;
        }

        .info-box {
            background: rgba(58, 173, 223, 0.1);
            border: 1px solid #3aaddf;
            color: #3aaddf;
            padding: 15px;
            border-radius: 5px;
            margin-top: 20px;
            font-size: 0.9rem;
        }

        .info-box strong {
            display: block;
            margin-bottom: 8px;
        }
    </style>
</head>
<body>
    <div class="login-container">
        <h1 class="login-title">🛡️ پنل مدیریت کامنت‌ها</h1>
        <p class="login-subtitle">لطفاً رمز عبور را وارد کنید</p>
        
        <?php if ($error): ?>
            <div class="error-message">
                ⚠️ <?php echo htmlspecialchars($error); ?>
            </div>
        <?php endif; ?>
        
        <form method="POST" action="">
            <div class="form-group">
                <label class="form-label" for="password">رمز عبور:</label>
                <input 
                    type="password" 
                    id="password" 
                    name="password" 
                    class="form-input" 
                    placeholder="رمز عبور را وارد کنید"
                    required
                    autofocus
                />
            </div>
            
            <button type="submit" class="btn-submit">ورود به پنل</button>
        </form>

        <div class="info-box">
            <strong>📝 راهنما:</strong>
            رمز عبور پیش‌فرض: <code>admin123</code><br>
            برای تغییر رمز، فایل <code>api/config.php</code> را ویرایش کنید.
        </div>
    </div>
</body>
</html>
<?php
    exit;
}

// If authenticated, show admin panel
?>
<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>پنل مدیریت کامنت‌ها</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Tahoma', 'Arial', sans-serif;
            background: #0a0a0a;
            color: #e0e0e0;
            padding: 20px;
            line-height: 1.6;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
        }

        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 30px;
            flex-wrap: wrap;
            gap: 15px;
        }

        h1 {
            color: #00ff41;
            text-shadow: 0 0 10px rgba(0, 255, 65, 0.5);
        }

        .logout-btn {
            padding: 10px 20px;
            background: rgba(255, 0, 0, 0.1);
            border: 1px solid #ff0000;
            color: #ff0000;
            border-radius: 5px;
            cursor: pointer;
            text-decoration: none;
            transition: all 0.3s;
            display: inline-block;
        }

        .logout-btn:hover {
            background: rgba(255, 0, 0, 0.2);
            box-shadow: 0 0 10px rgba(255, 0, 0, 0.3);
        }

        .stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }

        .stat-card {
            background: #0f0f0f;
            border: 1px solid rgba(0, 255, 65, 0.3);
            border-radius: 8px;
            padding: 20px;
            text-align: center;
        }

        .stat-number {
            font-size: 2.5rem;
            color: #00ff41;
            font-weight: bold;
        }

        .stat-label {
            color: #b0b0b0;
            margin-top: 10px;
        }

        .tabs {
            display: flex;
            gap: 10px;
            margin-bottom: 20px;
            border-bottom: 2px solid rgba(0, 255, 65, 0.3);
        }

        .tab {
            padding: 10px 20px;
            background: transparent;
            border: none;
            color: #b0b0b0;
            cursor: pointer;
            font-size: 1rem;
            transition: all 0.3s;
        }

        .tab.active {
            color: #00ff41;
            border-bottom: 2px solid #00ff41;
        }

        .comment-card {
            background: #0f0f0f;
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 20px;
            transition: all 0.3s;
        }

        .comment-card:hover {
            border-color: rgba(0, 255, 65, 0.5);
            box-shadow: 0 0 20px rgba(0, 255, 65, 0.1);
        }

        .comment-header {
            display: flex;
            justify-content: space-between;
            align-items: start;
            margin-bottom: 15px;
            flex-wrap: wrap;
            gap: 10px;
        }

        .comment-info {
            flex: 1;
        }

        .comment-author {
            font-size: 1.2rem;
            color: #00ff41;
            font-weight: bold;
        }

        .comment-meta {
            color: #808080;
            font-size: 0.9rem;
            margin-top: 5px;
        }

        .comment-article {
            color: #3aaddf;
            font-size: 0.9rem;
            margin-top: 5px;
        }

        .comment-body {
            background: rgba(255, 255, 255, 0.03);
            padding: 15px;
            border-radius: 5px;
            margin: 15px 0;
            white-space: pre-wrap;
            word-wrap: break-word;
        }

        .comment-actions {
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }

        .btn {
            padding: 8px 16px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 0.9rem;
            transition: all 0.3s;
        }

        .btn-approve {
            background: rgba(0, 255, 65, 0.1);
            border: 1px solid #00ff41;
            color: #00ff41;
        }

        .btn-approve:hover {
            background: rgba(0, 255, 65, 0.2);
            box-shadow: 0 0 10px rgba(0, 255, 65, 0.3);
        }

        .btn-reject {
            background: rgba(224, 108, 17, 0.1);
            border: 1px solid #e06c11;
            color: #e06c11;
        }

        .btn-reject:hover {
            background: rgba(224, 108, 17, 0.2);
            box-shadow: 0 0 10px rgba(224, 108, 17, 0.3);
        }

        .btn-delete {
            background: rgba(255, 0, 0, 0.1);
            border: 1px solid #ff0000;
            color: #ff0000;
        }

        .btn-delete:hover {
            background: rgba(255, 0, 0, 0.2);
            box-shadow: 0 0 10px rgba(255, 0, 0, 0.3);
        }

        .status-badge {
            padding: 5px 10px;
            border-radius: 5px;
            font-size: 0.85rem;
            font-weight: bold;
        }

        .status-pending {
            background: rgba(224, 108, 17, 0.2);
            color: #e06c11;
        }

        .status-approved {
            background: rgba(0, 255, 65, 0.2);
            color: #00ff41;
        }

        .empty-state {
            text-align: center;
            padding: 60px 20px;
            color: #808080;
        }

        .loading {
            text-align: center;
            padding: 40px;
            color: #00ff41;
        }

        @keyframes spin {
            to { transform: rotate(360deg); }
        }

        .spinner {
            display: inline-block;
            width: 40px;
            height: 40px;
            border: 3px solid rgba(0, 255, 65, 0.3);
            border-top-color: #00ff41;
            border-radius: 50%;
            animation: spin 1s linear infinite;
        }

        @media (max-width: 768px) {
            .comment-header {
                flex-direction: column;
            }

            .comment-actions {
                width: 100%;
            }

            .btn {
                flex: 1;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🛡️ پنل مدیریت کامنت‌ها</h1>
            <a href="?logout" class="logout-btn">خروج از پنل</a>
        </div>

        <div class="stats" id="stats">
            <div class="stat-card">
                <div class="stat-number" id="totalComments">0</div>
                <div class="stat-label">کل کامنت‌ها</div>
            </div>
            <div class="stat-card">
                <div class="stat-number" id="pendingComments">0</div>
                <div class="stat-label">در انتظار تایید</div>
            </div>
            <div class="stat-card">
                <div class="stat-number" id="approvedComments">0</div>
                <div class="stat-label">تایید شده</div>
            </div>
        </div>

        <div class="tabs">
            <button class="tab active" data-tab="pending">در انتظار تایید</button>
            <button class="tab" data-tab="approved">تایید شده</button>
            <button class="tab" data-tab="all">همه</button>
        </div>

        <div id="commentsContainer">
            <div class="loading">
                <div class="spinner"></div>
                <p>در حال بارگذاری...</p>
            </div>
        </div>
    </div>

    <script>
        let allComments = [];
        let currentTab = 'pending';

        // Load comments
        async function loadComments() {
            try {
                const response = await fetch('../data/user_comments.json?' + Date.now());
                const data = await response.json();
                allComments = data.comments || [];
                updateStats();
                renderComments();
            } catch (error) {
                console.error('Error loading comments:', error);
                document.getElementById('commentsContainer').innerHTML = 
                    '<div class="empty-state">خطا در بارگذاری کامنت‌ها</div>';
            }
        }

        // Update statistics
        function updateStats() {
            const total = allComments.length;
            const pending = allComments.filter(c => !c.confirmed).length;
            const approved = allComments.filter(c => c.confirmed).length;

            document.getElementById('totalComments').textContent = total;
            document.getElementById('pendingComments').textContent = pending;
            document.getElementById('approvedComments').textContent = approved;
        }

        // Render comments
        function renderComments() {
            let filtered = [];
            
            if (currentTab === 'pending') {
                filtered = allComments.filter(c => !c.confirmed);
            } else if (currentTab === 'approved') {
                filtered = allComments.filter(c => c.confirmed);
            } else {
                filtered = allComments;
            }

            const container = document.getElementById('commentsContainer');

            if (filtered.length === 0) {
                container.innerHTML = '<div class="empty-state">کامنتی یافت نشد</div>';
                return;
            }

            // Sort by date (newest first)
            filtered.sort((a, b) => new Date(b.created_at) - new Date(a.created_at));

            container.innerHTML = filtered.map(comment => `
                <div class="comment-card">
                    <div class="comment-header">
                        <div class="comment-info">
                            <div class="comment-author">${escapeHtml(comment.name)}</div>
                            <div class="comment-meta">
                                📧 ${escapeHtml(comment.email)} | 
                                🕒 ${new Date(comment.created_at).toLocaleString('fa-IR')} |
                                🌐 IP: ${comment.ip_address || 'N/A'}
                            </div>
                            <div class="comment-article">
                                📄 مقاله: ${comment.article_slug}
                            </div>
                            ${comment.website ? `<div class="comment-meta">🔗 ${escapeHtml(comment.website)}</div>` : ''}
                        </div>
                        <span class="status-badge ${comment.confirmed ? 'status-approved' : 'status-pending'}">
                            ${comment.confirmed ? '✓ تایید شده' : '⏳ در انتظار'}
                        </span>
                    </div>
                    <div class="comment-body">${escapeHtml(comment.comment)}</div>
                    <div class="comment-actions">
                        ${!comment.confirmed ? 
                            `<button class="btn btn-approve" onclick="approveComment('${comment.id}')">
                                ✓ تایید
                            </button>
                            <button class="btn btn-reject" onclick="rejectComment('${comment.id}')">
                                ✗ رد
                            </button>` : 
                            `<button class="btn btn-reject" onclick="unapproveComment('${comment.id}')">
                                ◄ برگشت به در انتظار
                            </button>`
                        }
                        <button class="btn btn-delete" onclick="deleteComment('${comment.id}')">
                            🗑️ حذف
                        </button>
                    </div>
                </div>
            `).join('');
        }

        // Approve comment
        async function approveComment(id) {
            if (!confirm('آیا از تایید این کامنت مطمئن هستید؟')) return;

            const comment = allComments.find(c => c.id === id);
            if (comment) {
                comment.confirmed = true;
                await saveComments();
            }
        }

        // Unapprove comment
        async function unapproveComment(id) {
            if (!confirm('آیا می‌خواهید این کامنت را به حالت در انتظار برگردانید؟')) return;

            const comment = allComments.find(c => c.id === id);
            if (comment) {
                comment.confirmed = false;
                await saveComments();
            }
        }

        // Reject comment (same as unapprove)
        async function rejectComment(id) {
            await unapproveComment(id);
        }

        // Delete comment
        async function deleteComment(id) {
            if (!confirm('آیا از حذف این کامنت مطمئن هستید؟ این عمل قابل بازگشت نیست!')) return;

            allComments = allComments.filter(c => c.id !== id);
            await saveComments();
        }

        // Save comments
        async function saveComments() {
            try {
                const response = await fetch('admin_save.php', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ comments: allComments })
                });

                const result = await response.json();

                if (result.success) {
                    updateStats();
                    renderComments();
                    alert('✓ تغییرات با موفقیت ذخیره شد');
                } else {
                    alert('✗ خطا در ذخیره: ' + result.error);
                }
            } catch (error) {
                console.error('Error saving comments:', error);
                alert('✗ خطا در ذخیره کامنت‌ها');
            }
        }

        // Escape HTML
        function escapeHtml(text) {
            const div = document.createElement('div');
            div.textContent = text;
            return div.innerHTML;
        }

        // Tab switching
        document.querySelectorAll('.tab').forEach(tab => {
            tab.addEventListener('click', () => {
                document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
                tab.classList.add('active');
                currentTab = tab.dataset.tab;
                renderComments();
            });
        });

        // Auto-refresh every 30 seconds
        setInterval(loadComments, 30000);

        // Initial load
        loadComments();
    </script>
</body>
</html>
