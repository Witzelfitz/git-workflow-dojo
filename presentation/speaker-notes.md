# Git wird greifbar – Sprechernotizen

25 Folien, passend zum 120-Minuten-Dojo. Zeitangaben der Praxisfolien umfassen die vorherigen Kurzimpulse der jeweiligen Runde.

## 01 · Git wird greifbar.

Begrüsse die Gruppe: Wir betreiben gemeinsam die Infoseiten eines Campus-Festivals. Die Inhalte sind klein; wir üben den Weg von einer Idee bis zu einer geprüften Änderung. Zehn Personen, fünf Zweierteams, zwei Stunden. Diese Präsentation wird in kurzen Impulsen zwischen den Praxisphasen genutzt.

## 02 · Welche Version gilt?

Zeige die linke Seite und frage: Wer kennt final_final? Git macht Änderungen, ihre Reihenfolge und ihren Kontext nachvollziehbar. Ein Commit ist ein Projektstand mit Metadaten und Elternverweisen, keine weitere Datei namens final. Der Diff hilft beim Vergleich.

## 03 · Git ist lokal. GitHub verbindet.

Git ist das Versionskontrollsystem und läuft auch ohne Netzwerk. GitHub hostet Repositories und ergänzt PRs, Reviews und Rechte. Push überträgt Objekte und aktualisiert den Server-Branch. Fetch holt Objekte und aktualisiert Remote-Tracking-Refs; er integriert nicht den aktuellen lokalen Branch. Frage: Ist ein Commit schon auf GitHub? Nein.

## 04 · Ändern. Auswählen. Festhalten.

Working Tree: Dateien bearbeiten. Staging Area oder Index: den nächsten Commit bewusst vorbereiten. Repository: Commit dauerhaft in der lokalen History halten. Die Farben sind nur Lernhilfen, die Beschriftungen tragen die Bedeutung. Mit git diff die ungestagten, mit git diff --staged die gestagten Änderungen prüfen. Neu bearbeitete Inhalte müssen nach dem Staging erneut gestagt werden.

## 05 · Der Commit nimmt die Auswahl.

Beispiel: headline.md enthält zuerst Version 1. git add übernimmt Version 1 in den Index. Danach ändern wir im Editor weiter auf Version 2, ohne erneut zu stagen. Der nächste Commit enthält Version 1. Version 2 bleibt als ungestagte Änderung im Working Tree. Frage zuerst, dann zeige mit dem Diagramm die Antwort.

## 06 · Ein Commit hält einen Stand fest.

Ein Commit verweist auf den kompletten versionierten Projektstand, nicht nur auf den angezeigten Diff. Git speichert identische Objekte effizient, das Bild ist also keine Aussage über vollständige physische Kopien pro Commit. Zum Commit gehören Elternverweise und Metadaten. Die Beispiel-ID ist illustrativ.

## 07 · Ein Branch ist ein Namensschild.

Ein Branch ist ein beweglicher Verweis auf einen Commit. Wenn wir einen Branch anlegen, müssen wir nicht das ganze Projekt kopieren. Hier zeigen main und feature auf denselben Commit B. HEAD verweist normalerweise auf den aktuell ausgecheckten Branch, hier feature. Die Linien zwischen Commits zeigen Abstammung; wir zeichnen ältere Stände links.

## 08 · Nur dein Branch bewegt sich.

Vergleiche mit der vorherigen Folie: Ein neuer Commit C wird auf feature erzeugt. main bleibt auf B. HEAD bleibt an feature gebunden und zeigt dadurch indirekt auf C. Ein Commit auf einem Feature-Branch ändert nicht automatisch main. Fragen lassen: Wo steht main jetzt? Wo steht HEAD?

## 09 · So wird aus einer Idee Teamarbeit.

Führe den gesamten Weg einmal vor: Issue beschreibt die Aufgabe, Branch grenzt die Arbeit ab, Commits machen Schritte nachvollziehbar, Push veröffentlicht. Im Pull Request folgen Review und Nachbesserung. Erst nach finalem Review wird integriert. Ein neuer Push auf denselben Branch aktualisiert den vorhandenen PR.

## 10 · Euer erster Pull Request.

