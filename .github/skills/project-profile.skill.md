---
name: project-profile
package: scf-pycode-crafter
version: 1.2.1
description: Lettura e interpretazione del project-profile.md SCF.
spark: true
---

# Skill: Project Profile

## Scopo

Il `project-profile.md` è il file di configurazione centrale del workspace SCF.
Questa skill definisce come leggerlo e usarlo.

## Campi principali

| Campo | Tipo | Descrizione |
|---|---|---|
| `initialized` | bool | `true` se il progetto è stato configurato |
| `project_name` | string | Nome del progetto |
| `project_type` | string | Tipo (python, web, cli, library...) |
| `language` | string | Linguaggio principale |
| `framework` | string | Pacchetto SCF installato |

## Procedura di lettura

1. `scf_get_project_profile()` — leggi il profilo via MCP
2. Controlla `initialized: true` — se false, avvisa l'utente
3. Usa i metadati per contestualizzare le risposte successive

## Inizializzazione

Se `initialized: false`:
1. Spiega all'utente che il progetto non è configurato
2. Guida nella compilazione dei campi obbligatori
3. Imposta `initialized: true` dopo la compilazione
4. Fai commit del profilo aggiornato
