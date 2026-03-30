---
name: docs_manager
package: scf-pycode-crafter
version: 1.0.0
description: Gestione completa della documentazione di un progetto Python.
---

# Skill: Docs Manager

## Responsabilità

Gestisce la creazione, aggiornamento e coerenza della documentazione del progetto.

## Tipi di documentazione

### Docstring
- Obbligatorie per moduli, classi pubbliche, funzioni pubbliche
- Formato: Google style (preferito) o reStructuredText
- Includere: descrizione, Args, Returns, Raises, Examples (quando utile)

### README.md
Struttura minima:
```markdown
# Nome Progetto
Breve descrizione.

## Installazione
## Uso
## Struttura progetto
## Sviluppo
## Licenza
```

### CHANGELOG.md
- Formato Keep a Changelog
- Aggiornato ad ogni release
- Usa skill `changelog-entry` per generare voci

### Decisioni architetturali (ADR)
- File `docs/adr/NNN-titolo.md`
- Struttura: Contesto → Decisione → Conseguenze

## Regole

- Non documentare il codice ovvio
- Aggiungi valore con contesto e motivazione, non con parafrasi del codice
- Mantieni la documentazione aggiornata quando il codice cambia
- I commenti inline spiegano il **perché**, non il **cosa**
