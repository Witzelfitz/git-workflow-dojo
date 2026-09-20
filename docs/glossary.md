# Git-Glossar und Antworten für die Moderation

Für den Auftritt zuerst die **Kernbegriffe** lernen. Die Vertiefung ist zum Nachschlagen gedacht. Ein Begriff wirkt souverän, wenn du seine Wirkung an einem konkreten Beispiel erklären kannst.

## Kernbegriffe: lokal arbeiten

| Fachwort | Bedeutung | So kannst du es sagen |
| --- | --- | --- |
| Git | Verteiltes Versionskontrollsystem | „Git verwaltet unsere Projektstände und ihre Geschichte.“ |
| GitHub / GitLab | Plattformen für Hosting und Zusammenarbeit rund um Git | „Git läuft lokal; die Plattform ergänzt unter anderem PRs, Reviews und Rechte.“ |
| Repository / Repo | Git-Datenbestand mit Objekten, Referenzen und Konfiguration; bei einem normalen Klon mit Arbeitsverzeichnis | „Das ist unser versioniertes Projekt.“ |
| Clone | Lokale Kopie eines Repositorys anlegen | „Wir holen uns eine eigene Arbeitskopie mit Git-History.“ |
| Working Tree / Arbeitsverzeichnis | Die ausgecheckten Dateien, die du bearbeitest | „Hier liegen die Dateien, die wir im Editor sehen.“ |
| Staging Area / Index | Für den nächsten Commit vorbereiteter Dateistand | „Hier wählen wir aus, was in den nächsten Commit kommt.“ |
| Stage / `git add` | Aktuellen Dateiinhalt in den Index übernehmen | „Wir bereiten diesen Stand für den Commit vor.“ |
| Commit | Gespeicherter Projektstand samt Metadaten und Verweisen auf Elterncommits | „Ein nachvollziehbarer Schritt in der Projektgeschichte.“ |
| Snapshot | Momentaufnahme eines Dateistands | „Ein Commit verweist auf einen Stand; Git zeigt uns bei Bedarf die Unterschiede.“ |
| Commit-ID / Hash / Object ID | Inhaltsabhängige Kennung eines Commit-Objekts | „Die kurze Zeichenfolge identifiziert diesen Commit; sie ist keine Versionsnummer.“ |
| Commit Message | Beschreibung des Commits | „Sie erklärt, welches Ergebnis dieser Schritt gebracht hat.“ |
| Diff | Vergleich zwischen zwei Ständen | „Hier sehen wir die Änderungen, die wir prüfen wollen.“ |
| Untracked | Datei wird von Git noch nicht versioniert | „Die neue Datei liegt da, gehört aber noch nicht zu einem Commit.“ |
| Modified / Staged | Bearbeitet beziehungsweise für den nächsten Commit vorbereitet | „Bearbeitet heisst noch nicht gestagt.“ |
| Clean Working Tree | Keine von `git status` gemeldeten offenen Änderungen | „Wir haben einen klaren Ausgangspunkt für den nächsten Schritt.“ |

