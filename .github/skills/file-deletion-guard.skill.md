---
name: file-deletion-guard
package: scf-pycode-crafter
version: 1.2.1
description: Protezione contro eliminazioni accidentali di file critici del progetto.
spark: true
---

# Skill: File Deletion Guard

## File sempre protetti (mai eliminare senza conferma esplicita)

- `.github/` — qualsiasi file del framework SCF
- `pyproject.toml` — configurazione build
- `requirements.txt`, `requirements-dev.txt` — dipendenze
- `README.md` radice — documentazione principale
- `CHANGELOG.md` — storico versioni
- Qualsiasi file di configurazione CI/CD
- File di migrazione database

## Procedura prima di eliminare

1. Verifica che nessun altro file importi o referenzi il file da eliminare
2. Controlla git log per capire quando e perché è stato creato
3. Se il file ha modifiche non committate, salvale prima
4. Esegui i test dopo l'eliminazione per verificare nessuna regressione

## Segnali di allarme

- Eliminazione richiesta in blocco (`rm -rf`, `git clean -fd`)
- Eliminazione di file in `src/` senza analisi delle dipendenze
- Eliminazione durante un refactoring non pianificato

## Comportamento atteso

Se viene richiesta l'eliminazione di un file protetto o sospetto:
1. Notifica l'utente con il file coinvolto
2. Chiedi conferma esplicita
3. Proponi alternativa (rinomina, deprecazione, commento) se appropriato
