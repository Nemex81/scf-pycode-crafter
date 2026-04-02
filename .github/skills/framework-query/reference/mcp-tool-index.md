# MCP Tool Index — SPARK Framework

## Struttura workspace `.github/`

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

## Tool MCP per categoria

### Workspace e progetto
| Tool | Scopo |
|------|-------|
| `scf_get_workspace_info` | Stato generale, contatori e path del workspace |
| `scf_get_project_profile` | Profilo e configurazione del progetto |
| `scf_get_global_instructions` | Istruzioni globali Copilot |

### Agenti
| Tool | Scopo |
|------|-------|
| `scf_list_agents` | Lista tutti gli agenti disponibili |
| `scf_get_agent(name)` | Contenuto di un agente specifico |

### Skill
| Tool | Scopo |
|------|-------|
| `scf_list_skills` | Lista tutte le skill disponibili |
| `scf_get_skill(name)` | Contenuto di una skill specifica |

### Istruzioni e prompt
| Tool | Scopo |
|------|-------|
| `scf_list_instructions` | Lista instruction disponibili |
| `scf_list_prompts` | Lista prompt disponibili |

### Pacchetti SCF
| Tool | Scopo |
|------|-------|
| `scf_list_installed_packages` | Pacchetti installati nel workspace |
| `scf_list_available_packages` | Pacchetti disponibili nel registry |
| `scf_get_package_info(id)` | Dettagli di un pacchetto specifico |
| `scf_verify_system` | Verifica coerenza cross-component del sistema |
