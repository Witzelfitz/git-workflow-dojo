# Trainer Guide: Vorbereitung und Hilfe im Raum

Der minutengenaue Sprechtext steht im [Drehbuch](moderation-script.md), Begriffe und Fachfragen im [Glossar](glossary.md). Das [Setup](setup.md) vorab erledigen; Installation und Kontenprobleme sind nicht in den 120 Minuten eingerechnet.

## Vor dem Termin

- [ ] Frisches Workshop-Repo und fünf Aufgaben vorbereitet, Teamliste und Review-Ring bekannt.
- [ ] Schreibrechte angenommen, ein Push sowie Review durch ein zweites Konto getestet.
- [ ] Schutz von `main` geprüft; Merge-Commits erlaubt, keine unpassende Pflicht zu linearer History.
- [ ] Terminal und Editor auf dem Beamer gut lesbar, Benachrichtigungen aus, Browser auf PR-Ansicht.
- [ ] Alle lokalen Labore einmal durchgespielt; insbesondere den erwarteten Konflikt und das erwartete Scheitern von `--ff-only` gesehen.
- [ ] Optional als technische Vorprüfung `python3 scripts/test-labs.py` ausgeführt; benötigt Python 3 nur auf dem Gerät der Moderation.
- [ ] Drehbuch, Spickzettel und ein lokaler Repository-Klon auch offline verfügbar.

## Editor vor der Session testen

Für den optionalen interaktiven Rebase braucht Git einen Editor, der wartet, bis die Datei gespeichert und geschlossen wurde. Im jeweiligen Labor lokal konfigurieren, zum Beispiel:

```bash
# Nur eine passende Variante wählen.
git config core.editor "code --wait"
# Alternative, falls nano installiert ist:
git config core.editor "nano"
```

Bei VS Code muss der `code`-Befehl im Terminal verfügbar sein. Bei Nano: speichern mit Ctrl+O, Enter, schliessen mit Ctrl+X. Falls ungewollt Vim startet: Esc, `:wq`, Enter zum Speichern oder Esc, `:cq`, Enter zum Abbrechen des Editoraufrufs. Anschliessend `git status` lesen; bei laufendem Rebase gegebenenfalls `git rebase --abort`. Ein konfigurierter `sequence.editor` kann beim interaktiven Rebase Vorrang vor `core.editor` haben.

## Hilfe ohne die Lösung wegzunehmen

Zuerst drei Fragen stellen: „In welchem Repository bist du? Auf welchem Branch? Was sagt `git status`?“ Dann die Person die beabsichtigte Zustandsänderung formulieren lassen. Erst danach den Befehl auswählen.

| Symptom | Prüfung und Hilfe |
| --- | --- |
| `not a git repository` | `pwd` und Verzeichnis prüfen; in den Klon bzw. den ausgegebenen Laborpfad wechseln. |
| `Author identity unknown` | Im Workshop-Klon lokale Identität gemäss Setup setzen. Labore haben eine eigene Übungsidentität. |
| Push verweigert / 403 | `git remote -v`, angemeldetes Konto, angenommene Einladung und Schreibrechte prüfen. Im Fork-Modell zum eigenen `origin` pushen. |
| `non-fast-forward` beim Push | Stoppen, `git fetch origin`, Graph anschauen. Fremde Commits integrieren; ein Force Push ist hier keine Standardreparatur. |
| `pull --ff-only` scheitert | Lokaler und entfernter Branch sind auseinander gelaufen. `git log --oneline --graph --decorate --all` lesen und die lokalen Commits zuerst mit einem neuen Sicherungsbranch festhalten. Gemeinsam klären, wie sie erhalten bleiben. |
| Branchwechsel wegen Änderungen blockiert | Diff lesen; passende Arbeit auf dem richtigen Branch committen. Änderungen nicht blind verwerfen. |
| PR hat falsche Dateien / falsche Basis | Base/Compare prüfen und Diff gemeinsam lesen. Nur den beabsichtigten Branch verwenden. |
| Kommentar ist für andere unsichtbar | Ausstehendes Review über „Submit review“ absenden. |
| Merge bleibt trotz Gespräch gesperrt | Erforderliche Freigabe, Change Request, offene Threads und Regeln prüfen; „Resolve conversation“ ist kein Approve. |
| Im Konfliktlabor kein Konflikt | Richtiges, frisches Labor? Branch `team-b`? Wurde der Merge schon abgeschlossen? Neu erzeugen; bestehendes Labor behalten. |
| Rebase stoppt mit Konflikt | Datei lösen, stagen, `git rebase --continue`; Status erneut lesen. `--skip` würde den aktuellen Patch überspringen und ist keine pauschale Lösung. |
| GitHub oder WLAN fällt aus | Lokale Labore weiterführen. Diff-Review paarweise mündlich üben; GitHub-PR/Review als noch offene Anschlussaufgabe dokumentieren. |

`git merge --abort` gehört zu einem laufenden Merge, `git rebase --abort` zu einem laufenden Rebase. Vor beiden Operationen einen sauberen Working Tree herstellen. Im Workshop kein `reset --hard` als schnelle Fehlerbehebung einsetzen.

## Erfolg beobachten

Am Ende nicht nur fragen „Hat es funktioniert?“, sondern Belege zeigen lassen: PR mit Feedback, eigener Review-Beitrag, gelöste Lunch-Zeile, Merge-Commit und Vorher-/Nachher-IDs beim Rebase. Wer Schritte nur beobachtet hat, bekommt einen zweiten eigenen Durchlauf.

Bei Überlastung: Squash streichen, Rebase gemeinsam demonstrieren, Konflikt und Reflexion erhalten. [Zeitplan](workshop-flow.md) nennt die Checkpoints.
