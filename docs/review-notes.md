# Review der ursprünglichen Übung

Geprüfter Ausgangsstand: Commit `3ef28e1` (`feat: create git workflow workshop repo`). Review vom 20. September 2026. Rahmen: zehn Personen, fünf Zweierteams, zwei Stunden, GitHub.

## Gesamturteil

Die kleine Campus-Festival-Aufgabe ist ein geeigneter Träger für Git-Lernen: wenig fachliche Einstiegshürde, überschaubare Diffs, mehrere unabhängige Aufgaben. Verbessert werden mussten vor allem die Durchführbarkeit, die individuellen Lernziele und die konkreten Git-Schritte.

| Befund | Auswirkung | Eingearbeitete Verbesserung |
| --- | --- | --- |
| Ziel „alle erstellen einen PR und lösen einen Konflikt“ bei einem PR pro Paar | Teilnahme und persönlicher Kompetenznachweis wurden vermischt | Lernziele nach Team und Person getrennt; Keyboardwechsel und individueller Konfliktdurchlauf |
| Konfliktübung ohne festgelegten gemeinsamen Ausgangscommit und Startbarriere | Je nach Reihenfolge entsteht kein Konflikt | Reproduzierbares lokales Labor; PR-Transfer mit identischer Basis und Barriere |
| Fünf Teams, aber Konfliktzuordnung nur abstrakt als A/B | Unklare Rollen; nicht alle müssen lösen | Gleicher Konflikt auf jedem Laptop; optionaler PR-Konflikt als zusätzliche Teamaufgabe |
| Fast-Forward im Titel, ohne ausführbare Demonstration | Begriff bleibt abstrakt | Erfolgreiches FF, erwartete Ablehnung bei Divergenz, Rebase und erneutes FF |
| Rebase/Squash ohne Abgrenzung zu veröffentlichten Branches | Unnötige Force-Push-Probleme in der Session | Lokale Labore ohne Remote, eigene Bonusaufgabe und klare Erklärung der History-Umschreibung |
| Merge-Regeln zwischen Runde 1 und 2 nicht eindeutig | PR könnte vor dem geplanten Review verschwinden | Runde 1 bleibt offen, Merge erst nach finalem Review in Runde 2 |
| Unterschiedliche Review-Mindestvorgaben | Unklar, wann ein Review fertig ist | Einheitlich begründete Stärke plus Frage/Verbesserung; beide Personen schreiben |
| Fehlende Abnahmekriterien und Prüfschritte | „Funktioniert“ ersetzt Inhaltsprüfung | Konkrete Kriterien pro Mission sowie Diff, Vorschau und Status als Belege |
| Setup und Fork-Ablauf nur angedeutet | Authentifizierung und falsche Remotes kosten Workshop-Zeit | Vorab-Setup, Push-Probe, korrekte origin/upstream-Wege |
| Nur kurze Moderationsnotizen, kein Glossar | Fachlich richtige spontane Erklärungen unnötig schwierig | Vollständiges Drehbuch, Spickzettel, Glossar mit Rückfragen und präzisen Formulierungen |

## Beobachtete GitHub-Konfiguration

Beim Review war `main` ohne klassische Branch Protection; die Repository-Ruleset-Liste war leer. Alle drei PR-Merge-Methoden waren erlaubt. Die fünf Warmup-Issues #1–#5 und das Label `workshop` waren vorhanden. Dies ist eine Momentaufnahme; vor jeder Durchführung erneut prüfen. Dieses Review verändert keine Repository-Einstellungen oder bestehenden Issues.

## Was vor der Durchführung offen bleibt

Workshop-Kopie wählen, Teilnehmendenrechte und Schutzregeln nach [Setup](setup.md) einrichten und mit zwei Konten prüfen. Die lokalen Git-Abläufe lassen sich automatisiert testen; eine Live-Durchführung mit zehn Personen und unterschiedlichen Geräten wird dadurch nicht simuliert. Die Zeiten sind Moderationsvorgaben mit Puffer, keine gemessenen Lerngeschwindigkeiten.

Die Teilnehmeraufträge bleiben bewusst klein. Wer alle Schritte einzeln auf GitHub durchführen oder zusätzlich echte PR-Konflikte üben möchte, plant mindestens eine weitere halbe Stunde ein.

## Technische Validierung dieser Überarbeitung

- Acht Ende-zu-Ende-Tests mit `python3 scripts/test-labs.py` bestanden: Konfliktlösung, Merge-Abbruch, Fast-Forward, Rebase, interaktiver Squash, saubere Labore ohne Remote, wiederholte Erzeugung und Schutz bestehender Zielverzeichnisse.
- Shell-Syntax mit `bash -n` geprüft; interne Markdown-Dateilinks und verwendete Überschriftenanker geprüft; `git diff --check` ohne Befund.
- Ausgeführt auf macOS mit Bash 3.2, Git 2.54.0 und Python 3.14.5. Windows/Git Bash und Linux wurden nicht separat ausgeführt.
- Git- und GitHub-Aussagen anhand der in Übungen und Glossar verlinkten offiziellen Dokumentation abgeglichen. PR-Berechtigungen und der Gruppenablauf müssen in der tatsächlichen Workshop-Umgebung geprobt werden.
