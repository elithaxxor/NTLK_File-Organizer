#!/usr/bin/env bash
mkdir new_repo
cd new_repo
git init

cat << EOF > .gitignore
# Ignore common Python files
__pycache__/
*.pyc
*.pyo
*.pyd
*.egg-info/
*.egg
dist/
build/
EOF

git add .
git commit -m \"Initial commit with .gitignore\"    git init
    