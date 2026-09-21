#!/usr/bin/env bash

set -euo pipefail

cat <<'EOF'
Beispielbefehle für den Workshop:

git switch -c team-1/hero-copy
git status
git add .
git commit -m "feat: improve hero section"
git push -u origin team-1/hero-copy

git fetch origin
git rebase origin/main

git log --oneline --graph --all
EOF