**Merken:** `git diff` zeigt im normalen Zustand ungestagte Änderungen versionierter Dateien, `git diff --staged` die Änderungen im Index gegenüber `HEAD`. Neue untracked Dateien erscheinen erst nach `git add` im gestagten Diff. Die Git-Dokumentation erläutert [Diff-Vergleiche](https://git-scm.com/docs/git-diff) und [Staging](https://git-scm.com/docs/git-add).

## Kernbegriffe: Branches und Zusammenarbeit

| Fachwort | Bedeutung | So kannst du es sagen |
| --- | --- | --- |
| Branch | Benannter, beweglicher Verweis auf die Spitze einer Entwicklungslinie | „Auf diesem Branch entwickeln wir unseren Auftrag weiter.“ |
| Feature-Branch | Branch für eine begrenzte Änderung | „Unser Arbeitszweig für genau diese Aufgabe.“ |
| `main` / Default Branch | Konventioneller Hauptbranch; der Default Branch wird auf der Plattform festgelegt | „Unser gemeinsam integrierter Stand.“ |
| `HEAD` | Verweis auf den aktuell ausgecheckten Stand, normalerweise über den aktuellen Branch | „HEAD zeigt, wo wir gerade arbeiten.“ |
| Switch / Checkout | Branch beziehungsweise Stand auschecken | „Wir wechseln unseren Arbeitsstand.“ `switch` ist auf Branchwechsel ausgerichtet. |
| Remote | Benannte Verbindung zu einem anderen Repository | „Hierhin können wir Daten übertragen oder von dort holen.“ |
| `origin` | Üblicher Name des beim Klonen angelegten Remotes | „Ein frei wählbarer Name, keine magische GitHub-Adresse.“ |
| Remote-Tracking Branch | Lokaler Verweis auf den zuletzt geholten Stand eines entfernten Branches, etwa `origin/main` | „Unsere zuletzt aktualisierte Sicht auf den Server-Branch.“ |
| Fetch | Objekte holen und die entsprechenden Remote-Tracking-Refs aktualisieren | „Wir holen Informationen, ohne den aktuellen Arbeitsbranch zu integrieren.“ |
| Pull | Fetch mit anschliessendem Integrationsversuch in den aktuellen Branch | „Wir holen und integrieren; wie, hängt von Optionen und Konfiguration ab.“ |
| Push | Git-Objekte übertragen und entfernte Referenzen aktualisieren | „Jetzt wird unser Branch-Stand auf dem Server verfügbar.“ |
| Upstream / Tracking Branch | Zugeordneter Gegenpart eines lokalen Branches | „Mit `push -u` richten wir ein, welchen Remote-Branch unser Branch verfolgt.“ |
| Fork | Eigenes Repository auf der Hosting-Plattform, abgeleitet von einem anderen | „Ein eigenes Server-Repo, aus dem wir Änderungen zurück vorschlagen können.“ |
| Issue | Beschriebene Aufgabe, Frage oder Fehler auf der Plattform | „Hier halten wir Ziel und Abnahme fest.“ |
| Pull Request / PR | Vorschlag, Änderungen eines Branches in einen Zielbranch zu integrieren, mit Diskussion und Review | „Unser gemeinsamer Prüf- und Entscheidungsraum.“ |
| Merge Request / MR | GitLab-Bezeichnung für diesen Integrationsvorschlag | „Bei GitHub sagen wir PR, bei GitLab MR.“ |
| Base / Target Branch | Zielbranch des PR | „Dorthin soll die Änderung.“ |
| Head / Source / Compare Branch | Branch, dessen Änderungen vorgeschlagen werden | „Daher kommt die Änderung.“ |

**Zwei Bedeutungen von upstream:** Der Tracking Branch ist Git-Konfiguration. Ein Remote namens `upstream` ist dagegen eine frei gewählte Benennung, im Fork-Modell oft für das zentrale Repository. `origin/main`, lokaler `main` und Server-Branch `main` können unterschiedliche Stände haben. Siehe [Remote-Branches im Git-Buch](https://git-scm.com/book/en/v2/Git-Branching-Remote-Branches) und [Git Pull](https://git-scm.com/docs/git-pull).

## Kernbegriffe: Review und Integration

| Fachwort | Bedeutung | So kannst du es sagen |
| --- | --- | --- |
| Code Review | Prüfung einer Änderung durch andere Personen; gilt auch für Texte und Konfiguration | „Wir prüfen Verständlichkeit, Richtigkeit und Auswirkungen.“ |
| Comment | Review-Rückmeldung ohne formelle Freigabe oder Änderungsanforderung | „Ich habe eine Frage oder einen Hinweis.“ |
| Request changes | Formelle Anforderung einer Nachbesserung; Wirkung hängt von Rechten und Regeln ab | „Dieser Punkt muss vor meiner Freigabe geklärt sein.“ |
| Approve | Formelle Zustimmung zu einem geprüften PR-Stand | „Ich gebe diesen Stand aus meiner Review-Sicht frei.“ |
| Resolve conversation | Review-Diskussion als geklärt markieren | „Der Thread ist erledigt; das ist nicht automatisch ein Approve.“ |
| Merge | Entwicklungslinien integrieren | „Wir führen die Stände zusammen.“ |
| Merge-Commit | Commit mit mehreren Eltern; im üblichen Zwei-Branch-Merge genau zwei | „Dieser Commit verbindet die beiden Entwicklungslinien.“ |
| Fast-Forward | Branch-Verweis auf einen bereits vorhandenen Nachfahren vorziehen | „Die Geschichte ist bereits eine Linie; der Zielbranch kann nachrücken.“ |
| Divergence / divergiert | Zwei Branches besitzen seit einer gemeinsamen Basis jeweils eigene Commits | „Beide Linien sind unabhängig weitergelaufen.“ |
| Merge Base / gemeinsamer Vorfahr | Gemeinsame Ausgangsbasis für den Vergleich | „Von welchem gemeinsamen Stand aus haben sich die Branches verändert?“ |
| Three-Way Merge | Zusammenführung anhand beider Branch-Stände und ihrer gemeinsamen Basis | „Git vergleicht beide Änderungen mit dem Ausgangspunkt.“ |
| Merge Conflict | Git kann Änderungen nicht automatisch eindeutig zusammenführen | „Hier müssen wir die gültige Endfassung entscheiden.“ |
| Conflict Markers | Markierungen wie `<<<<<<<`, `=======`, `>>>>>>>` im Textkonflikt | „Sie grenzen die widersprechenden Varianten ab.“ |
| Conflict Resolution | Konflikt inhaltlich lösen, Lösung stagen und Operation abschliessen | „Wir entscheiden, prüfen und setzen den Git-Vorgang fort.“ |
| Rebase | Änderungen einer Commit-Reihe auf eine andere Basis erneut anwenden | „Wir bauen unsere Entwicklungslinie auf einem neueren Ausgangspunkt auf.“ |
| Interactive Rebase | Rebase mit bearbeitbarer Aktionsliste | „Wir können lokale Commits ordnen, umformulieren oder zusammenfassen.“ |
| Squash | Mehrere Änderungen/Commits zu einem Commit verdichten | „Wir behalten das Ergebnis und ändern die Granularität der History.“ |
| Rewrite History | Neue Commits erzeugen und Referenzen auf die neue History bewegen | „Andere können noch auf den alten Commit-IDs aufbauen; deshalb stimmen wir das ab.“ |

Die offiziellen Referenzen behandeln [Review-Zustände](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/about-pull-request-reviews), [Branching und Merging](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging) sowie [interaktiven Rebase](https://git-scm.com/docs/git-rebase#_interactive_mode).

## Merge, Rebase und Squash im Vergleich

| Methode | Wirkung in unserem Beispiel | Typischer Zweck |
| --- | --- | --- |
| `git merge --ff-only feature` | Zielbranch rückt auf vorhandenen Commit; bei divergierter History Abbruch | Lineares Integrieren ohne neuen Merge-Commit |
| Merge divergierter Branches | Zusätzlicher Commit mit zwei Eltern | Entwicklungslinien und Integration sichtbar erhalten |
| `git rebase main` auf Feature | Feature-Änderungen auf aktueller Basis, hier mit neuen Commit-IDs | Eigene lokale Arbeit vor Integration aktualisieren |
| Interaktiver Rebase mit Squash | Mehrere lokale Commits werden ein neuer Commit | Zusammengehörende Zwischenschritte verdichten |
| GitHub „Create a merge commit“ | Zusätzlicher Merge-Commit im Zielbranch | PR-Integration im Graph nachvollziehen |
| GitHub „Squash and merge“ | Ein neuer zusammengefasster Commit im Zielbranch | Ein integrierter Schritt pro PR |
| GitHub „Rebase and merge“ | Neue Commits im Zielbranch, kein zusätzlicher Merge-Commit | Lineare Integration einzelner PR-Commits |

GitHub verändert bei „Rebase and merge“ die Commit-IDs auch in Situationen, in denen ein lokaler Rebase ohne Änderung auskommen könnte. Daher den Plattformknopf nicht mit lokalem Fast-Forward gleichsetzen. [GitHub: Pull Request Merges](https://docs.github.com/en/pull-requests/reference/pull-request-merges).

## Vertiefung: Begriffe für Rückfragen

| Fachwort | Kurze Erklärung |
| --- | --- |
| Branch Protection / Ruleset | Plattformregeln für Änderungen an bestimmten Branches oder Referenzen, etwa erforderliche Reviews. |
| Status Check / CI | Automatisierte Prüfung einer Änderung. Continuous Integration führt typischerweise Build, Tests oder andere Checks aus. Dieses Repo hat derzeit keine CI. |
| Force Push | Aktualisierung eines Remote-Branches, die dessen bisherige History ersetzen kann. |
| `--force-with-lease` | Erlaubt eine erzwungene Aktualisierung nur beim erwarteten Remote-Stand. Ohne explizite Erwartung hängt diese Prüfung meist am Remote-Tracking-Stand; Hintergrund-Fetches können die Schutzwirkung abschwächen. |
| `--ff-only` | Nur Fast-Forward erlauben; bei nötiger echter Zusammenführung abbrechen. |
| `--no-ff` | Bei einem Merge nach Möglichkeit einen Merge-Commit auch dann anlegen, wenn Fast-Forward möglich wäre. Bereits vollständig integrierte History erzeugt dadurch keinen zusätzlichen Merge. |
| Ours / Theirs | Relative Bezeichnungen der am Merge beteiligten Seiten. Bei Rebase steht „ours“ für die bereits aufgebaute Zielseite; „theirs“ für den gerade angewendeten ursprünglichen Commit. Inhalt und Kontext prüfen. |
| Revert | Einen neuen Commit erzeugen, der die Wirkung einer früheren Änderung rückgängig macht. |
| Reset | Je nach Aufruf Referenz, Index und/oder Working Tree auf einen anderen Stand setzen; `--hard` kann lokale Arbeit verwerfen. |
| Restore | Dateiinhalte im Working Tree oder Index wiederherstellen; kann uncommittete Änderungen überschreiben. |
| Stash | Uncommittete Änderungen vorübergehend weglegen; untracked Dateien nur mit entsprechender Option. Kein Ersatz für langfristige Sicherung. |
| Reflog | Lokales Protokoll von Referenzbewegungen; kann beim Wiederfinden früherer Commit-Stände helfen, wird nicht gepusht. |
| Detached HEAD | `HEAD` zeigt direkt auf einen Commit statt auf einen Branch. Neue Arbeit durch einen Branch benennen, wenn sie erhalten bleiben soll. |
| Cherry-pick | Änderung eines ausgewählten Commits auf den aktuellen Branch anwenden, normalerweise als neuer Commit. |
| Tag | Benannte Markierung eines Standes, häufig für Releases. Bewegt sich beim Committen nicht wie ein Branch mit. |
| Amend | Letzten Commit durch einen neuen, überarbeiteten Commit ersetzen. Auch das schreibt History um. |
| Parent Commit / Elterncommit | Direkter Vorgänger, auf den ein Commit verweist; Merge-Commits haben mehrere Eltern. |
| Ref / Referenz | Benannter Verweis auf ein Git-Objekt, etwa ein Branch oder Tag. |
| DAG / Commit-Graph | Gerichteter azyklischer Graph: Commits verweisen auf ihre Eltern, ohne geschlossene Schleifen zu bilden. Im Workshop zeichnen wir die Abstammung von links nach rechts. |
| `.gitignore` | Muster für absichtlich unversionierte Dateien; bereits versionierte Dateien werden dadurch nicht automatisch untracked. |
| Driver / Navigator | Person am Keyboard beziehungsweise aktiv mitdenkende Partnerperson. Navigator ist nicht dasselbe wie formeller PR-Reviewer. |
| Timebox | Festes Zeitfenster mit klarem Zwischenziel. |
| Definition of Done / Abnahmekriterien | Prüfkriterien dafür, wann eine Aufgabe abgeschlossen ist. |
| Conventional Commits | Konvention für Nachrichten wie `docs: …` oder `fix: …`; Git selbst verlangt diese Präfixe nicht. |

Für Details: [Git Push und Lease](https://git-scm.com/docs/git-push), [Git Reset](https://git-scm.com/docs/git-reset), [Git Revert](https://git-scm.com/docs/git-revert), [Git Reflog](https://git-scm.com/docs/git-reflog), [Gitignore](https://git-scm.com/docs/gitignore) und [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/).

## Acht typische Fragen – sprechfertige Antworten

**„Ist Rebase besser als Merge?“**

„Rebase kann eigene lokale Arbeit übersichtlich auf eine neue Basis setzen. Ein Merge-Commit hält die Verbindung zweier Entwicklungslinien sichtbar fest. Wir wählen passend zur Zusammenarbeit und zur gewünschten Nachvollziehbarkeit.“

**„Verändert ein Rebase immer jede Commit-ID?“**

„Wenn er Commits auf einer neuen Basis neu erzeugt, ändern sich deren IDs. Ist der Branch schon passend aufgebaut, kann ein lokaler Rebase auch nichts ändern. In unserem Labor ändert sich die Basis bewusst.“

**„Warum heisst es Pull Request, obwohl ich pushe?“**

„Der Push veröffentlicht meinen Branch. Mit dem Pull Request bitte ich das Zielprojekt, meine Änderungen zu übernehmen. Das ist kein automatischer Aufruf von `git pull`.“

**„Wenn beide dieselbe Datei ändern, gibt es immer einen Konflikt?“**

„Nein. Viele unabhängige Textänderungen kann Git zusammenführen. Unser Labor ändert absichtlich dieselbe Zeile unterschiedlich von derselben Basis aus.“

**„Ist ein konfliktfreier Merge automatisch richtig?“**

„Nein. Zwei Änderungen können sich fachlich widersprechen, auch wenn sie verschiedene Zeilen betreffen. Darum prüfen wir das Ergebnis.“

**„Kann ich einfach Accept Both klicken?“**

„Nur wenn beide Inhalte zusammen fachlich korrekt sind. Bei zwei Lunch-Zeilen brauchen wir eine gemeinsame gültige Fassung. Ein Editor-Knopf trifft diese Entscheidung nicht für uns.“

**„Braucht Rebase immer einen Force Push?“**

„Nein. Im lokalen Labor überhaupt keinen Push. Wenn ein bereits veröffentlichter Branch durch Rebase anders aufgebaut wurde, kann die Server-Aktualisierung einen abgestimmten Force Push erfordern. Im gemeinsamen Workshop arbeiten wir ohne diese History-Umschreibung.“

**„Verliere ich beim Löschen eines Branches die Commits?“**

„Das Löschen entfernt den Branchnamen. Commits, die weiterhin über andere Branches oder Tags erreichbar sind, bleiben erreichbar. Auf Reflogs als dauerhafte Sicherung sollte man sich nicht verlassen.“

## Formulierungen, die fachlich präzise bleiben

| Ungenaue Aussage | Besser |
| --- | --- |
| „Ich speichere auf GitHub.“ | „Ich committe lokal und pushe danach.“ |
| „Pull lädt nur herunter.“ | „Pull holt und versucht zu integrieren; Fetch holt zunächst nur.“ |
| „Rebase verschiebt einfach dieselben Commits.“ | „Rebase wendet die Änderungen auf einer neuen Basis an und erzeugt dabei hier neue Commits.“ |
| „Fast-Forward heisst ohne Konflikt.“ | „Fast-Forward beschreibt die Beziehung in der History.“ |
| „Ein schöner Graph beweist gute Qualität.“ | „Der Graph zeigt die Entwicklung; Qualität prüfen wir zusätzlich.“ |
| „Force-with-lease ist immer sicher.“ | „Die Lease prüft eine Erwartung an den Remote-Stand; Zusammenarbeit müssen wir trotzdem abstimmen.“ |

Weitere Definitionen finden sich im [offiziellen Git-Glossar](https://git-scm.com/docs/gitglossary). Für den Workshop reichen die Kernbegriffe; Fachwörter jeweils erst am Beispiel einführen.
