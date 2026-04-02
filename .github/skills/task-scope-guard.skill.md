---
name: task-scope-guard
package: scf-pycode-crafter
version: 1.2.1
description: Delimita lo scope delle operazioni per evitare modifiche fuori contesto.
spark: true
---

# Skill: Task Scope Guard

## Scopo

Evitare che operazioni su un componente si propaghino accidentalmente ad altri.

## Regole di scope

### Sviluppo funzionalità
- Opera solo nei file del task corrente
- Non modificare file non menzionati nel task
- Non refactoring opportunistico su file che "si trovano nel percorso"

### Modifica framework SCF
- Solo file in `.github/`
- Commit separato dal codice applicativo
- Non toccare logica applicativa durante task SCF

### Task di test
- Solo file in `tests/`
- Non modificare il codice sorgente durante scrittura test
- Se il codice sorgente deve cambiare, è un task separato

## Segnali di violazione

- Diff che tocca file in directory diverse senza motivazione esplicita
- Modifiche a file di configurazione durante task di sviluppo
- Commit che mescola codice applicativo e aggiornamenti documentazione

## Comportamento atteso

Se durante un task si rileva la necessità di modificare file fuori scope:
1. Completa il task corrente
2. Crea un nuovo task separato per le modifiche fuori scope
3. Segnala all'utente cosa è stato trovato fuori scope
