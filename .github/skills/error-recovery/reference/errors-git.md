# Errori Git comuni — Reference

| Errore | Soluzione |
|--------|-----------|
| `error: failed to push some refs` | `git pull --rebase` poi ripeti il push |
| `CONFLICT (content): Merge conflict in X` | Risolvi manualmente, `git add X`, `git rebase --continue` |
| `detached HEAD state` | `git checkout main` per tornare sul branch |
| `Your branch is behind 'origin/main'` | `git pull --rebase origin main` |
| `nothing to commit, working tree clean` | Non c'è niente da committare — comportamento normale |
| `error: pathspec 'X' did not match any file(s)` | Il file non esiste o il path è errato |
