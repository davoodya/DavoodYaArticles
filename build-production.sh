#!/bin/bash
# Build script for production deployment
# Usage: ./build-production.sh

echo "=================================="
echo "Building Hugo Site for Production"
echo "=================================="
echo ""
echo "Base URL: https://davoodya.ir/articles/"
echo ""

# Clean previous build
echo "🧹 Cleaning previous build..."
rm -rf public

# Build with production settings
echo "🏗️  Building site..."
hugo --minify \
     --cleanDestinationDir \
     --gc \
     --verbose

# Check if build was successful
if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Build successful!"
    echo ""
    echo "📂 Output directory: public/"
    echo "📊 Statistics:"
    
    # Count files
    if [ -d "public" ]; then
        html_count=$(find public -name "*.html" | wc -l)
        css_count=$(find public -name "*.css" | wc -l)
        js_count=$(find public -name "*.js" | wc -l)
        img_count=$(find public -type f \( -name "*.jpg" -o -name "*.png" -o -name "*.gif" -o -name "*.webp" \) | wc -l)
        
        echo "   - HTML files: $html_count"
        echo "   - CSS files: $css_count"
        echo "   - JS files: $js_count"
        echo "   - Images: $img_count"
    fi
    
    echo ""
    echo "🚀 Ready to deploy!"
    echo ""
    echo "Next steps:"
    echo "1. Test the build: cd public && python -m http.server 8000"
    echo "2. Upload 'public/' folder to: https://davoodya.ir/articles/"
    echo ""
else
    echo ""
    echo "❌ Build failed!"
    echo "Please check the errors above."
    exit 1
fi
