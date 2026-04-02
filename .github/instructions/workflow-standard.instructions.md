---
applyTo: "**"
name: workflow-standard
package: scf-pycode-crafter
version: 1.2.1
spark: true
---

# Instruction: Workflow Standard

## Sequenza standard per nuova funzionalità

1. **Plan** — definisci task, dipendenze, criteri di accettazione
2. **Design** — architettura e interfacce se il task è complesso
3. **Code** — implementazione seguendo i principi in `python.instructions`
4. **Validate** — pytest + mypy + ruff
5. **Docs** — aggiorna docstring, README, CHANGELOG se necessario
6. **Git** — commit atomico con Conventional Commit

## Regole workflow

- Non saltare la fase di validazione prima del commit
- Non mescolare funzionalità diverse nello stesso commit
- Se la validazione fallisce, torna alla fase Code
- Documenta le decisioni significative prima di dimenticarle

## Checklist pre-commit

- [ ] `pytest` — tutti i test passano
- [ ] `mypy` — 0 errori
- [ ] `ruff` — 0 violazioni
- [ ] Docstring aggiornate
- [ ] CHANGELOG aggiornato (se modifica visibile)
