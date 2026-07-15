# Workshop Flow

## Phase 1: Warmup

Ziel: erste saubere Branch- und PR-Routine.

1. Jede Gruppe zieht sich ein Ticket aus `exercises/01-warmup.md`.
2. Branch-Namensschema:
   - `team-1/hero-copy`
   - `team-2/program-update`
3. Pro Gruppe mindestens 2 Commits:
   - ein inhaltlicher Commit
   - ein kleiner Verbesserungs-Commit
4. PR auf `main` eroeffnen

Lernziel:

- `git switch -c`
- `git add`
- `git commit`
- `git push -u origin ...`
- PR sauber beschreiben

## Phase 2: Review

Ziel: PRs nicht nur "durchwinken", sondern lesen und kommentieren.

1. Jede Gruppe reviewt den PR einer anderen Gruppe.
2. Mindestens 2 Review-Kommentare:
   - 1 Lob oder positive Beobachtung
   - 1 konkrete Aenderung oder Rueckfrage
3. Autor:innen bessern nach und pushen erneut.

Lernziel:

- Review-Kultur
- kleine Nachbesserungen auf demselben Branch
- Force Push vermeiden, solange nicht noetig

## Phase 3: Konflikte

Ziel: nicht ausweichen, sondern den Konflikt bewusst loesen.

1. Die Trainerperson weist zwei Teams dieselbe Datei aus [exercises/03-conflicts.md](../exercises/03-conflicts.md) zu.
2. Team A merged zuerst.
3. Team B aktualisiert den eigenen Branch und loest den Konflikt lokal.
4. Danach neuer Push und Merge.

Lernziel:

- `git fetch`
- `git rebase origin/main` oder `git merge origin/main`
- Konfliktmarker verstehen
- Entscheidung begruenden

## Phase 4: History Cleanup

Ziel: Unterschied zwischen sauberer lokaler History und chaotischer Verlaufskette verstehen.

1. Jede Gruppe erstellt absichtlich 3 bis 4 Mini-Commits.
2. Danach:
   - entweder interaktiver Rebase zum Squashen
   - oder Vergleich mit Merge-Commit-Variante
3. Im Plenum kurz anschauen, wie die History aussieht.

Lernziel:

- wann Rebase sinnvoll ist
- wann ein Merge-Commit ok ist
- was Fast-Forward bedeutet

## Phase 5: Debrief

Fragen:

- Wo sind Konflikte wirklich entstanden?
- Was hat Reviews besser gemacht?
- Welche Branch-Regeln wollt ihr kuenftig fix verwenden?
- Wann ist Rebase hilfreich und wann verwirrt es eher?
