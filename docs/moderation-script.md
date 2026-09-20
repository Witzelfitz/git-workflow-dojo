# Moderationsdrehbuch: Git Workflow Dojo

**Rahmen:** zehn Personen, fünf Zweierteams, 120 Minuten; Setup vorab. Zitate sind sprechbare Vorschläge, keine auswendig zu lernende Rede. Die Uhrzeiten sind Minuten seit Beginn. [Spickzettel](cheat-sheet.md) daneben öffnen, [Glossar](glossary.md) als Nachschlagewerk bereithalten.

## Vor Einlass: T−15 bis T0

Workshop-Repo und Teamliste projizieren. Browser-Tabs: README, Issues, Pull Requests. Im Terminal Workshop-Klon öffnen; `git status` und `git remote -v` prüfen. Ein eigenes frisches Labor mit `bash scripts/create-labs.sh` erstellen und die vier Pfade notieren. Dieses Labor für Vorführungen verwenden; Teilnehmende erzeugen ihre eigenen. Keine Live-Demo auf dem gemeinsamen `main`.

Auf dem Flipchart fünf Teams und den Ring **1 → 2 → 3 → 4 → 5 → 1** notieren. Daneben drei Spalten: **PR offen / Review erledigt / Konflikt erklärt**. So siehst du Fortschritt, ohne ständig zu unterbrechen.

## 00–05 · Begrüssung und Ziel

**Sagen:**

> „Wir betreiben heute gemeinsam die Infoseiten eines Campus-Festivals. Inhaltlich sind die Änderungen klein. Unser eigentliches Produkt ist ein nachvollziehbarer Weg von einer Idee bis zu einer geprüften Änderung im gemeinsamen Stand.“
>
> „Ihr arbeitet zuerst zu zweit: eine Person tippt, eine denkt mit. Nach dem ersten Commit tauscht ihr. Später löst jede Person selbst einen Konflikt. Am Ende sollt ihr erklären können, was Git gerade tut und warum ihr den nächsten Befehl ausführt.“

**Zeigen:** Die fünf Dateien unter `app/`, Teamzuordnung und Ablauf. GitHub-Runden und lokale Labore unterscheiden.

**Rahmen setzen:**

> „Auf dem gemeinsamen Repository arbeiten wir über Branch und Pull Request. Gemergt wird nach dem Review. In den lokalen Laboren dürfen wir experimentieren; sie haben keine Verbindung zum Server.“

## 05–12 · Ein verständliches Git-Modell

**Zeigen:** Aufzeichnen: `Working Tree → git add → Staging Area → git commit → lokales Repository → git push → Remote`.

**Sagen:**

> „Im Working Tree bearbeite ich Dateien. Mit `git add` wähle ich den Stand für den nächsten Commit. Mit `git commit` halte ich ihn lokal fest. Erst mit `git push` übertrage ich Commits und aktualisiere den Branch auf dem Server.“
>
> „Ein Branch ist ein beweglicher Verweis auf einen Commit. Er macht eine Entwicklungslinie benennbar. Ein Pull Request ergänzt die Zusammenarbeit: Was soll in welchen Zielbranch, warum, und wer hat es geprüft?“

**Frage ins Plenum:** „Ich habe committed und gehe offline. Ist die Änderung schon auf GitHub?“

**Erwartete Antwort:** „Nein, dafür braucht es einen Push.“ Bei „Ja“ die Grenze zwischen lokalem Repository und Remote nochmals zeigen.

**Zweite Frage:** „Was kommt in den Commit, wenn ich nach `git add` nochmals dieselbe Datei bearbeite?“

**Antwort:** „Der gestagte Stand. Weitere Änderungen müssen erneut gestagt werden.“ Optional `git diff` und `git diff --staged` an einem kleinen lokalen Beispiel zeigen.

## 12–15 · Startbereitschaft

Alle zeigen `git status` und den richtigen Remote. GitHub-Anmeldung kurz prüfen. Ein Team mit Setup-Problemen an einem funktionierenden Laptop starten lassen und später individuelle Praxis nachholen.

**Sagen:**

> „Vor jedem grösseren Schritt lesen wir zuerst den Status. Der beantwortet: Wo bin ich, was ist verändert und läuft bereits eine Operation?“

