# Istruzioni globali Copilot — scf-pycode-crafter

Queste istruzioni si applicano a tutti gli agenti e alle sessioni Copilot in questo workspace Python.

## Profilo sviluppatore

Questo workspace usa il pacchetto SCF `scf-pycode-crafter`. Copilot opera in un ambiente Python professionale con focus su qualità, leggibilità e manutenibilità del codice.

## Principi di sviluppo

- **Modularità:** funzioni e classi con responsabilità singola e ben definita
- **Leggibilità:** codice chiaro prima di codice furbo
- **Separazione:** logica di business separata da I/O e UI
- **Nomi espliciti:** variabili e funzioni con nomi che documentano l'intenzione
- **Commenti utili:** spiega il perché, non il cosa
- **Testabilità:** scrivi codice facile da testare, preferisci funzioni pure

## Standard tecnici Python

- Python 3.10+ con type hints
- Docstring in formato Google style o reStructuredText
- Gestione errori esplicita con eccezioni tipizzate
- f-string per la formattazione di stringhe
- Dataclass o NamedTuple per strutture dati semplici
- `pathlib.Path` invece di `os.path`

## Workflow

- Analizza sempre il contesto del file prima di modificare
- Proponi architettura prima di implementare funzionalità complesse
- Segnala trade-off tecnici quando esistono
- Non fare refactor non richiesti
- Mantieni coerenza con lo stile già presente nel codebase

## Testing

- Usa pytest come framework di test
- Test unitari per logica di business
- Nomi di test descrittivi: `test_<cosa>_<condizione>_<risultato_atteso>`
- Evita mock eccessivi: testa comportamenti, non implementazioni

## Git

- Commit atomici con messaggio descrittivo
- Formato: `tipo: descrizione breve` (feat, fix, refactor, docs, test, chore)
- Branch per funzionalità isolate
