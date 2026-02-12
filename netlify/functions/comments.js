/**
 * ===========================
 * Netlify Serverless Function: Comments API
 * ===========================
 * Handles comment submission and retrieval
 * Uses Netlify Blobs for storage
 */

const { getStore } = require('@netlify/blobs');

// ===========================
// Configuration
// ===========================

const CONFIG = {
    STORE_NAME: 'comments',
    MAX_COMMENT_LENGTH: 2000,
    MIN_COMMENT_LENGTH: 10,
    RATE_LIMIT_WINDOW: 60000, // 1 minute
    MAX_REQUESTS_PER_WINDOW: 10,
};

// ===========================
// Rate Limiting (In-Memory)
// ===========================

const rateLimitMap = new Map();

function checkRateLimit(identifier) {
    const now = Date.now();
    const record = rateLimitMap.get(identifier);
    
    if (!record) {
        rateLimitMap.set(identifier, { count: 1, resetAt: now + CONFIG.RATE_LIMIT_WINDOW });
        return { allowed: true };
    }
    
    if (now > record.resetAt) {
        rateLimitMap.set(identifier, { count: 1, resetAt: now + CONFIG.RATE_LIMIT_WINDOW });
        return { allowed: true };
    }
    
    if (record.count >= CONFIG.MAX_REQUESTS_PER_WINDOW) {
        return { 
            allowed: false, 
            retryAfter: Math.ceil((record.resetAt - now) / 1000) 
        };
    }
    
    record.count++;
    return { allowed: true };
}

// Clean up old entries periodically
setInterval(() => {
    const now = Date.now();
    for (const [key, record] of rateLimitMap.entries()) {
        if (now > record.resetAt) {
            rateLimitMap.delete(key);
        }
    }
}, CONFIG.RATE_LIMIT_WINDOW);

// ===========================
// Utility Functions
// ===========================

function sanitizeInput(str) {
    if (!str) return '';
    return str.trim().replace(/[<>]/g, '');
}

function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

function validateURL(url) {
    if (!url) return true; // Optional field
    try {
        const urlObj = new URL(url);
        return urlObj.protocol === 'http:' || urlObj.protocol === 'https:';
    } catch {
        return false;
    }
}

function generateId() {
    return `${Date.now()}-${Math.random().toString(36).substr(2, 9)}`;
}

function corsHeaders(origin) {
    const allowedOrigins = [
        process.env.URL,
        process.env.DEPLOY_PRIME_URL,
        'http://localhost:1313',
        'http://localhost:8888',
    ].filter(Boolean);
    
    const allowOrigin = allowedOrigins.includes(origin) ? origin : allowedOrigins[0];
    
    return {
        'Access-Control-Allow-Origin': allowOrigin || '*',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
        'Access-Control-Max-Age': '86400',
    };
}

// ===========================
// Comment Storage Functions
// ===========================

async function getComments(store, articleSlug) {
    try {
        const data = await store.get(articleSlug, { type: 'json' });
        return data || { comments: [] };
    } catch (error) {
        console.error('Error reading comments:', error);
        return { comments: [] };
    }
}

async function saveComments(store, articleSlug, data) {
    try {
        await store.setJSON(articleSlug, data);
        return true;
    } catch (error) {
        console.error('Error saving comments:', error);
        return false;
    }
}

// ===========================
// GET Handler - Retrieve Comments
// ===========================

async function handleGet(event, store) {
    const articleSlug = event.queryStringParameters?.article;
    
    if (!articleSlug) {
        return {
            statusCode: 400,
            body: JSON.stringify({ error: 'Article slug is required' }),
        };
    }
    
    const data = await getComments(store, articleSlug);
    
    // Filter only approved comments
    const approvedComments = (data.comments || [])
        .filter(c => c.status === 'approved')
        .sort((a, b) => new Date(b.created_at) - new Date(a.created_at));
    
    return {
        statusCode: 200,
        body: JSON.stringify({ 
            comments: approvedComments,
            count: approvedComments.length 
        }),
    };
}

// ===========================
// POST Handler - Submit Comment
// ===========================