**Checkpoint:** Fünf Teams kennen Datei und Issue. Keine längere Installation im Plenum; bei mehreren Ausfällen Zeitplan offen anpassen.

## 15–25 · Erste Änderung und erster Commit

[Übung 1](../exercises/01-warmup.md) öffnen. Team 1 als Befehlsmuster zeigen, andere Teams passen Namen und Datei an.

**Sagen:**

> „Holt den aktuellen `main`, erstellt euren Feature-Branch und setzt den ersten Teil eures Auftrags um. Prüft den Diff vor dem Stagen und den gestagten Diff vor dem Commit. Die Nachricht soll später erklären, welches Ergebnis dieser Schritt gebracht hat.“

**Während du herumgehst:** „Auf welchem Branch seid ihr? Welche Dateien kommen in diesen Commit? Warum ist das ein sinnvoller einzelner Schritt?“

**Bei zu grossem Diff:** Umfang gemeinsam verkleinern. **Bei künstlichen Mini-Commits:** Zwei fachliche Teilschritte suchen, etwa Headline und Handlungsaufforderung.

## 25–35 · Rollenwechsel und PR

**Ansagen:** „Jetzt wechselt das Keyboard. Die zweite Person setzt die nächste Teiländerung um, committed und pusht.“

**Sagen:**

> „Eure PR-Beschreibung richtet sich an jemanden, der nicht neben euch sass. Beschreibt Ziel, Änderung und Prüfung. Der Diff zeigt das Was; die Beschreibung erklärt vor allem das Warum.“

**Zeigen:** Base `main`, Compare Feature-Branch, ausgefüllte Vorlage, Issue-Bezug. Den Merge-Knopf noch nicht betätigen.

**Checkpoint bei Minute 35:** Fünf offene PRs. Falls nötig auf einen guten Commit reduzieren, Rollenwechsel und PR-Kontext erhalten.

## 35–43 · Review geben

Den Review-Ring zeigen. Jede Person verwendet ihr eigenes Konto.

**Sagen:**

> „Lest zuerst den Auftrag und dann den Diff. Nennt eine konkrete Stärke und eine Frage oder Verbesserung mit Begründung. Ein hilfreiches Review erklärt die Auswirkung auf jemanden, der diese Seite nutzt.“

**Beispiel vorlesen:** „Beim neuen Programmpunkt fehlt der Ort. Könnt ihr ihn ergänzen, damit Besucher:innen nicht nachfragen müssen?“

**Drei Review-Zustände erklären:** Comment = Rückmeldung; Request changes = begründeter Änderungsbedarf vor dem Merge; Approve = aktuellen Stand freigeben. Niemand soll einen Mangel erfinden, nur um einen Knopf auszuprobieren.

**Erinnern:** Ausstehende Reviews absenden. „Ein Kommentar im Entwurf ist für das andere Team noch keine Rückmeldung.“

**Checkpoint:** Zehn Personen haben einen sichtbaren Review-Beitrag.

## 43–55 · Nachbessern und integrieren

**Sagen:**

> „Antwortet auf das Feedback und übernehmt eine sinnvolle Verbesserung. Bleibt auf demselben Branch. Ein neuer Push aktualisiert euren bestehenden PR. Danach schaut das andere Team nochmals auf den geänderten Stand.“

Bei Uneinigkeit nach Ziel und Wirkung fragen. Kommentar beantworten, Entscheidung begründen; keine endlose Geschmacksdiskussion.

Ab Minute 50 die geprüften PRs nacheinander mit **Create a merge commit** integrieren lassen. Keine formellen Change Requests offen lassen. Danach lokalen `main` aktualisieren.

**Frage:** „Wer sagt uns, ob der Inhalt richtig ist: der grüne Merge-Knopf oder unser Review?“

**Antwort:** „Das Review und die fachliche Prüfung. Automatisches Zusammenführen bestätigt keine inhaltliche Richtigkeit.“

## 55–60 · Konfliktlabor starten

[Übung 3](../exercises/03-conflicts.md) öffnen; alle erzeugen ihre eigenen Labore und wechseln nach `conflict`.

**Sagen:**

