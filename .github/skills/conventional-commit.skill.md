---
name: conventional-commit
package: scf-pycode-crafter
version: 1.2.1
description: Formato Conventional Commits per messaggi di commit git.
spark: true
---

# Skill: Conventional Commit

## Formato

```
tipo(scope): descrizione breve

[corpo opzionale]

[footer opzionale]
```

## Tipi

| Tipo | Quando usarlo |
|---|---|
| `feat` | Nuova funzionalità |
| `fix` | Bugfix |
| `refactor` | Refactoring senza cambio comportamento |
| `docs` | Solo documentazione |
| `test` | Aggiunta o modifica test |
| `chore` | Build, dipendenze, config |
| `perf` | Ottimizzazione performance |
| `ci` | Pipeline CI/CD |
| `style` | Formattazione, whitespace |

## Regole

- Descrizione breve: max 72 caratteri, imperativo presente
- Scope: nome del modulo o componente (opzionale ma consigliato)
- Breaking change: aggiungi `!` dopo il tipo: `feat!: ...` e specifica nel footer
- Esempi validi:
  - `feat(auth): aggiunge validazione token JWT`
  - `fix(parser): corregge encoding UTF-8 su Windows`
  - `refactor(core): sposta logica in domain layer`