async function handlePost(event, store) {
    let body;
    try {
        body = JSON.parse(event.body);
    } catch {
        return {
            statusCode: 400,
            body: JSON.stringify({ error: 'Invalid JSON' }),
        };
    }
    
    // Validate required fields
    const { article_slug, name, email, comment_text, website } = body;
    
    if (!article_slug || !name || !email || !comment_text) {
        return {
            statusCode: 400,
            body: JSON.stringify({ error: 'Missing required fields' }),
        };
    }
    
    // Sanitize inputs
    const sanitizedData = {
        article_slug: sanitizeInput(article_slug),
        name: sanitizeInput(name),
        email: sanitizeInput(email).toLowerCase(),
        website: sanitizeInput(website),
        comment_text: sanitizeInput(comment_text),
    };
    
    // Validate name
    if (sanitizedData.name.length < 2 || sanitizedData.name.length > 100) {
        return {
            statusCode: 400,
            body: JSON.stringify({ error: 'Name must be between 2 and 100 characters' }),
        };
    }
    
    // Validate email
    if (!validateEmail(sanitizedData.email)) {
        return {
            statusCode: 400,
            body: JSON.stringify({ error: 'Invalid email address' }),
        };
    }
    
    // Validate website (optional)
    if (sanitizedData.website && !validateURL(sanitizedData.website)) {
        return {
            statusCode: 400,
            body: JSON.stringify({ error: 'Invalid website URL' }),
        };
    }
    
    // Validate comment length
    if (sanitizedData.comment_text.length < CONFIG.MIN_COMMENT_LENGTH) {
        return {
            statusCode: 400,
            body: JSON.stringify({ error: `Comment must be at least ${CONFIG.MIN_COMMENT_LENGTH} characters` }),
        };
    }
    
    if (sanitizedData.comment_text.length > CONFIG.MAX_COMMENT_LENGTH) {
        return {
            statusCode: 400,
            body: JSON.stringify({ error: `Comment must be less than ${CONFIG.MAX_COMMENT_LENGTH} characters` }),
        };
    }
    
    // Create comment object
    const comment = {
        id: generateId(),
        article_slug: sanitizedData.article_slug,
        name: sanitizedData.name,
        email: sanitizedData.email, // Not exposed in API
        website: sanitizedData.website || null,
        comment_text: sanitizedData.comment_text,
        created_at: new Date().toISOString(),
        status: 'approved', // Change to 'pending' if you want manual approval
        parent_id: null, // For future nested comments support
    };
    
    // Get existing comments
    const data = await getComments(store, sanitizedData.article_slug);
    
    // Add new comment
    data.comments = data.comments || [];
    data.comments.push(comment);
    
    // Save
    const saved = await saveComments(store, sanitizedData.article_slug, data);
    
    if (!saved) {
        return {
            statusCode: 500,
            body: JSON.stringify({ error: 'Failed to save comment' }),
        };
    }
    
    // Return success (without email)
    const { email: _email, ...commentWithoutEmail } = comment;
    
    return {
        statusCode: 201,
        body: JSON.stringify({
            message: 'Comment submitted successfully',
            comment: commentWithoutEmail,
        }),
    };
}

// ===========================
// Main Handler
// ===========================

exports.handler = async (event, context) => {
    const origin = event.headers.origin || event.headers.Origin;
    const headers = {
        'Content-Type': 'application/json',
        ...corsHeaders(origin),
    };
    
    // Handle CORS preflight
    if (event.httpMethod === 'OPTIONS') {
        return {
            statusCode: 204,
            headers,
            body: '',
        };
    }
    
    // Rate limiting
    const identifier = event.headers['x-forwarded-for'] || event.headers['client-ip'] || 'unknown';
    const rateLimitCheck = checkRateLimit(identifier);
    
    if (!rateLimitCheck.allowed) {
        return {
            statusCode: 429,
            headers: {
                ...headers,
                'Retry-After': rateLimitCheck.retryAfter.toString(),
            },
            body: JSON.stringify({ 
                error: 'Too many requests', 
                retryAfter: rateLimitCheck.retryAfter 
            }),
        };
    }
    
    // Initialize Netlify Blobs store
    let store;
    try {
        store = getStore(CONFIG.STORE_NAME);
    } catch (error) {
        console.error('Failed to initialize store:', error);
        return {
            statusCode: 500,
            headers,
            body: JSON.stringify({ error: 'Internal server error' }),
        };
    }
    
    // Route to appropriate handler
    let response;
    try {
        if (event.httpMethod === 'GET') {
            response = await handleGet(event, store);
        } else if (event.httpMethod === 'POST') {
            response = await handlePost(event, store);
        } else {
            response = {
                statusCode: 405,
                body: JSON.stringify({ error: 'Method not allowed' }),
            };
        }
    } catch (error) {
        console.error('Handler error:', error);
        response = {
            statusCode: 500,
            body: JSON.stringify({ error: 'Internal server error' }),
        };
    }
    
    // Add CORS headers to response
    return {
        ...response,
        headers: {
            ...headers,
            ...response.headers,
        },
    };
};
