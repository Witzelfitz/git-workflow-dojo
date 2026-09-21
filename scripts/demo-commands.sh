#!/usr/bin/env bash
# Prints examples only; does not execute Git operations.
set -euo pipefail

cat <<'EOF'
Beispielbefehle für Team 1 im gemeinsamen Workshop-Repository.
Voraussetzung: Setup abgeschlossen, sauberer Working Tree.
Andere Teams passen Branchname und Dateipfad an.

git status
git switch main
git pull --ff-only origin main
git switch -c team-1/hero-copy
# Jetzt app/index.md bearbeiten.
git diff
git add app/index.md
git diff --staged
git commit -m "docs: clarify festival headline"
# Keyboard wechseln, zweite Änderung prüfen und committen.
git push -u origin team-1/hero-copy

Danach auf GitHub: PR erstellen, Review geben, nachbessern, finales Review,
Create a merge commit. Der PR bleibt bis zur Review-Runde offen.
Im Fork-Modell siehe docs/setup.md für upstream/main.

Lokale Labore für Konflikte, Fast-Forward, Rebase und Squash:
bash scripts/create-labs.sh
# Einen der ausgegebenen cd-Befehle verwenden.
# Weiter mit exercises/03-conflicts.md und exercises/04-history-cleanup.md.

Diagnose:
git status
git log --oneline --graph --decorate --all
EOF
