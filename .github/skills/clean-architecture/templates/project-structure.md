# Struttura progetto Python — Clean Architecture

```
project-name/
├── src/
│   ├── domain/          # entità, value objects, interfacce — zero dipendenze esterne
│   │   ├── __init__.py
│   │   ├── entities.py
│   │   └── interfaces.py
│   ├── application/     # use cases, orchestrazione — dipende solo da domain
│   │   ├── __init__.py
│   │   └── use_cases.py
│   ├── infrastructure/  # DB, API, file system, framework — dipende da domain
│   │   ├── __init__.py
│   │   └── adapters.py
│   └── main.py          # entry point — assembla i layer
├── tests/
│   ├── unit/            # testano domain e application in isolamento
│   ├── integration/     # testano infrastructure con dipendenze reali
│   └── conftest.py
├── docs/
├── requirements.txt
└── pyproject.toml
```

## Regola di import

- `domain` non importa da nessun altro layer
- `application` importa solo da `domain`
- `infrastructure` importa da `domain` (mai da `application`)
- `main.py` è l'unico punto che assembla tutto
