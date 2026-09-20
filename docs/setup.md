# Setup vor dem Workshop

Zeitbedarf vorab: etwa 15–30 Minuten. Git ab 2.28, ein Texteditor, Browser, GitHub-Konto und Bash müssen verfügbar sein. Unter Windows die Befehle in **Git Bash** ausführen; die Skripte sind keine PowerShell-Skripte.

## Moderation: gemeinsames Repository vorbereiten

1. Eine frische Workshop-Kopie mit dem aktuellen Inhalt dieses Repos erstellen, zum Beispiel als GitHub-Template-Kopie, falls die Template-Funktion aktiviert ist. Einen eindeutigen Namen wie `git-dojo-2026-09-team` wählen. Die Vorlage für weitere Durchführungen behalten.
2. Allen Teilnehmenden Schreibrechte geben; Einladungen vorab annehmen lassen. Zwei verschiedene Konten für Autor und Reviewer testen.
3. Fünf Issues gemäss [Warmup](../exercises/01-warmup.md) anlegen. Issues, offene PRs und Repository-Einstellungen werden bei einer reinen Inhaltskopie nicht übernommen. Alternativ die Aufgaben ohne Issues verteilen und dieses reduzierte Lernziel benennen.
4. Für `main` Branch Protection oder ein passendes Ruleset aktivieren: PR erforderlich, mindestens ein zustimmendes Review, offene Review-Diskussionen vor Merge klären, Force Push und Löschen verbieten. Bypass-Rechte bewusst prüfen; Admins sind nicht automatisch überall eingeschränkt.
5. **Merge commits erlauben**, lineare History für diese Session nicht erzwingen. Die anderen Merge-Optionen können bleiben; die Gruppe verwendet in Runde 2 ausdrücklich **Create a merge commit**.
6. Nur tatsächlich vorhandene CI-Checks als Pflicht konfigurieren. Dieses Repository enthält keinen App-Build und keinen CI-Workflow. Geprüft werden Diff, Markdown-Vorschau und Auftrag.
7. URL, Teamzuordnung und [Drehbuch](moderation-script.md) bereitlegen. Alle vier Labore einmal durchspielen.

Die GitHub-Einstellungen sind eine Vorbereitungsliste; diese Dokumentation aktiviert sie nicht. Wie erforderliche Reviews, Bypass und lineare History zusammenwirken, beschreibt [GitHub zu geschützten Branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches).

## Teilnehmende: Klon und Identität prüfen

Im Terminal zuerst `git --version` prüfen. Die Moderation gibt die tatsächliche Workshop-URL bekannt. Im Browser **Code → HTTPS/SSH** wählen und den Clone-Befehl mit dieser URL ausführen, danach in den geklonten Ordner wechseln. Das Original-Repo nur verwenden, wenn die Moderation es ausdrücklich als Workshop-Repo festlegt.

Im Repository:

```bash
git status
git remote -v
git config user.name
git config user.email
```

Falls Name oder E-Mail fehlen, **lokal in diesem Repository** setzen, mit den eigenen Angaben:

```bash
git config user.name "Vorname Nachname"
git config user.email "DEINE-GITHUB-NOREPLY-ADRESSE"
```

Die Adresse oben ist ein Platzhalter. Die eigene No-Reply-Adresse steht in den GitHub-E-Mail-Einstellungen. Die Git-Identität ist unabhängig von der Anmeldung für Push und Pull.

Push-Zugriff vorab mit einem eigenen Prüfbranch testen, zum Beispiel `setup/dein-kuerzel`. Das Kürzel ersetzen; jeder Prüfbranch muss eindeutig sein:

```bash
git switch -c setup/dein-kuerzel
git push -u origin setup/dein-kuerzel
git switch main
git push origin --delete setup/dein-kuerzel
git branch -d setup/dein-kuerzel
```

Es entstehen keine neuen Commits. Nur den gerade selbst erstellten Prüfbranch löschen. Scheitert die Anmeldung, den eingerichteten Git-Credential-Manager oder SSH verwenden; das GitHub-Kontopasswort ist kein Git-HTTPS-Passwort. Danach `bash scripts/create-labs.sh` einmal testen und den ausgegebenen Pfad aufbewahren. Im Workshop für jeden Durchlauf frische Labore erzeugen.

## Alternative: Forks

Für diese Variante vorab mehr Setup-Zeit einplanen. Pro Team arbeitet ihr in einem Fork; PRs gehen an das zentrale **Workshop-Repository**. `origin` bezeichnet den Fork, ein zusätzliches Remote namens `upstream` das zentrale Repository. Die Moderation liefert dessen URL:

```text
git remote add upstream WORKSHOP-URL
git fetch upstream
git switch -c team-1/hero-copy upstream/main
```

`WORKSHOP-URL` ersetzen; die Befehle sind ein Muster. Push erfolgt zu `origin`. Beim PR **base repository = zentraler Workshop**, **base = main**, **head repository = eigener Fork**, **compare = Feature-Branch** wählen. Nach einem Merge aktualisiert ihr den lokalen `main` mit:

```bash
git fetch upstream
git switch main
git merge --ff-only upstream/main
```

In den Übungen ersetzt ihr beim Aktualisieren `origin/main` durch `upstream/main`. Review-Beiträge von Personen ohne Schreibrechte zählen je nach Schutzregel nicht als erforderliche Freigabe; die Moderation mit passenden Rechten prüft und genehmigt zusätzlich. Runden 3 und 4 bleiben unverändert lokal.
