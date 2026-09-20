# Teams und Rollen

| Team | Auftrag | Datei | Issue im ursprünglichen Repo | Reviewt |
| --- | --- | --- | --- | --- |
| 1 | Einstieg und Helfer-Aufruf | `app/index.md` | #3 | Team 2 |
| 2 | Tagesprogramm | `app/program.md` | #5 | Team 3 |
| 3 | Snack-Menü | `app/snacks.md` | #4 | Team 4 |
| 4 | Orga-Kontakte | `app/team.md` | #1 | Team 5 |
| 5 | Status-Board | `app/status-board.md` | #2 | Team 1 |

In einer neuen Workshop-Kopie Issues neu anlegen; Nummern können abweichen. Die Aufgaben in [Übung 1](../exercises/01-warmup.md) sind massgeblich.

## Im Zweierteam

- **Driver:** bedient Terminal und Editor und erklärt vor jedem Befehl das Ziel.
- **Navigator:** liest Diff und Auftrag, prüft den nächsten Schritt und stellt Rückfragen. Das ist eine andere Rolle als das formelle PR-Review durch ein anderes Team.
- Nach dem ersten Commit wechselt das Keyboard. In Runde 2 schreiben beide mit ihrem eigenen GitHub-Konto einen Review-Beitrag.
- In Runde 3 arbeitet jede Person an ihrem eigenen lokalen Labor; danach erklärt ihr euch die Lösung gegenseitig. Bei nur einem Laptop ein zweites frisches Labor erstellen und Keyboard wechseln.

## Gemeinsame Konventionen

Branches heissen zum Beispiel `team-1/hero-copy` oder `team-2/program-update`. Commit-Messages beschreiben das Ergebnis, etwa `docs: clarify volunteer meeting point`. Die Präfixe `docs:`, `feat:` und `fix:` sind eine Teamkonvention und keine Git-Vorschrift. Für diese Markdown-Aufgaben passt meistens `docs:`.

Ein PR pro Team, zwei inhaltlich getrennte Commits, Review im Ring, Nachbesserung auf demselben Branch. Die Moderation gibt nach dem Review die Merge-Runde frei; ein Teammitglied mit Schreibrechten oder die Moderation führt den Merge aus. Niemand genehmigt den eigenen PR.
