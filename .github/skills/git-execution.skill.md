---
name: git-execution
package: scf-pycode-crafter
version: 1.0.0
description: Procedure operative per esecuzione comandi git in sicurezza.
---

# Skill: Git Execution

## Pre-flight check

Prima di qualsiasi operazione git distruttiva:
```bash
git status          # verifica stato working tree
git diff --stat     # verifica file modificati
git log --oneline -5  # verifica storia recente
```

## Commit sicuro

```bash
git add <file-specifici>   # mai git add . senza review
git status                 # verifica staging area
git diff --cached          # verifica cosa si sta committando
git commit -m "tipo(scope): descrizione"
```

## Branch workflow

```bash
git checkout -b feature/nome    # crea e vai su nuovo branch
git push -u origin feature/nome # prima push con tracking
# ... sviluppo ...
git checkout main
git pull --rebase
git merge --no-ff feature/nome
git push
```

## Tag di versione

```bash
git tag -a v1.2.3 -m "Release v1.2.3: descrizione"
git push origin v1.2.3
```

## Regole di sicurezza

- Non fare `git push --force` su `main` mai
- Non fare `git reset --hard` senza backup
- Verifica sempre `git status` prima di operazioni distruttive
- In caso di dubbio, crea un branch di backup prima