Lasse diese Folie während Runde 1 stehen. Ein PR pro Zweierteam. Team 1 bearbeitet index.md, 2 program.md, 3 snacks.md, 4 team.md, 5 status-board.md. Die genaue Mission steht in exercises/01-warmup.md. Nach dem ersten Commit wechselt das Keyboard. Mindestens zwei sinnvolle Commits, PR mit Ziel und Prüfschritten. Noch nicht mergen.

## 11 · Ein PR macht Entscheidungen sichtbar.

Ein hilfreiches Review begründet seine Rückfrage anhand der Wirkung für Nutzer:innen. Zeige die fehlende Ortsangabe und den Kommentar. Die Autor:innen ergänzen den Ort und pushen auf denselben Branch. Der PR aktualisiert sich. Reviewer prüfen den neuen Stand. Comment ist Rückmeldung; Request changes fordert Nachbesserung; Approve gibt den geprüften Stand frei.

## 12 · Jetzt prüft das nächste Team.

Lasse diese Folie während Runde 2 stehen. Review-Ring 1 zu 2, 2 zu 3, 3 zu 4, 4 zu 5, 5 zu 1. Jede Person schreibt mit dem eigenen Konto einen begründeten Beitrag. Pro Team eine konkrete Stärke und eine Frage oder Verbesserung. Entwürfe absenden. Autor:innen übernehmen eine sinnvolle Verbesserung, Reviewer prüfen erneut. Ab Minute 50 nacheinander Create a merge commit verwenden, danach lokalen main aktualisieren.

## 13 · Holen ist noch nicht integrieren.

Die drei Zeilen gehören zu verschiedenen Orten: Server-Branch main, lokale Remote-Tracking-Ref origin/main und lokaler Branch main. Nach Fetch kann origin/main auf C stehen, während lokaler main auf B bleibt. Pull führt zunächst Fetch und dann einen Integrationsversuch aus. Im Workshop pull --ff-only: bei Divergenz bricht der Integrationsschritt ab. Die Folie zeigt den Zustand nach einem erfolgreichen Fetch und vor dem Pull.

## 14 · Gleicher Start. Zwei Entscheidungen.

Ab Minute 55 erzeugt jede Person mit bash scripts/create-labs.sh eigene Labore und öffnet conflict. Das Skript hat zwei Branches vom selben Ausgangspunkt erstellt. Team A verlegt den Lunch in die Mensa und ist bereits im lokalen main. Team B ändert Zeit und Angebot. Beide haben dieselbe Zeile verschieden geändert. Gleiche Datei allein garantiert keinen Konflikt; hier ist der Konflikt gezielt konstruiert.

## 15 · Git stoppt. Ihr entscheidet.

Führt im frischen conflict-Labor auf team-b git merge main aus. Der erwartete Konflikt stoppt die automatische Zusammenführung. Oben steht in diesem Merge HEAD beziehungsweise team-b, unten der eingehende main. Beim Rebase kann die ours/theirs-Zuordnung anders wirken; nicht verallgemeinern. Die Festivalleitung bestätigt Mensa, 12:30 Uhr und vegetarisches Buffet. Die endgültige Zeile noch nicht verraten.

## 16 · Baut die gültige Lunch-Zeile.

Konfliktrunde insgesamt 25 Minuten, inklusive der vorherigen Einführung: fünf Minuten Labore und Graph, fünf Minuten Konflikt lesen, sieben Minuten lösen, acht Minuten erklären beziehungsweise zweiten Durchlauf am gemeinsamen Laptop durchführen. Pro Person ein eigener Durchlauf. Nach Bearbeitung git diff --check, git add program.md, git diff --staged und Merge committen. Erfolg: alle drei Vorgaben erfüllt, keine Marker, sauberer Status und Merge-Commit mit zwei Eltern.

## 17 · Drei Anforderungen. Eine Lösung.

Erst nach dem eigenen Lösungsversuch zeigen. Die gemeinsame Fassung lautet 12:30 Lunch in der Mensa mit vegetarischem Buffet. Das Zusammensetzen ist eine inhaltliche Entscheidung. git add markiert als gelöst, prüft aber keine fachliche Richtigkeit. Im Graph zeigt main weiter auf A, team-b nach dem Merge auf M; M hat A und B als Eltern. Das lokale Beispiel braucht keinen Push.

