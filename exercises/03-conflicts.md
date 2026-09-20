# Übung 3: Einen echten Konflikt verstehen und lösen

**25 Minuten, jede Person im eigenen lokalen Labor.** Ein Zweierteam darf sich gegenseitig erklären, was es sieht. Bei einem gemeinsamen Laptop nach dem ersten Durchlauf ein frisches Labor erstellen und wechseln.

## 1. Vorbereiteten Ausgangspunkt öffnen, 5 Minuten

Im geklonten Workshop-Repository:

```bash
bash scripts/create-labs.sh
```

Den ausgegebenen `cd`-Befehl für **conflict** ausführen. Den Pfad auch für Runde 4 aufbewahren. Die folgenden Befehle gehören in dieses Labor, nicht in den Workshop-Klon:

```bash
git status
git remote -v
git log --oneline --graph --decorate --all
```

Erwartet: Branch `team-b`, sauberer Working Tree, keine Remotes. Das Skript hat zwei Branches vom gleichen Ausgangscommit vorbereitet. Team A wurde schon in den lokalen `main` übernommen. Beide Branches haben dieselbe Lunch-Zeile unterschiedlich geändert.

## 2. Zusammenführen und bewusst stoppen, 5 Minuten

```bash
git merge main
```

**Erwartet: `CONFLICT` und ein abgebrochener automatischer Merge.** Das ist der Übungsfall. Noch nicht committen. `git status` und `git diff` lesen, dann `program.md` im Editor öffnen:

> ```text
> <<<<<<< HEAD
> - 12:30 Lunch im Innenhof mit vegetarischem Buffet
> =======
> - 12:00 Lunch in der Mensa
> >>>>>>> main
> ```

`HEAD` bezeichnet hier die Version des aktuellen Branches `team-b`; darunter steht die eingehende Version von `main`. Diese Zuordnung gilt für diesen Merge. Bei Rebase können „ours/theirs“ überraschend anders zugeordnet sein; deshalb den Inhalt lesen.

## 3. Fachlich entscheiden und abschliessen, 7 Minuten

Die Festivalleitung bestätigt: Wegen Regen wird in der **Mensa** gegessen, Beginn ist **12:30**, das **vegetarische Buffet** bleibt. Formuliert daraus genau eine gültige Zeile. Das Ergebnis muss alle drei Informationen enthalten. Entfernt die Marker und doppelte Varianten.

```bash
git diff --check
git add program.md
git diff --staged
git commit -m "merge: combine lunch time, venue and buffet"
git status
git log --oneline --graph --decorate --all
```

`git add` markiert den bearbeiteten Konflikt als gelöst. Git prüft dabei nicht, ob eure fachliche Entscheidung korrekt ist. `git diff --check` meldet unter anderem neu eingeführte Konfliktmarker und bestimmte Whitespace-Probleme; die Inhaltsprüfung bleibt nötig.

**Erfolg:** sauberer Working Tree, keine Marker, alle drei Vorgaben erfüllt und ein Merge-Commit mit zwei Eltern. In diesem Labor ist kein Push nötig.

## 4. Erklären, 8 Minuten

Zeigt euch gegenseitig die Lösung. Beantwortet: Was war die gemeinsame Basis? Warum konnte Git die Änderungen nicht selbst entscheiden? Warum wäre „Accept current“ oder „Accept incoming“ allein unvollständig gewesen?

Bei einem geteilten Laptop jetzt im ursprünglichen Workshop-Verzeichnis das Skript nochmals starten und die andere Person lösen lassen. Wer alleine arbeitet, kann in einem frischen Labor `git merge main` und danach `git merge --abort` ausprobieren. Erwartet: wieder der saubere Stand von `team-b` vor dem Merge. Vorher eigene Änderungen committen; ein Abort ist kein allgemeines Backup.

## Transfer: Ein Konflikt im GitHub-PR (optional)

Zusätzliche Runde, etwa 20–30 Minuten; kein Pflichtteil der 120 Minuten:

1. Zwei Teams erhalten dieselbe Zeile und unterschiedliche Änderungen, etwa den `12:00`-Slot in `app/program.md`. Andere Teams reviewen; keine weiteren Personen bearbeiten diese Datei.
2. Beide erstellen neue Branches vom **identischen, aktuellen `origin/main`-Commit**. Hash gemeinsam mit `git rev-parse origin/main` prüfen. Im Fork-Modell `upstream/main` verwenden.
3. Beide Änderungen committen, pushen und PRs öffnen. **Beide PRs müssen bereit sein, bevor der erste merged wird.** Sonst kann die zweite Änderung schon auf der ersten aufbauen und der gewünschte Konflikt ausbleiben.
4. PR A reviewen und mergen. Auf dem Branch von PR B, bei sauberem Working Tree:

   ```bash
   git fetch origin
   git merge origin/main
   ```

5. Konflikt fachlich lösen, Datei stagen, Merge committen und normal pushen. Im PR die Entscheidung dokumentieren, erneut reviewen und dann mergen.

`origin/main` ist die lokale Sicht auf den entfernten Branch nach dem Fetch; ein Wechsel auf den lokalen `main` ist dafür nicht nötig. Bei Forks lauten die beiden Befehle `git fetch upstream` und `git merge upstream/main`.