> „Zwei Branches haben denselben Ausgangspunkt. Einer verlegt den Lunch nach drinnen, der andere ändert Zeit und Angebot. Der erste Stand ist bereits in `main`. Jetzt integrieren wir ihn in den zweiten Branch.“

**Zeigen:** `git status`, leeres `git remote -v`, `git log --oneline --graph --decorate --all`. Im Graph gemeinsame Basis und beide Enden benennen lassen.

## 60–72 · Konflikt lösen

Alle führen `git merge main` aus.

**Beim erwarteten Stopp ruhig sagen:**

> „Genau dieser Stopp ist geplant. Git kann die beiden Textänderungen nicht eindeutig zusammenführen. Unsere Arbeit ist noch da. Jetzt müssen wir die fachlich richtige Endfassung entscheiden.“

Die Marker erklären: oben aktueller Branch, unten eingehender `main` in diesem Merge. **Nicht sofort die fertige Zeile zeigen.**

**Fachliche Vorgabe vorlesen:** „Die Leitung bestätigt: Mensa, 12:30 Uhr, vegetarisches Buffet.“

**Fragen:** „Welche Information steckt in welcher Variante? Was würde verloren gehen, wenn wir einfach eine Seite übernehmen?“

Bearbeiten lassen; dann `git diff --check`, `git add program.md`, `git diff --staged`, Commit und Graph prüfen.

**Falls jemand nur Marker löscht:** „Lies mir die Information für die Gäste vor. Erfüllt sie alle drei Vorgaben?“

**Trainerlösung, erst nach eigenem Versuch zeigen:** `- 12:30 Lunch in der Mensa mit vegetarischem Buffet`.

## 72–80 · Erklärung und zweiter Versuch

Partner:innen erklären einander Ursache und Entscheidung. Bei geteiltem Laptop ein frisches Labor starten und Person wechseln. Schnellere Personen probieren in einem frischen Labor `git merge --abort` nach einem ausgelösten Konflikt.

**Sagen:**

> „Ein Konflikt ist eine technische Stelle, an der wir eine inhaltliche Entscheidung treffen. Dieselbe Datei zu bearbeiten führt nicht automatisch zu einem Konflikt. Umgekehrt kann Git problemlos mergen und trotzdem ein fachlich falsches Ergebnis erzeugen.“

**Checkpoint:** Jede Person zeigt die gültige Lunch-Zeile und einen sauberen Status. Der Merge-Commit hat zwei Eltern.

## 80–87 · Fast-Forward sichtbar machen

