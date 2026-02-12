/**
 * ===========================
 * Netlify Serverless Function: Admin Comments Management
 * ===========================
 * Handles admin operations: list all, approve, reject, delete
 */

const { getStore } = require('@netlify/blobs');

// ===========================
// Configuration
// ===========================

const CONFIG = {
    STORE_NAME: 'comments',
    ADMIN_PASSWORD: process.env.ADMIN_PASSWORD || 'admin123', // Change in Netlify env vars
};

// ===========================
// Utility Functions
// ===========================

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
        'Access-Control-Allow-Headers': 'Content-Type, Authorization',
        'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
        'Access-Control-Max-Age': '86400',
    };
}

// ===========================
// Storage Functions
// ===========================

async function getAllComments(store) {
    try {
        // Get all article slugs (this is a limitation - we need to track articles separately)
        // For now, return empty - you'll need to implement article tracking
        return [];
    } catch (error) {
        console.error('Error reading all comments:', error);
        return [];
    }
}

async function getCommentsForArticle(store, articleSlug) {
    try {
        const data = await store.get(articleSlug, { type: 'json' });
        return data || { comments: [] };
    } catch (error) {
        console.error('Error reading comments:', error);
        return { comments: [] };
    }
}

async function saveCommentsForArticle(store, articleSlug, data) {
    try {
        await store.setJSON(articleSlug, data);
        return true;
    } catch (error) {
        console.error('Error saving comments:', error);
        return false;
    }
}

// ===========================
// GET Handler - List All Comments (Admin)
// ===========================

async function handleGet(event, store) {
    // Simple auth check (improve this in production)
    const authHeader = event.headers.authorization || event.headers.Authorization;
    const password = authHeader?.replace('Bearer ', '');
    
    if (password !== CONFIG.ADMIN_PASSWORD) {
        return {
            statusCode: 401,
            body: JSON.stringify({ error: 'Unauthorized' }),
        };
    }
    
    // For now, return empty array
    // In production, you'd need to track all article slugs
    return {
        statusCode: 200,
        body: JSON.stringify({ 
            success: true,
            comments: [],
            message: 'Admin panel requires article-specific queries. Use GET /.netlify/functions/admin-comments?article=SLUG'
        }),
    };
}

// ===========================
// POST Handler - Update Comment Status
// ===========================

async function handlePost(event, store) {
    // Simple auth check
    const authHeader = event.headers.authorization || event.headers.Authorization;
    const password = authHeader?.replace('Bearer ', '');
    
    if (password !== CONFIG.ADMIN_PASSWORD) {
        return {
            statusCode: 401,
            body: JSON.stringify({ error: 'Unauthorized' }),
        };
    }
    
    let body;
    try {
        body = JSON.parse(event.body);
    } catch {
        return {
            statusCode: 400,
            body: JSON.stringify({ error: 'Invalid JSON' }),
        };
    }
    
    const { action, article_slug, comment_id } = body;
    
    if (!action || !article_slug || !comment_id) {
        return {
            statusCode: 400,
            body: JSON.stringify({ error: 'Missing required fields: action, article_slug, comment_id' }),
        };
    }
    
    // Get comments for article
    const data = await getCommentsForArticle(store, article_slug);
    const comments = data.comments || [];
    
    // Find comment
    const commentIndex = comments.findIndex(c => c.id === comment_id);
    
    if (commentIndex === -1) {
        return {
            statusCode: 404,
            body: JSON.stringify({ error: 'Comment not found' }),
        };
    }
    
    // Perform action
    switch (action) {
        case 'approve':
            comments[commentIndex].confirmed = true;
            break;
        
        case 'reject':
        case 'unapprove':
            comments[commentIndex].confirmed = false;
            break;
        
        case 'delete':
            comments.splice(commentIndex, 1);
            break;
        
        default:
            return {
                statusCode: 400,
                body: JSON.stringify({ error: 'Invalid action. Use: approve, reject, unapprove, delete' }),
            };
    }
    
    // Save
    data.comments = comments;
    const saved = await saveCommentsForArticle(store, article_slug, data);
    
    if (!saved) {
        return {
            statusCode: 500,
            body: JSON.stringify({ error: 'Failed to save changes' }),
        };
    }
    
    return {
        statusCode: 200,
        body: JSON.stringify({
            success: true,
            message: `Comment ${action} successful`,
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
    
    // Initialize store
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
    
    // Route to handler
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
    
    return {
        ...response,
        headers: {
            ...headers,
            ...response.headers,
        },
    };
};
