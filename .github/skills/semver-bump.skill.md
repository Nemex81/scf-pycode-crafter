---
name: semver-bump
package: scf-pycode-crafter
version: 1.2.1
description: Calcolo del bump di versione semver in base alle modifiche.
spark: true
---

# Skill: Semver Bump

## Regole semver

**MAJOR.MINOR.PATCH**

| Tipo di modifica | Bump |
|---|---|
| Breaking change API pubblica | MAJOR |
| Nuova funzionalità retrocompatibile | MINOR |
| Bugfix retrocompatibile | PATCH |
| Solo documentazione / refactoring interno | PATCH o nessuno |

## Algoritmo di decisione

1. Ci sono breaking changes? → MAJOR
2. Ci sono nuove funzionalità? → MINOR
3. Ci sono solo bugfix? → PATCH
4. Solo docs/chore? → considera PATCH o nessun bump

## In pyproject.toml

```toml
[project]
version = "1.2.3"
```

Aggiornare manualmente o con tool come `bump2version` o `poetry version`.

## Versioni pre-release

- Alpha: `1.0.0-alpha.1`
- Beta: `1.0.0-beta.1`
- Release candidate: `1.0.0-rc.1`
