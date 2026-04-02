---
name: clean-architecture
package: scf-pycode-crafter
version: 2.0.0
description: Regole di clean architecture per progetti Python.
---

# Skill: Clean Architecture Rules

## Layer e dipendenze

```
UI / CLI / API
     ↓
Use Cases / Application
     ↓
Domain / Business Logic
     ↓
Infrastructure / Adapters
```

Le dipendenze puntano sempre verso il basso. I layer interni non conoscono quelli esterni.

## Regole fondamentali

- **Single Responsibility:** ogni modulo, classe e funzione ha una sola ragione per cambiare
- **Dependency Inversion:** dipendi da astrazioni (ABC, Protocol), non da implementazioni concrete
- **Interface Segregation:** interfacce piccole e coese, non monolitiche
- **Separation of Concerns:** logica di business separata da I/O, UI, DB, rete
- **Pure functions first:** preferisci funzioni senza side effect dove possibile

## Segnali di violazione

- Import diretti tra layer non adiacenti
- Logica di business in handler HTTP o callback UI
- Dipendenze circolari tra moduli
- Classi God con troppe responsabilità
- Test che richiedono setup infrastrutturale complesso

## In Python

- Usa `abc.ABC` o `typing.Protocol` per le interfacce
- Separa `src/domain/`, `src/application/`, `src/infrastructure/`
- I test del dominio non devono mai importare da infrastructure
