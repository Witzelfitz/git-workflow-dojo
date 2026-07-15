# Trainer Guide

## Lernziele

Die Gruppe soll nicht nur Befehle sehen, sondern typische Team-Probleme selbst erleben:

- gleichzeitig an verwandten Bereichen arbeiten
- Review-Kommentare sauber einarbeiten
- Konflikte ohne Panik loesen
- Unterschiede zwischen Merge, Rebase und Fast-Forward verstehen

## Vorbereitung vor dem Workshop

1. Repo fuer alle freigeben
2. Optional Branch Protection auf `main` aktivieren:
   - direct pushes verbieten
   - 1 Review verlangen
3. Teams einteilen
4. Entscheiden, ob GitHub oder GitLab verwendet wird

## Gute Moderationsfragen

- Warum sollte dieser Commit spaeter noch lesbar sein?
- Ist der PR fuer andere verstaendlich?
- Was wuerdest du als Reviewer ohne Kontext nicht verstehen?
- Welche Version wollt ihr beim Konflikt behalten und warum?
- War Rebase hier hilfreich oder nur zusaetzlicher Stress?

## Typische Stolpersteine

- alle committen direkt auf `main`
- Branches heissen `test2` oder `neu`
- PR-Beschreibungen sind leer
- Review ist nur "ok"
- Konflikte werden per Copy-Paste geloest, ohne zu verstehen was passiert

## Minimalziel

Wenn die Zeit knapp wird, dann muessen alle mindestens das hier gemacht haben:

1. Branch erstellt
2. PR erstellt
3. Review-Kommentar geschrieben
4. echten Konflikt geloest

## Bonusziel

Wenn die Gruppe schnell ist:

- Commit-History aufraeumen
- Squash vs Merge Commit vergleichen
- fast-forward-only erklaeren
- lokales `git log --oneline --graph --all` gemeinsam lesen
