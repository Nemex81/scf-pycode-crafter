---
name: style-setup
package: scf-pycode-crafter
version: 1.0.0
description: Configurazione strumenti di stile e linting per Python.
---

# Skill: Style Setup

## Strumenti consigliati

| Strumento | Scopo | Config |
|---|---|---|
| `ruff` | Linting + formatting veloce | `pyproject.toml` |
| `mypy` | Type checking statico | `mypy.ini` o `pyproject.toml` |
| `black` | Formatting opinionated (alternativa a ruff fmt) | `pyproject.toml` |
| `isort` | Ordinamento import (integrato in ruff) | `pyproject.toml` |

## Configurazione minima pyproject.toml

```toml
[tool.ruff]
line-length = 100
target-version = "py310"
select = ["E", "F", "W", "I", "N"]

[tool.mypy]
python_version = "3.10"
strict = false
warn_return_any = true
warn_unused_configs = true

[tool.pytest.ini_options]
testpaths = ["tests"]
```

## Pre-commit hook

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.3.0
    hooks:
      - id: ruff
      - id: ruff-format
```

## Regola

Configura gli strumenti una volta all'inizio del progetto.
Non cambiare configurazione durante lo sviluppo attivo.
