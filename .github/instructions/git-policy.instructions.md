---
applyTo: "**"
name: git-policy
package: scf-pycode-crafter
version: 1.2.1
spark: true
---

# Instruction: Git Policy

## Commit

- Usa Conventional Commits: `tipo(scope): descrizione`
- Commit atomici: una modifica logica per commit
- Non committare mai file generati, cache, `.pyc`, ambienti virtuali
- Verifica sempre con `git diff --cached` prima di committare

## Branch

- `main` — sempre stabile, CI deve passare
- `feature/nome` — nuove funzionalità
- `fix/nome` — bugfix
- `release/x.y.z` — preparazione release
- Non sviluppare direttamente su `main` per task non banali

## Push

- Non fare `git push --force` su `main`
- Usa `--force-with-lease` se necessario su branch personali
- Prima del push: `git pull --rebase` per mantenere storia lineare

## .gitignore obbligatori per Python

```
__pycache__/
*.pyc
*.pyo
.venv/
venv/
.env
dist/
build/
*.egg-info/
.mypy_cache/
.pytest_cache/
.ruff_cache/
```
