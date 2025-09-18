#!/bin/bash

# Setup script for MkDocs documentation structure
# This script creates the docs directory structure and moves existing content

echo "🚀 Setting up MkDocs documentation structure..."

# Create docs directory if it doesn't exist
mkdir -p docs

# Create subdirectories for each module
modules=(
    "git_version_control"
    "ansible_basics"
    "ansible_advanced"
    "ansible_roles"
    "docker_fundamentals"
    "docker_orchestration"
    "terraform_basics"
    "ci_cd_advanced"
    "kubernetes_overview"
)

# Create module directories and move content
for module in "${modules[@]}"; do
    echo "📁 Setting up $module..."
    
    # Create module directory in docs
    mkdir -p "docs/$module"
    
    # Move existing files if they exist
    if [ -f "$module/lecture.md" ]; then
        cp "$module/lecture.md" "docs/$module/"
        echo "  ✅ Moved lecture.md"
    fi
    
    if [ -f "$module/lab.md" ]; then
        cp "$module/lab.md" "docs/$module/"
        echo "  ✅ Moved lab.md"
    fi
    
    if [ -f "$module/homework.md" ]; then
        cp "$module/homework.md" "docs/$module/"
        echo "  ✅ Moved homework.md"
    fi
    
    if [ -f "$module/reading_materials.md" ]; then
        cp "$module/reading_materials.md" "docs/$module/"
        echo "  ✅ Moved reading_materials.md"
    fi
    
    # Copy examples and reference directories if they exist
    if [ -d "$module/examples" ]; then
        cp -r "$module/examples" "docs/$module/"
        echo "  ✅ Copied examples directory"
    fi
    
    if [ -d "$module/reference" ]; then
        cp -r "$module/reference" "docs/$module/"
        echo "  ✅ Copied reference directory"
    fi
done

# Copy curriculum.md to docs
if [ -f "curriculum.md" ]; then
    cp "curriculum.md" "docs/"
    echo "✅ Moved curriculum.md"
fi

# Create additional directories
mkdir -p docs/stylesheets
mkdir -p docs/javascripts

# Create basic CSS file
cat > docs/stylesheets/extra.css << 'EOF'
/* Custom styles for the automation course */

/* Course-specific styling */
.course-header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 2rem;
    border-radius: 8px;
    margin-bottom: 2rem;
}

.module-card {
    border: 1px solid #e1e4e8;
    border-radius: 6px;
    padding: 1rem;
    margin-bottom: 1rem;
    transition: box-shadow 0.2s ease;
}

.module-card:hover {
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

.practical-exercise {
    background-color: #f6f8fa;
    border-left: 4px solid #0366d6;
    padding: 1rem;
    margin: 1rem 0;
}

.reading-material {
    background-color: #fff3cd;
    border-left: 4px solid #ffc107;
    padding: 1rem;
    margin: 1rem 0;
}
EOF

# Create basic JavaScript file
cat > docs/javascripts/extra.js << 'EOF'
// Custom JavaScript for the automation course

// Add smooth scrolling to anchor links
document.addEventListener('DOMContentLoaded', function() {
    const links = document.querySelectorAll('a[href^="#"]');
    
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
});

// Add copy button to code blocks
document.addEventListener('DOMContentLoaded', function() {
    const codeBlocks = document.querySelectorAll('pre code');
    
    codeBlocks.forEach(block => {
        const button = document.createElement('button');
        button.textContent = 'Kopeeri';
        button.className = 'copy-button';
        button.style.cssText = `
            position: absolute;
            top: 0.5rem;
            right: 0.5rem;
            background: #0366d6;
            color: white;
            border: none;
            border-radius: 4px;
            padding: 0.25rem 0.5rem;
            font-size: 0.8rem;
            cursor: pointer;
        `;
        
        button.addEventListener('click', function() {
            navigator.clipboard.writeText(block.textContent);
            this.textContent = 'Kopeeritud!';
            setTimeout(() => {
                this.textContent = 'Kopeeri';
            }, 2000);
        });
        
        const pre = block.parentElement;
        pre.style.position = 'relative';
        pre.appendChild(button);
    });
});
EOF

echo ""
echo "✅ Documentation structure setup complete!"
echo ""
echo "📋 Next steps:"
echo "1. Review the docs/ directory structure"
echo "2. Update mkdocs.yml with your GitHub username"
echo "3. Test locally: mkdocs serve"
echo "4. Push to GitHub and enable GitHub Pages"
echo ""
echo "🌐 Your site will be available at: https://your-username.github.io/automation-course"
