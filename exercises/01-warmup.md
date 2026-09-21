# Übung 1: Branch → Commits → Pull Request

**20 Minuten, ein PR pro Zweierteam.** Start: sauberer Working Tree, [Setup](../docs/setup.md) abgeschlossen, Teamauftrag und tatsächliche Issue-Nummer bekannt. Noch nicht mergen.

## Missionen und Abnahmekriterien

| Team | Datei | Auftrag | Inhaltlicher Check |
| --- | --- | --- | --- |
| 1 | [Startseite](../app/index.md) | Klarere Headline und kurzer Aufruf für Helfer:innen | Publikum und gewünschte Handlung sind verständlich |
| 2 | [Programm](../app/program.md) | Zwei Programmpunkte präzisieren, einen Slot um 16:30 ergänzen | Chronologische Reihenfolge, keine doppelte Uhrzeit |
| 3 | [Snacks](../app/snacks.md) | Zwei Beschreibungen verbessern, vegetarisches Spezial ergänzen | Vegetarische Option eindeutig erkennbar |
| 4 | [Kontakte](../app/team.md) | Rollen präzisieren, zusätzliche fiktive Person mit Verantwortung ergänzen | Zuständigkeiten sind unterscheidbar; keine echten Kontaktdaten nötig |
| 5 | [Status](../app/status-board.md) | Zwei Statuszeilen präzisieren, eine Tagesinfo ergänzen | Erledigt/offen und nächste Handlung sind erkennbar |

## Schritte

1. Issue übernehmen oder die Zuständigkeit mit der Moderation festhalten.
2. Aktuellen Stand holen und einen Feature-Branch erstellen. Beispiel für Team 1; andere Teams passen Branchname und Dateipfad an:

   ```bash
   git status
   git switch main
   git pull --ff-only origin main
   git switch -c team-1/hero-copy
   ```

3. Erste Teiländerung im Editor vornehmen. Dann **vor** dem Commit kontrollieren:

   ```bash
   git diff
   git add app/index.md
   git diff --staged
   git commit -m "docs: clarify festival headline"
   ```

4. Keyboard wechseln. Zweite sinnvolle Teiländerung bearbeiten, erneut Diff ansehen, dieselbe Datei stagen und committen. Zwei Commits sollen zwei nachvollziehbare Schritte zeigen; keine künstlichen Tippfehler einbauen.
5. Veröffentlichen:

   ```bash
   git status
   git push -u origin team-1/hero-copy
   ```

6. Auf GitHub **Pull requests → New pull request**, Basis `main`, Vergleich euer Feature-Branch. Titel und Vorlage ausfüllen. Issue mit `Closes #NUMMER` verbinden, Nummer ersetzen. Beschreibt auch, wie ihr den Inhalt geprüft habt.

## Fertig, wenn

- [ ] Beide Personen haben Git am Keyboard verwendet.
- [ ] Der PR enthält nur die beabsichtigte Datei und mindestens zwei sinnvolle Commits.
- [ ] Ziel, Änderung und Prüfung sind für das nächste Team verständlich.
- [ ] Die GitHub-Markdown-Vorschau wurde gelesen; der PR bleibt für Runde 2 offen.

**Kontrollfrage:** Ist ein Commit bereits auf GitHub sichtbar? Erst nach einem Push; der PR ist anschliessend der Ort für Review und Integration.
