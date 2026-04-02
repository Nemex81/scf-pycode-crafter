---
name: semantic-gate
package: scf-pycode-crafter
version: 1.2.1
description: Validazione semantica pre-commit per garantire qualità del codice.
spark: true
---

# Skill: Semantic Gate

## Scopo

Definisce i criteri di accettazione semantica che il codice deve soddisfare
prima di essere committato o mergiato.

## Gate obbligatori

### 1. Correttezza funzionale
- Tutti i test unitari passano: `pytest`
- Nessuna regressione rispetto al commit precedente

### 2. Type safety
- `mypy` senza errori (o con solo warning documentati)
- Tutti i parametri pubblici hanno type hints

### 3. Stile
- `ruff` o `flake8` senza violazioni bloccanti
- Nessun `TODO` o `FIXME` non tracciato in un issue

### 4. Documentazione
- Funzioni e classi pubbliche con docstring
- CHANGELOG aggiornato se la modifica è visibile all'utente

## Gate consigliati (non bloccanti)

- Coverage test >= 70% per logica di business
- Nessuna dipendenza circolare nuova
- Complessità ciclomatica <= 10 per funzione

## Comportamento

Se un gate fallisce:
1. Segnala quale gate e perché
2. Non procedere con commit o merge
3. Indica come risolvere il problema
