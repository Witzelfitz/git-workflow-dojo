# Trainer Guide

## Lernziele

Die Gruppe soll nicht nur Befehle sehen, sondern typische Team-Probleme selbst erleben:

- gleichzeitig an verwandten Bereichen arbeiten
- Review-Kommentare sauber einarbeiten
- Konflikte ohne Panik lösen
- Unterschiede zwischen Merge, Rebase und Fast-Forward verstehen

## Vorbereitung vor dem Workshop

1. Repo für alle freigeben
2. Branch-Schutz auf `main` prüfen (für dieses Repository eingerichtet):
   - Änderungen nur über Pull Requests mit mindestens einer Freigabe
   - neue Änderungen nach einer Freigabe erneut reviewen
   - offene Review-Diskussionen vor dem Merge klären
   - direkte Pushes, Force-Pushes und Löschen von `main` sperren, auch für Admins
   - Merge-Commits erlauben; keine lineare History erzwingen
   - bei Workshop-Kopien dieselben Regeln separat einrichten
3. Teams einteilen
4. Entscheiden, ob GitHub oder GitLab verwendet wird

## Gute Moderationsfragen

- Warum sollte dieser Commit später noch lesbar sein?
- Ist der PR für andere verständlich?
- Was würdest du als Reviewer ohne Kontext nicht verstehen?
- Welche Version wollt ihr beim Konflikt behalten und warum?
- War Rebase hier hilfreich oder nur zusätzlicher Stress?

## Typische Stolpersteine

- alle committen direkt auf `main`
- Branches heissen `test2` oder `neu`
- PR-Beschreibungen sind leer
- Review ist nur "ok"
- Konflikte werden per Copy-Paste gelöst, ohne zu verstehen was passiert

## Minimalziel

Wenn die Zeit knapp wird, dann müssen alle mindestens das hier gemacht haben:

1. Branch erstellt
2. PR erstellt
3. Review-Kommentar geschrieben
4. echten Konflikt gelöst

## Bonusziel

Wenn die Gruppe schnell ist:

- Commit-History aufräumen
- Squash vs Merge Commit vergleichen
- fast-forward-only lokal erklären; auf dem geschützten GitHub-`main` weiterhin PRs verwenden
- lokales `git log --oneline --graph --all` gemeinsam lesen