## 18 · Fast-Forward: Das Schild rückt nach.

Wechsel ins fast-forward-Labor. Zeige vorher und nachher: A ist ein Vorfahr von B. Das Merge muss keinen zusätzlichen Commit erzeugen, sondern kann main auf B setzen. feature/info und main zeigen anschliessend auf denselben bereits vorhandenen Commit. IDs vergleichen. Nicht mit konfliktfrei gleichsetzen: Das ist eine Aussage über die History.

## 19 · Beide Linien sind weitergelaufen.

Im rebase-Labor stehen main und feature auf eigenen Nachfahren derselben Basis. B liegt nicht in der Abstammung von C. Auf main git merge --ff-only feature/volunteers ausführen: erwartete Ablehnung. Es läuft danach kein Merge, daher ist kein merge --abort nötig. Die Branches ändern verschiedene Dateien; die Ablehnung ist kein Dateikonflikt.

## 20 · Rebase: gleiche Änderung, neue Basis.

Auf dem Feature-Branch wird git rebase main ausgeführt. C wird auf B erneut angewendet; es entsteht C′ mit anderem Elterncommit und damit anderer ID. main bleibt auf B. Ein lokaler Rebase kann in anderen Ausgangssituationen ohne Änderungen auskommen; hier ändert sich die Basis bewusst. before-rebase hält im Labor den alten Commit C erreichbar, deshalb zeigt git log --all diesen weiterhin.

## 21 · Jetzt kann main folgen.

Nach dem Rebase wechseln wir auf main und führen git merge --ff-only feature/volunteers aus. main ist nun Vorfahr des Feature-Commits; Fast-Forward gelingt. Rebase und anschliessende Integration sind zwei getrennte Schritte. Frage: Welcher Schritt hat die neue Commit-ID erzeugt? Der Rebase, nicht das Fast-Forward. Nur aktive Branches dargestellt, der Vergleichsbranch before-rebase bleibt im Labor vorhanden.

## 22 · Drei Wege. Drei Geschichten.

Alle drei Skizzen starten gedanklich bei O: main ist bis B gelaufen; der Feature-Zweig hat C und D. Links Merge: M verbindet B und D, beide Linien bleiben sichtbar. Mitte Rebase: C′ und D′ werden auf B neu aufgebaut und danach integriert. Rechts Squash-Integration: ein neuer S fasst den Inhalt des Features auf B zusammen. Gleiche resultierende Dateien sind im konfliktfreien Beispiel möglich, die History unterscheidet sich. GitHub Rebase and merge erzeugt neue IDs und ist nicht identisch mit lokalem --ff-only.

## 23 · Lest die History.

Diese 20 Minuten umfassen die vorherigen kurzen Erklärungen und das eigene Ausführen, keine zusätzlichen 20 Minuten. Die Labore aus Runde 3 sind bereits erstellt. Für Fast-Forward IDs vergleichen; im Rebase-Labor erwartete FF-Ablehnung, Rebase, neue ID und erfolgreiches FF. Squash nur als Bonus mit fünf bis zehn Minuten zusätzlich. Alle Arbeiten sind lokal ohne Remote; kein Force Push erforderlich.

## 24 · Was passiert als Nächstes?

Erst 30 Sekunden still nachdenken, dann im Paar besprechen. Antworten: 1 Nur der gestagte Stand kommt in den Commit; danach bearbeitete ungestagte Änderungen bleiben im Working Tree. 2 Nach Fetch ist origin/main aktualisiert, lokaler main aber noch nicht notwendigerweise integriert. 3 Nein, ein konfliktfreier Merge beweist keine fachliche Richtigkeit. Zusatzfrage: Wann ist FF möglich? Wenn der Zielstand Vorfahr des einzubindenden Commits ist.

## 25 · Erst verstehen. Dann integrieren.

Sammelt drei konkrete Regeln für eure nächste Zusammenarbeit. Lasst die Gruppe formulieren: Status und Branch zuerst lesen; kleine verständliche Änderungen; Reviews begründen und den finalen Stand prüfen. Wer noch keinen eigenen Konflikt gelöst hat, plant genau diesen nächsten Übungsschritt. Verweise auf Glossar, Spickzettel und Drehbuch im Repository. Letzte fünf Minuten sind Puffer.
