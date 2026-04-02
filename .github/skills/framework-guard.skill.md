---
name: framework-guard
package: scf-pycode-crafter
version: 1.2.1
description: Protezione dell'integrità del framework SCF nel workspace.
spark: true
---

# Skill: Framework Guard

## Scopo

Garantire che le modifiche al codice del progetto non danneggino accidentalmente
la struttura del framework SCF installato in `.github/`.

## File SCF protetti

Tutti i file in `.github/` sono gestiti dal framework SCF:
- `.github/agents/*.md`
- `.github/skills/*.skill.md`
- `.github/instructions/*.instructions.md`
- `.github/prompts/*.prompt.md`
- `.github/copilot-instructions.md`
- `.github/project-profile.md`
- `.github/AGENTS.md`

## Regole

- Non modificare file SCF durante task di sviluppo del progetto principale
- Se una modifica a `.github/` è necessaria, trattarla come task separato
- Le modifiche a file SCF devono essere committate separatamente dal codice applicativo
- Segnalare sempre quando un'operazione potrebbe toccare `.github/`

## Comportamento in caso di conflitto

Se un task richiede modifiche che coinvolgono `.github/`:
1. Interrompi il task corrente
2. Notifica l'utente della situazione
3. Chiedi conferma esplicita prima di procedere
4. Esegui le modifiche SCF in un commit dedicato
