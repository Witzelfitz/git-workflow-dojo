# Übung 2: Review → Nachbesserung → Merge

**20 Minuten.** Start: fünf offene PRs aus Runde 1. Review-Ring: **1 → 2 → 3 → 4 → 5 → 1**. Beide Personen kommentieren mit ihrem eigenen GitHub-Konto.

## Review, 8 Minuten

Öffnet **Files changed** und lest Auftrag, Beschreibung und Diff. Prüft Inhalt, Verständlichkeit und Markdown-Vorschau. Pro Review-Team braucht es:

- eine konkrete positive Beobachtung mit Begründung;
- eine begründete Rückfrage oder Verbesserung, die dem Auftrag hilft.

Beispiel: „Die Uhrzeiten sind jetzt leichter zu scannen. Beim neuen Slot fehlt der Ort; könnt ihr ihn ergänzen, damit Gäste direkt wissen, wohin sie müssen?“

Eine Person kann die positive Beobachtung, die andere die Frage beitragen. **Add review comment / Start a review** allein reicht noch nicht: das Review danach über **Review changes / Submit review** absenden, sonst bleiben Kommentare ausstehend.

Wählt **Comment** für Rückfragen und unverbindliche Vorschläge, **Request changes** für einen begründeten Mangel, der vor dem Merge behoben werden muss. **Approve** bedeutet: den aktuellen Stand geprüft und für die Integration freigegeben. Keine künstlichen Fehler oder Change Requests erzwingen; wenn der Auftrag bereits erfüllt ist, eine kleine echte Verbesserung gemeinsam vereinbaren.

## Nachbessern, 7 Minuten

Autor:innen antworten, setzen mindestens eine sinnvolle Verbesserung um und bleiben auf **demselben Feature-Branch**:

```bash
git status
git diff
# Beispiel Team 1: Dateipfad für andere Teams anpassen.
git add app/index.md
git diff --staged
git commit -m "docs: clarify call to action after review"
git push
```

Der bestehende PR aktualisiert sich automatisch. Reviewer prüfen den neuen Diff und geben die finale Freigabe. Offene Diskussionen erst nach Klärung auflösen. Ein formelles **Request changes** benötigt eine erneute Freigabe; „Resolve conversation“ allein ist keine Zustimmung.

## Merge und Synchronisation, 5 Minuten

Nach Freigabe durch die Moderation nacheinander **Create a merge commit** wählen. Person mit Schreibrechten oder Moderation merged. Danach lokal:

```bash
git switch main
git pull --ff-only origin main
git log --oneline --graph --decorate -12
```

Im Fork-Modell gilt die [abweichende Aktualisierung](../docs/setup.md#alternative-forks). Lokale Branches dürfen fürs Nachschauen bestehen bleiben.

## Fertig, wenn

- [ ] Beide Personen haben einen sichtbaren Review-Beitrag geschrieben.
- [ ] Feedback ist beantwortet, eine Verbesserung übernommen und der finale Diff freigegeben.
- [ ] PR ist gemergt; lokaler `main` ist aktualisiert.

**Kontrollfrage:** Ein grünes „mergeable“ bestätigt, dass Git technisch zusammenführen kann. Es sagt nichts darüber aus, ob Inhalt oder Verhalten richtig sind.
