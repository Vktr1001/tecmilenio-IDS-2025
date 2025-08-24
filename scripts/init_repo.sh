#!/usr/bin/env bash
set -euo pipefail

# Inicializa el repo, configura usuario local y hace el primer commit/push.
# Uso:
#   ./scripts/init_repo.sh <github_repo_url>
#
# Ejemplo:
#   ./scripts/init_repo.sh https://github.com/Vktr1001/tecmilenio-IDS-2025.git

if [ $# -lt 1 ]; then
  echo "Uso: $0 <github_repo_url>"
  exit 1
fi

REPO_URL="$1"

git init
git config user.name "Vktr1001"
git config user.email "vk.src9@gmail.com"

git add .
git commit -m "feat: Act01 calculadora de uso digital (estructura inicial)"
git branch -M main
git remote add origin "$REPO_URL"
git push -u origin main
