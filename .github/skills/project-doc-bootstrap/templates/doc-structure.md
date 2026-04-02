# Struttura documentazione progetto Python

```
docs/
├── README.md              ← descrizione generale, installazione, uso rapido
├── CHANGELOG.md           ← storico versioni in formato Keep a Changelog
├── architecture/
│   ├── overview.md        ← diagramma layer e scelte architetturali principali
│   └── adr/               ← Architecture Decision Records numerati
│       └── 001-titolo.md
├── api/
│   └── reference.md       ← riferimento API pubblica (generabile da docstring)
└── guides/
    ├── setup.md           ← setup ambiente di sviluppo
    ├── testing.md         ← come eseguire i test
    └── contributing.md    ← linee guida contribuzione
```

## Priorità di creazione

1. `README.md` — obbligatorio, crea subito
2. `CHANGELOG.md` — obbligatorio, crea al primo commit
3. `architecture/overview.md` — crea quando l'architettura è stabile
4. `adr/` — crea al primo snodo decisionale significativo
5. `api/` e `guides/` — crea quando il progetto è pronto per utenti esterni
