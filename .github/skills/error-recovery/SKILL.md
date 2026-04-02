---
name: error-recovery
package: scf-pycode-crafter
version: 1.2.1
description: Procedure di recovery da errori comuni durante lo sviluppo Python.
spark: true
---

# Skill: Error Recovery

## Errori di import

```
ModuleNotFoundError: No module named 'X'
```
- Verifica che il modulo sia in `requirements.txt`
- Controlla che il virtualenv sia attivato
- Verifica `PYTHONPATH` se si usa struttura `src/`

## Errori mypy

- `error: Incompatible types` → controlla type hints della funzione
- `error: Item "None" of "Optional[X]" has no attribute` → aggiungi guard `if x is not None`
- `error: Cannot find implementation or library stub` → aggiungi stub o `# type: ignore`

## Errori pytest

- `FAILED test_X - AssertionError` → leggi il diff assertion, confronta expected/actual
- `ERROR test_X - fixture 'Y' not found` → verifica conftest.py e scope fixture
- `ImportError` in test → verifica struttura package e `__init__.py`

## Errori git

- `error: failed to push some refs` → fai `git pull --rebase` prima del push
- `CONFLICT` → risolvi manualmente, poi `git add` + `git rebase --continue`
- `detached HEAD` → torna su branch con `git checkout main`

## Principio generale

1. Leggi l'errore completo — non solo la prima riga
2. Identifica il file e la riga esatta
3. Capisce il tipo di errore prima di agire
4. Correggi una cosa alla volta
5. Verifica dopo ogni correzione
