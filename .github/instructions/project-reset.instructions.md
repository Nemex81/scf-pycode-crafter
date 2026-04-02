---
applyTo: "**"
name: project-reset
package: scf-pycode-crafter
version: 1.2.1
spark: true
---

# Instruction: Project Reset

All'inizio di ogni sessione di lavoro:

1. Interroga `scf_get_project_profile()` per caricare il contesto del progetto
2. Interroga `scf_get_global_instructions()` per le istruzioni operative
3. Verifica stato git con `git status` e `git log --oneline -5`
4. Leggi solo i file rilevanti per il task corrente

Non assumere che il contesto della sessione precedente sia ancora valido.
Un reset all'inizio di ogni sessione è buona pratica.
