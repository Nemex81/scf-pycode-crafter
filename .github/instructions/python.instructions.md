---
applyTo: "**/*.py"
name: python
package: scf-pycode-crafter
version: 1.2.1
spark: true
---

# Instruction: Python

Questa instruction si applica a tutti i file `.py` del workspace.

## Standard

- Python 3.10+ con type hints obbligatori per funzioni pubbliche
- Docstring per moduli, classi pubbliche e funzioni pubbliche
- f-string per formattazione stringhe
- `pathlib.Path` per operazioni su file (no `os.path`)
- Dataclass per strutture dati semplici
- Context manager per risorse (file, connessioni, lock)

## Stile

- Nomi variabili e funzioni in `snake_case`
- Nomi classi in `PascalCase`
- Costanti in `UPPER_SNAKE_CASE`
- Lunghezza riga max 100 caratteri
- Import ordinati: stdlib, third-party, locale (isort/ruff)

## Errori

- Gestione esplicita con eccezioni tipizzate
- Non usare `except Exception` senza motivazione
- Non sopprimere eccezioni con `pass`
- Log degli errori prima di ri-sollevare

## Test

- Framework: pytest
- File di test: `tests/test_<nome_modulo>.py`
- Naming: `test_<cosa>_<condizione>_<risultato_atteso>`
- Evita mock eccessivi: testa comportamenti, non implementazioni
