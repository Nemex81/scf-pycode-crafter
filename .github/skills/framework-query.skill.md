---
name: framework-query
package: scf-pycode-crafter
version: 1.0.0
description: Pattern per interrogare il framework SCF tramite il server MCP.
---

# Skill: Framework Query

## Quando usare i tool MCP SCF

Prima di rispondere a domande sul progetto o sul framework, interroga il server MCP:

```
scf_get_project_profile()     → stato e profilo del progetto
scf_get_global_instructions() → istruzioni globali Copilot
scf_get_workspace_info()      → contatori e path del workspace
scf_list_agents()             → agenti disponibili
scf_get_agent(name)           → contenuto di un agente specifico
scf_list_skills()             → skill disponibili
scf_get_skill(name)           → contenuto di una skill specifica
```

## Ordine di interrogazione consigliato

1. `scf_get_project_profile` — capire il contesto del progetto
2. `scf_get_global_instructions` — caricare le istruzioni operative
3. Tool specifici in base al task

## Regola

Non assumere il contenuto dei file framework dalla memoria.
Interroga sempre il server MCP per ottenere dati aggiornati dal filesystem reale.
