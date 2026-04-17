---
spark: true
scf_file_role: "config"
scf_version: "2.0.1"
scf_merge_strategy: "merge_sections"
scf_protected: false
scf_owner: "scf-pycode-crafter"
scf_merge_priority: 30
---
## Istruzioni SCF Python CodeCrafter

Questo pacchetto aggiunge al framework le regole operative e gli agenti Python-specifici.

- Usa gli agenti `py-Agent-*` per analisi, design, code, plan e validate su task Python.
- Applica sempre `.github/instructions/python.instructions.md` per file `*.py`.
- Applica anche `.github/instructions/tests.instructions.md` quando lavori in `tests/`.
- Mantieni type hints, docstring, `pathlib.Path`, pytest e gestione esplicita delle eccezioni.
- Nei test privilegia fixture pytest, isolamento dei casi e mock limitati alle dipendenze esterne.