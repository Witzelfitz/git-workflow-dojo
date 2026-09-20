#!/usr/bin/env bash
# Creates disposable, independent repositories; never edits the workshop repo.
set -euo pipefail

if [ "$#" -gt 1 ]; then
  printf 'Usage: bash scripts/create-labs.sh [new-directory]\n' >&2
  exit 2
fi
command -v git >/dev/null || { printf 'Git is required.\n' >&2; exit 1; }

if [ "$#" -eq 1 ]; then
  # mkdir deliberately refuses existing directories, including symlinks.
  mkdir -- "$1"
  lab_root=$(cd -- "$1" && pwd -P)
else
  lab_root=$(mktemp -d "${TMPDIR:-/tmp}/git-workflow-dojo.XXXXXX")
  lab_root=$(cd -- "$lab_root" && pwd -P)
fi

init_lab() {
  git init -q --template= -b main "$lab_root/$1"
  cd -- "$lab_root/$1"
  git config user.name 'Git Dojo'
  git config user.email 'git-dojo@example.invalid'
  git config commit.gpgSign false
  git config tag.gpgSign false
  mkdir .git/no-hooks
  git config core.hooksPath .git/no-hooks
  git config core.autocrlf false
  git config core.excludesFile /dev/null
  git config merge.conflictStyle merge
  git config merge.ff true
  git config rerere.enabled false
  git config rebase.updateRefs false
  printf '# Campus Festival – lokales Übungslabor\n' > README.md
  git add README.md
  git commit -qm 'docs: start festival lab'
}

init_lab conflict
printf '%s\n' '- 12:00 Lunch im Innenhof' > program.md
git add program.md
git commit -qm 'docs: add lunch slot'
git switch -qc team-a
printf '%s\n' '- 12:00 Lunch in der Mensa' > program.md
git commit -qam 'docs: move lunch indoors'
git switch -qc team-b main
printf '%s\n' '- 12:30 Lunch im Innenhof mit vegetarischem Buffet' > program.md
git commit -qam 'docs: reschedule lunch and add buffet'
git switch -q main
git merge --ff-only team-a >/dev/null
git switch -q team-b

init_lab fast-forward
git switch -qc feature/info
printf '%s\n' 'Einlass ab 09:30.' > info.md
git add info.md
git commit -qm 'docs: add arrival information'
git switch -q main

init_lab rebase
git switch -qc feature/volunteers
printf '%s\n' 'Treffpunkt für Helfer:innen: Eingang Nord.' > volunteers.md
git add volunteers.md
git commit -qm 'docs: add volunteer meeting point'
git branch before-rebase
git switch -q main
printf '%s\n' 'Bei Regen findet das Festival drinnen statt.' > weather.md
git add weather.md
git commit -qm 'docs: add wet weather information'
git switch -q feature/volunteers

init_lab squash
git switch -qc feature/snacks
printf '%s\n' '# Snacks' > snacks.md
git add snacks.md
git commit -qm 'docs: start snack menu'
printf '\n%s\n' '- Falafel-Wrap' >> snacks.md
git commit -qam 'docs: add vegetarian snack'
printf '%s\n' '- Wasser und hausgemachter Eistee' >> snacks.md
git commit -qam 'docs: add drinks'

printf '\nVier lokale Labore erstellt: %s\n' "$lab_root"
printf 'Konflikte:    cd %q\n' "$lab_root/conflict"
printf 'Fast-Forward: cd %q\n' "$lab_root/fast-forward"
printf 'Rebase:       cd %q\n' "$lab_root/rebase"
printf 'Squash:       cd %q\n' "$lab_root/squash"
printf '\nKein Remote eingerichtet. Anleitung: exercises/03-conflicts.md und 04-history-cleanup.md\n'
printf 'Für einen neuen Versuch das Skript erneut ausführen; bestehende Labore bleiben erhalten.\n'
