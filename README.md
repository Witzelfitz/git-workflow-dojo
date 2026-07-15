# Git Workflow Dojo

Ein Uebungs-Repo fuer eine 10er-Gruppe, um in rund 2 Stunden einen sauberen Git-Workflow praktisch durchzuspielen.

Im Fokus:

- Branches
- Pull Requests / Merge Requests
- Code Reviews
- Merge Conflicts
- Fast-Forward Merges
- Rebasing
- kleine Team-Absprachen unter Zeitdruck

## Zielbild

Am Ende sollen alle einmal selbst:

1. ein Issue uebernehmen
2. einen Feature-Branch erstellen
3. kleine Aenderungen committen
4. einen PR eroeffnen
5. ein Review geben
6. einen Merge Conflict loesen
7. eine Branch-Historie per Rebase oder Merge bereinigen

## Setup

Empfohlen:

- 10 Teilnehmende
- 1 Trainer:in
- 1 gemeinsames GitHub-Repo
- 5 Zweier-Teams

Jedes Zweier-Team arbeitet parallel an einer kleinen Story. Dadurch entstehen echte Ueberschneidungen, Reviews und Konflikte.

Falls nicht alle direkten Schreibzugriff auf dasselbe Repo haben, funktioniert der Workshop auch im Fork-Modell:

- alle forken dieses Repo
- gearbeitet wird auf Branches im eigenen Fork
- PRs laufen zur zentralen Vorlage

## Ablauf fuer 2 Stunden

1. `00:00-00:15` Einstieg: Branches, PRs, Reviews, Merge-Strategien kurz erklaeren
2. `00:15-00:35` Runde 1: einfache Feature-Branches und erste PRs
3. `00:35-00:55` Runde 2: Reviews, Change Requests, Nachbesserungen
4. `00:55-01:20` Runde 3: absichtliche Konflikte loesen
5. `01:20-01:40` Runde 4: Rebase, Fast-Forward und saubere History
6. `01:40-02:00` Debrief: Was war chaotisch, was war sauber, welche Regeln helfen?

## Start

1. Repo clonen
2. [docs/roles.md](docs/roles.md) lesen und Teams zuteilen
3. [docs/workshop-flow.md](docs/workshop-flow.md) als gemeinsamer Fahrplan verwenden
4. Team-Missionen aus `exercises/` starten

## Repo-Idee

Das Team arbeitet an einer fiktiven Mini-App fuer ein Campus-Festival:

- Startseite textlich verbessern
- Tagesprogramm erweitern
- Snack-Menue anpassen
- Team-Kontakte pflegen
- Status-Board aktualisieren

Die Aenderungen sind klein genug fuer Einsteiger, aber absichtlich so verteilt, dass Konflikte und Review-Situationen entstehen.

## Ordner

- [docs/workshop-flow.md](docs/workshop-flow.md): empfohlener 2h-Ablauf
- [docs/roles.md](docs/roles.md): Rollen und Team-Aufteilung
- [docs/trainer-guide.md](docs/trainer-guide.md): Moderationshilfe
- [exercises/01-warmup.md](exercises/01-warmup.md): erste PRs
- [exercises/02-review-cycle.md](exercises/02-review-cycle.md): Review-Runde
- [exercises/03-conflicts.md](exercises/03-conflicts.md): Konflikte provozieren und loesen
- [exercises/04-history-cleanup.md](exercises/04-history-cleanup.md): Rebase und Fast-Forward
- [app/](app): Mini-Projekt zum Bearbeiten

## Regeln fuer die Gruppe

- `main` bleibt stabil.
- Es wird nichts direkt auf `main` committed.
- Jede Aenderung laeuft ueber einen Branch und PR.
- Vor jedem Merge gibt es mindestens 1 Review.
- Konflikte werden nicht weggedrueckt, sondern verstanden.

## Optional fuer den Trainer

Wenn du den Druck erhoehen willst:

- zwei Teams gleichzeitig dieselbe Datei anfassen lassen
- eine PR absichtlich mit unklarer Beschreibung erstellen lassen
- einen Review mit echten Change Requests verlangen
- nach einem Konflikt sowohl `merge` als auch `rebase` vergleichen
