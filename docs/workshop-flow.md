# Fahrplan für 120 Minuten

Voraussetzung: [Setup](setup.md) ist abgeschlossen. [Drehbuch](moderation-script.md) enthält Sprechtexte und Interventionen.

| Minuten | Auftrag | Checkpoint für die Moderation |
| --- | --- | --- |
| 00–05 | Ziel, Campus-Szenario, Teams, Arbeitsorte erklären | Fünf Teams kennen ihren Auftrag |
| 05–12 | Working Tree → Staging Area → Commit; Branch und PR zeigen | Gruppe unterscheidet Commit und Push |
| 12–15 | `git status`, Remote und Anmeldung kurz prüfen | Alle können starten; Setup-Probleme sofort paarweise abfedern |
| 15–25 | [Warmup](../exercises/01-warmup.md): Branch, erste Änderung, erster Commit | Fünf richtige Feature-Branches |
| 25–35 | Keyboard wechseln; zweite Änderung, Push, PR | Fünf offene PRs mit Ziel und Prüfschritten; nicht mergen |
| 35–43 | [Review](../exercises/02-review-cycle.md) im Ring | Jede Person hat einen begründeten Beitrag geschrieben |
| 43–50 | Eine echte Verbesserung einarbeiten und erneut prüfen | Feedback beantwortet, finaler Diff geprüft |
| 50–55 | Approve, freigegebene PRs mergen, `main` lokal aktualisieren | Fünf gemergte PRs; keine offenen Change Requests |
| 55–60 | [Labore](../exercises/03-conflicts.md) erstellen, Branchgraph lesen | Jede Person ist im Verzeichnis `conflict` |
| 60–72 | Merge starten, Konflikt lesen und fachlich lösen | Konfliktmarker entfernt, Datei geprüft, Merge-Commit erstellt |
| 72–80 | Lösung erklären; bei geteiltem Laptop zweiter Durchlauf | Jede Person kann Ursache und Entscheidung erklären |
| 80–87 | [Fast-Forward](../exercises/04-history-cleanup.md) durchführen | Branch zeigt auf vorhandenen Commit; kein neuer Commit |
| 87–97 | Fehlgeschlagenes Fast-Forward, Rebase, erneutes Fast-Forward | Neue Commit-ID und neue Basis erkannt |
| 97–100 | Vergleich; optional Squash nur bei Zeitreserve | Merge, Rebase und Squash begrifflich getrennt |
| 100–110 | Drei bis vier Lernfragen mit Begründung | Verständnis prüfen, nicht nur Befehle abfragen |
| 110–115 | Drei Teamregeln festhalten | Konkreter Transfer in den Arbeitsalltag |
| 115–120 | Puffer und Abschluss | Offene Punkte und nächster Übungsschritt benannt |

## Wenn die Zeit knapp wird

Um Minute 35 reichen ein sinnvoller Commit und ein beschriebener PR pro Team; den Rollenwechsel trotzdem durchführen. Bei langsamen Reviews bis Minute 60 verlängern, Squash streichen und Rebase kurz gemeinsam demonstrieren. Den Konflikt-Durchlauf und mindestens fünf Minuten Reflexion erhalten. Fehlende individuelle Praxis ausdrücklich als Anschlussaufgabe festhalten.

## Wenn die Gruppe schneller ist

Das optionale Squash-Labor verwenden oder einen echten PR-Konflikt nach der [Transferaufgabe](../exercises/03-conflicts.md#transfer-ein-konflikt-im-github-pr-optional) nachstellen. Zusätzliche Challenges erst nach dem Checkpoint der gesamten Gruppe starten.
