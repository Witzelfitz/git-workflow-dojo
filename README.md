# Git Workflow Dojo

Zwei Stunden Git-Praxis für zehn Personen in fünf Zweierteams: vom Issue über Branch, Commit und Pull Request bis zu Review, Konfliktlösung und verständlicher History. Ihr bearbeitet die Markdown-Inhalte eines fiktiven Campus-Festivals; Programmierkenntnisse und ein App-Build sind nicht nötig.

## Schnellstart

- **Teilnehmende:** [Setup](docs/setup.md) vorab erledigen, dann [Teamrollen](docs/roles.md) und [Übung 1](exercises/01-warmup.md) öffnen.
- **Moderation:** [Vorbereitung](docs/trainer-guide.md), [Drehbuch mit Sprechtext](docs/moderation-script.md) und [Spickzettel](docs/cheat-sheet.md).
- **Visuelle Präsentation:** [25 Folien mit Diagrammen und Sprechernotizen](presentation/README.md), als PowerPoint, PDF und offline nutzbare Browser-Version.
- **Begriffe nachschlagen:** [Glossar und typische Fachfragen](docs/glossary.md).
- **Gesamtüberblick:** [Zeitplan](docs/workshop-flow.md) und [Review der ursprünglichen Übung](docs/review-notes.md).

## Was ihr am Ende könnt

Pro Zweierteam: ein Issue übernehmen, einen Feature-Branch mit zwei sinnvollen Commits erstellen, einen PR beschreiben, Feedback einarbeiten und den geprüften PR mergen.

Pro Person: Git-Befehle selbst ausführen, einen Review-Beitrag unter dem eigenen GitHub-Konto geben, im lokalen Labor einen echten Konflikt lösen sowie Fast-Forward und Rebase erklären. Wer einen eigenen vollständigen PR-Durchlauf pro Person möchte, plant eine zweite Runde und mindestens 30 Minuten zusätzlich ein.

## Ablauf: 120 Minuten

| Zeit | Inhalt | Sichtbares Ergebnis |
| --- | --- | --- |
| 00–15 | Einstieg und kurzer Setup-Check | Alle kennen Arbeitsverzeichnis, Staging Area und Commit |
| 15–35 | [Branch, Commits, PR](exercises/01-warmup.md) | Fünf offene PRs; noch nicht mergen |
| 35–55 | [Review und Nachbesserung](exercises/02-review-cycle.md) | Geprüfte PRs sind gemergt |
| 55–80 | [Konfliktlabor](exercises/03-conflicts.md) | Jede Person löst denselben reproduzierbaren Konflikt |
| 80–100 | [Fast-Forward und Rebase](exercises/04-history-cleanup.md) | History vorher/nachher vergleichen; Squash optional |
| 100–120 | Debrief, Lernkontrolle und Puffer | Gemeinsame Regeln für den Alltag |

Das [Setup](docs/setup.md) findet **vor den zwei Stunden** statt. Ohne Vorwissen in Terminal und Git-Grundbefehlen sind eher 150–180 Minuten sinnvoll.

## Zwei Arbeitsorte

1. **Workshop-Repository auf GitHub:** Runden 1 und 2 im gemeinsamen Repo mit Schreibrechten. Für jede Durchführung eine frische Workshop-Kopie verwenden. [Fork-Alternative](docs/setup.md#alternative-forks) nur nach vorheriger Vorbereitung.
2. **Lokale Labore ohne Remote:** Runden 3 und 4 auf jedem Laptop. Im geklonten Workshop-Repository ausführen:

   ```bash
   bash scripts/create-labs.sh
   ```

   Das Skript zeigt die vier neuen Verzeichnisse samt `cd`-Befehlen an. Es bereitet Ausgangszustände vor; die eigentlichen Konflikte und History-Schritte führt ihr selbst aus. Voraussetzungen: Git ab 2.28 und Bash; unter Windows Git Bash verwenden. Labore liegen standardmässig im temporären Verzeichnis.

## Spielregeln

- Im gemeinsamen Repository bleibt `main` geschützt: Feature-Branch → PR → Review → Merge.
- Erst nach Runde 2 mergen, mit **Create a merge commit**. So bleiben die Team-Commits sichtbar.
- Vor Git-Operationen `git status` lesen; nur beabsichtigte Dateien stagen.
- Die Person am Keyboard erklärt ihre Absicht, die andere prüft mit. Rollenwechsel ist Teil der Übung.
- Rebase und Squash üben wir an unveröffentlichten lokalen Branches. Die isolierten Labore dürfen direkte Änderungen an ihrem eigenen `main` enthalten.

Der Beispielinhalt liegt in [app/](app/). Alle Unterlagen sind auf GitHub ausgerichtet; „Merge Request“ ist die bei GitLab übliche Bezeichnung für denselben Review-Ablauf.

## Labore prüfen

Für die Pflege der Übung gibt es einen Ende-zu-Ende-Test mit Python 3, Bash und Git, ohne zusätzliche Pakete:

```bash
python3 scripts/test-labs.py
```

Er prüft die vier Git-Szenarien, den Merge-Abbruch sowie frische und bereits bestehende Zielverzeichnisse. Die Teilnehmenden benötigen für die Labore selbst kein Python. Ein bestandener Test ersetzt keine Probe der GitHub-Rechte und Reviews vor der Session.