Ins Labor `fast-forward` wechseln und [Übung 4A](../exercises/04-history-cleanup.md#a-fast-forward-beobachten-7-minuten) ausführen.

**Vor dem Befehl fragen:** „Ist `main` in der Geschichte dieses Feature-Branches bereits enthalten?“

**Nach dem Befehl sagen:**

> „Hier musste Git keinen neuen Commit herstellen. Es konnte den Verweis von `main` auf einen bereits vorhandenen Nachfahren setzen. Das nennt man Fast-Forward.“

IDs vergleichen. **Präzise bleiben:** konfliktfrei und fast-forward-fähig sind unterschiedliche Eigenschaften.

## 87–97 · Rebase erklären, dann ausführen

Ins Labor `rebase` wechseln. Den Versuch mit `git merge --ff-only feature/volunteers` auf `main` bewusst scheitern lassen.

**Sagen:**

> „Beide Branches sind seit dem gemeinsamen Ausgangspunkt weitergelaufen. Deshalb kann der Zielbranch nicht einfach entlang einer einzigen Linie aufrücken. Es liegt trotzdem kein Dateikonflikt vor.“

Auf `feature/volunteers` wechseln, ID merken, `git rebase main`, neue ID zeigen.

> „Beim Rebase wenden wir unsere Feature-Änderung auf der neuen Basis erneut an. Der neue Commit hat einen anderen Elterncommit und damit eine andere ID. Danach können wir `main` per Fast-Forward nachziehen.“

**Frage:** „Hat der Rebase schon `main` bewegt?“ **Antwort:** „Nein, wir haben den Feature-Branch neu aufgebaut. `main` folgt erst beim anschliessenden Merge.“

Den zweiten Fast-Forward durchführen. Auf die Zusatzdatei `weather.md` hinweisen und die unveränderte Volunteer-Änderung prüfen. `before-rebase` erklärt den alten Seitenzweig bei `--all`.

## 97–100 · Methoden einordnen

**Sagen:**

> „Ein Merge-Commit verbindet Entwicklungslinien und erhält ihre Commits. Rebase verändert die Basis unserer Entwicklungslinie und erzeugt dabei hier neue Commits. Squash fasst mehrere Schritte zu einem zusammen. Welche Darstellung passt, entscheidet das Team anhand seiner Zusammenarbeit und der benötigten Nachvollziehbarkeit.“

GitHub-Knöpfe kurz mit dem [Vergleich](glossary.md#merge-rebase-und-squash-im-vergleich) abgleichen. Squash-Labor nur mit zusätzlicher Zeit; bei normalen 120 Minuten als Anschlussaufgabe ankündigen.

## 100–110 · Lernkontrolle

Jede Person denkt zunächst 30 Sekunden selbst nach; dann Zweieraustausch, anschliessend drei bis vier Antworten im Plenum. Lösungen zuerst verdeckt halten:

| Frage | Erwartete Antwort |
| --- | --- |
| Was macht `fetch`, was macht `pull` zusätzlich? | Fetch holt Objekte und aktualisiert Remote-Tracking-Refs. Pull versucht zusätzlich, den geholten Stand in den aktuellen Branch zu integrieren. |
| Git zeigt keinen Konflikt. Ist die Änderung korrekt? | Das ist noch nicht bewiesen; Inhalt und Verhalten müssen geprüft werden. |
| Wann ist Fast-Forward möglich? | Wenn der aktuelle Zielstand ein Vorfahr des einzubindenden Commits ist. |
| Warum ändert Rebase hier die ID? | Der neu erzeugte Commit hat eine andere Basis beziehungsweise einen anderen Elterncommit. |
| Wie beendest du einen gelösten Rebase-Konflikt? | Stagen, dann `git rebase --continue`, gegebenenfalls wiederholen. |
| Kann ich einen gemeinsam genutzten Branch einfach rebasen? | Erst abstimmen; andere Arbeit kann auf den bisherigen Commits beruhen. |

## 110–115 · Transfer vereinbaren

**Frage:** „Welche drei Regeln würden unsere nächste echte Zusammenarbeit konkret verbessern?“

Bei Bedarf vorschlagen: kleine nachvollziehbare Änderungen; PRs erklären Ziel und Prüfung; Reviews begründen Rückfragen und Freigaben. Das Team formuliert die endgültigen Regeln selbst.

**Abschlusssatz:**

> „Euer wichtigstes Werkzeug ist nicht ein einzelner Git-Befehl. Es ist die Fähigkeit, den aktuellen Zustand zu lesen und die nächste Änderung bewusst zu wählen. Wenn ihr unsicher seid: Repository prüfen, Branch prüfen, Status lesen, dann handeln.“

## 115–120 · Puffer und Anschluss

Offene Fragen einsammeln. Links zu [Glossar](glossary.md), [Spickzettel](cheat-sheet.md) und Bonuslabor teilen. Wer noch keinen eigenen Konflikt gelöst hat, erhält genau diesen nächsten Schritt; fehlende Praxis nicht als erreicht abhaken.

## Wenn du ins Stocken gerätst

- **Befehl geht schief:** „Lasst uns erst den Status lesen. Welche Operation läuft, und was erwartet Git jetzt?“
- **Du weisst ein Detail nicht:** „Für unseren Fall ist die Wirkung klar. Das Detail prüfe ich in der offiziellen Referenz, bevor ich es als allgemeine Regel behaupte.“
- **Diskussion wird zu theoretisch:** „Welche konkrete Änderung würde das in unserem Branchgraphen bewirken? Zeigen wir es im Labor.“
- **Gruppe hängt zurück:** Squash streichen, Rebase gemeinsam vorführen; Konfliktpraxis und kurze Reflexion sichern.
- **GitHub fällt aus:** Lokale Labore vorziehen; PR-Teil als offenen Folgetermin benennen.
