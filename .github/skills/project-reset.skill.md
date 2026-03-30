---
name: project-reset
package: scf-pycode-crafter
version: 1.0.0
description: Procedura di reset del contesto SCF per una nuova sessione di lavoro.
---

# Skill: Project Reset

## Quando usare

- Inizio di una nuova sessione di lavoro
- Dopo un lungo periodo di inattività
- Quando il contesto sembra desincronizzato dalla realtà del codice
- Prima di affrontare un task complesso

## Procedura di reset

1. `scf_get_project_profile()` — ricarica il profilo progetto
2. `scf_get_global_instructions()` — ricarica le istruzioni operative
3. `scf_get_workspace_info()` — verifica stato workspace
4. Leggi i file rilevanti per il task corrente (non tutto il codebase)
5. Verifica lo stato git: `git status`, `git log --oneline -5`

## Output atteso

Dopo il reset, l'assistente deve poter rispondere a:
- Qual è lo stato attuale del progetto?
- Quali agenti e skill sono disponibili?
- Ci sono task in sospeso o branch attivi?

## Regola

Non assumere che il contesto della sessione precedente sia ancora valido.
Un reset all'inizio di ogni sessione è buona pratica.
