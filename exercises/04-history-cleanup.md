# Übung 4: Fast-Forward, Rebase und optional Squash

**20 Minuten.** Verwendet die Labore aus Runde 3. Jedes ist ein eigenes Repository ohne Remote. Den jeweils ausgegebenen `cd`-Befehl verwenden. Alle Schritte starten mit sauberem Working Tree. Labore für Wiederholungen neu erstellen.

## A. Fast-Forward beobachten, 7 Minuten

Im Labor **fast-forward**:

```bash
git switch main
git log --oneline --graph --decorate --all
git rev-parse feature/info
git merge --ff-only feature/info
git rev-parse main
git log --oneline --graph --decorate --all
```

Vorher: `A (main) → B (feature/info)`. Nachher: `A → B (main, feature/info)`.

Die beiden ausgegebenen IDs sind gleich. Es entsteht kein zusätzlicher Commit. Der Zielbranch konnte entlang der vorhandenen History aufrücken, weil sein alter Stand ein Vorfahr des Feature-Branches war. [Git beschreibt dieses Verhalten unter Fast-Forward](https://git-scm.com/docs/git-merge#_fast_forward_merge).

## B. Divergenz, Rebase und danach Fast-Forward, 10 Minuten

Im Labor **rebase**:

```bash
git switch main
git log --oneline --graph --decorate --all
git merge --ff-only feature/volunteers
```

**Der letzte Befehl soll fehlschlagen.** `main` und Feature-Branch haben jeweils eigene neue Commits. Das ist kein Dateikonflikt: Fast-Forward ist aufgrund der History unmöglich. Es läuft kein Merge, also ist auch kein `merge --abort` erforderlich.

```bash
git switch feature/volunteers
git rev-parse HEAD
git rebase main
git rev-parse HEAD
git log --oneline --graph --decorate main feature/volunteers
git diff before-rebase feature/volunteers -- volunteers.md
```

Erwartet: neue Commit-ID, kein Dateikonflikt und beim letzten Befehl kein Diff. Die Volunteer-Änderung bleibt inhaltlich erhalten; die neue Basis enthält zusätzlich die Wetterinformation. `before-rebase` hält den alten Feature-Stand zum Vergleich fest. Deshalb sieht `git log --all` weiterhin auch den alten Seitenzweig.

```text
Vorher:                 Nachher, aktive Branches:
    B (main)            A---B (main)---C' (feature/volunteers)
   /
  A
   \
    C (feature/volunteers)
```

Die Striche zeigen Abstammung, nicht Zeitdauer. Jetzt integrieren:

```bash
git switch main
git merge --ff-only feature/volunteers
git status
```

Erwartet: Fast-Forward gelingt. Rebase hat die Feature-Änderung auf die neue Basis angewendet; das anschliessende Merge bewegt `main`. [Das Git-Buch erklärt diesen Ablauf](https://git-scm.com/book/en/v2/Git-Branching-Rebasing).

**Bei einem Rebase-Konflikt in anderen Aufgaben:** Datei bearbeiten → `git add DATEI` → `git rebase --continue`, gegebenenfalls mehrfach. Mit `git rebase --abort` zum Ausgangspunkt zurück. Nicht stattdessen einen gewöhnlichen Merge-Commit erzeugen. In diesem vorbereiteten Labor ändern die beiden Branches verschiedene Dateien und sollten konfliktfrei bleiben.

## C. Vergleich und Lerncheck, 3 Minuten

- Warum konnte Teil A sofort fast-forwarden und Teil B erst nach Rebase?
- Welcher Schritt erzeugte eine neue Commit-ID?
- Warum braucht dieses Labor keinen Force Push? Es gibt keinen Remote und keine veröffentlichte History.

**GitHub-Falle:** Der PR-Knopf **Rebase and merge** erzeugt auf GitHub neue Commit-IDs; er ist nicht identisch mit dem lokalen `git merge --ff-only`. **Squash and merge** verdichtet PR-Änderungen zu einem Commit auf dem Zielbranch. **Create a merge commit** erhält die Branch-Commits und ergänzt einen Merge-Commit. [GitHub dokumentiert die drei Methoden](https://docs.github.com/en/pull-requests/reference/pull-request-merges).

## D. Drei Commits zu einem machen (Bonus, 5–10 zusätzliche Minuten)

Im Labor **squash**:

```bash
git switch feature/snacks
git log --oneline main..HEAD
git branch before-squash
git rebase -i main
```

Im geöffneten Editor den ersten Eintrag auf `pick` lassen und die beiden folgenden von `pick` auf `squash` ändern. Reihenfolge ist hier vom ältesten zum neuesten Commit. Speichern, schliessen und im nächsten Editor eine gemeinsame Nachricht wie `docs: add snack menu and drinks` setzen.

Vorab einen vertrauten Editor für Git konfigurieren; Beispiele stehen im [Trainer Guide](../docs/trainer-guide.md). Bei Unsicherheit abbrechen und `git rebase --abort` verwenden, falls der Rebase läuft.

```bash
git rev-list --count main..HEAD
git diff before-squash HEAD
git status
```

Erwartet: **1** Commit, leerer Diff und sauberer Working Tree. Die Änderungen sind dieselben, die Commit-Aufteilung wurde neu geschrieben. Squash ist eine mögliche Nutzung des interaktiven Rebase; ein normaler Rebase fasst Commits nicht automatisch zusammen.

## Übertragung in den Alltag

Rebase ist für private Feature-Arbeit praktisch. Bei bereits veröffentlichten Branches zuerst die Zusammenarbeit klären: andere können auf den bisherigen Commits aufbauen. In diesem Workshop werden gemeinsame Branches nicht umgeschrieben. `--force-with-lease` prüft einen erwarteten Remote-Stand; es ersetzt weder Absprache noch Prüfung fremder Commits. [Details stehen in der Git-Push-Dokumentation](https://git-scm.com/docs/git-push#Documentation/git-push.txt---force-with-lease).
