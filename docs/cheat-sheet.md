# Moderations-Spickzettel

**10 Personen · 5 Teams · 120 Minuten · Setup vorher**

| Minute | Dein nächster Schritt | Prüfen |
| --- | --- | --- |
| 00–15 | Ziel erklären; Working Tree → Index → Commit → Push | Commit ist lokal, Push veröffentlicht |
| 15–35 | Ein Issue und PR pro Team; nach erstem Commit Keyboard wechseln | Richtiger Branch, sinnvolle Commits, PR bleibt offen |
| 35–55 | Review-Ring 1 → 2 → 3 → 4 → 5 → 1, nachbessern, mergen | Beide kommentieren; finales Approve; Create a merge commit |
| 55–80 | Lokales Konfliktlabor pro Person | Mensa + 12:30 + vegetarisches Buffet, sauberer Status |
| 80–100 | Fast-Forward, dann Rebase und Fast-Forward | Kein neuer Commit beim FF; neue ID beim Rebase |
| 100–115 | Lernfragen und drei Alltagsregeln | Erklären lassen, nicht nur Erfolgsmeldung abfragen |
| 115–120 | Puffer | Offene Praxis als nächsten Schritt festhalten |

## Die wichtigste Diagnose

```bash
pwd
git status
git branch --show-current
git remote -v
git log --oneline --graph --decorate --all
```

**Erst sagen lassen, was als Nächstes passieren soll, dann den Befehl wählen.**

## Standardweg im gemeinsamen Repo

```bash
git switch main
git pull --ff-only origin main
git switch -c team-1/hero-copy
# Datei bearbeiten; Branchname und Dateipfad pro Team anpassen.
git diff
git add app/index.md
git diff --staged
git commit -m "docs: clarify festival headline"
git push -u origin team-1/hero-copy
```

Danach PR → Review → Nachbesserung auf demselben Branch → `git push` → finales Review → Merge auf GitHub. Im [Fork-Modell](setup.md#alternative-forks) vom zentralen `upstream/main` starten und aktualisieren.

## Lokale Labore

Aus dem Workshop-Klon `bash scripts/create-labs.sh` ausführen, ausgegebene `cd`-Befehle verwenden. Die folgenden Schritte gehören jeweils in das benannte Labor:

| Labor | Schritte |
| --- | --- |
| `conflict` | Auf `team-b`: `git merge main` → Konflikt erwartet → Datei fachlich lösen → `git diff --check` → `git add program.md` → gestagten Diff prüfen → `git commit` |
| `fast-forward` | Auf `main`: `git merge --ff-only feature/info` → zeigt auf vorhandenen Commit |
| `rebase` | Auf `main`: FF zu `feature/volunteers` scheitert → auf Feature wechseln → `git rebase main` → auf `main` wechseln → FF gelingt |
| `squash` (Bonus) | Auf Feature: `git rebase -i main` → erster `pick`, danach zweimal `squash` |

**Merge abbrechen:** `git merge --abort`. **Rebase abbrechen:** `git rebase --abort`. Gelösten Rebase mit `git add DATEI` und `git rebase --continue` fortsetzen. Vor Beginn sauberer Working Tree; kein blindes Verwerfen von Änderungen.

## Fünf Sätze für einen klaren Auftritt

1. „Ein Commit hält unseren Stand lokal fest; ein Push veröffentlicht ihn.“
2. „Ein Branch ist ein beweglicher Verweis auf einen Commit.“
3. „Git löst Textzusammenführungen; die fachliche Entscheidung treffen wir.“
4. „Fast-Forward bewegt einen Verweis entlang vorhandener History.“
5. „Rebase baut unsere Änderung auf einer neuen Basis auf; gemeinsame History stimmen wir zuerst ab.“

**Falls Zeit fehlt:** Squash streichen, Rebase gemeinsam zeigen, Konfliktpraxis und Reflexion behalten. **Falls eine Frage offenbleibt:** präzise benennen und in der offiziellen Referenz nachschlagen. [Drehbuch](moderation-script.md) · [Glossar](glossary.md) · [Pannenhilfe](trainer-guide.md).
