---
name: rollback-procedure
package: scf-pycode-crafter
version: 1.0.0
description: Procedure di rollback per annullare modifiche problematiche.
---

# Skill: Rollback Procedure

## Rollback git (non ancora pushato)

```bash
# Annulla ultimo commit mantenendo le modifiche
git reset --soft HEAD~1

# Annulla ultimo commit rimuovendo le modifiche
git reset --hard HEAD~1

# Annulla modifiche su file specifico
git checkout -- <file>

# Annulla staging
git reset HEAD <file>
```

## Rollback git (già pushato)

```bash
# Crea commit di revert (preferito — non riscrive storia)
git revert <commit-sha>
git push

# Force push (solo su branch personali, mai su main)
git reset --hard <commit-sha>
git push --force-with-lease
```

## Rollback dipendenze

```bash
# Torna a versione precedente di un pacchetto
pip install pacchetto==versione-precedente
pip freeze > requirements.txt
```

## Decisione rollback vs fix-forward

Scegli **rollback** se:
- Il bug è critico e il fix non è immediato
- La modifica ha introdotto regressioni multiple
- Il branch è condiviso e altri sono bloccati

Scegli **fix-forward** se:
- Il bug è isolato e la correzione è semplice
- Il rollback causerebbe perdita di altri lavori
