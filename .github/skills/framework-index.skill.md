---
name: framework-index
package: scf-pycode-crafter
version: 1.0.0
description: Indice e navigazione del framework SCF nel workspace corrente.
---

# Skill: Framework Index

## Scopo

Fornisce un indice navigabile del framework SCF installato nel workspace.
Usata da py-Agent-Helper per rispondere a domande sulla struttura del framework.

## Come ottenere l'indice

Tramite il server MCP spark-framework-engine:
- `scf_get_workspace_info` — stato generale del workspace
- `scf_list_agents` — lista agenti disponibili
- `scf_list_skills` — lista skill disponibili
- `scf_list_instructions` — lista instruction disponibili
- `scf_list_prompts` — lista prompt disponibili

## Struttura attesa in `.github/`

```
.github/
├── AGENTS.md
├── copilot-instructions.md
├── project-profile.md
├── agents/
├── skills/
├── instructions/
└── prompts/
```

## Uso

Quando un utente chiede "quali agenti ho?" o "cosa contiene il framework?",
consulta prima `scf_get_workspace_info` poi rispondi con l'indice aggiornato.
