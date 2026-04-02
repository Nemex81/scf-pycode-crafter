---
name: code-routing
package: scf-pycode-crafter
version: 1.2.1
description: Routing tra agenti di sviluppo in base alla natura del task di codice.
spark: true
---

# Skill: Code Routing

## Scopo

Quando un task richiede sviluppo codice, questa skill determina quale agente è più adatto.

## Routing logic

### py-Agent-Code
Task di logica pura:
- Implementare funzioni, classi, moduli
- Algoritmi e strutture dati
- Business logic, validazioni, trasformazioni
- Refactoring di logica esistente
- Integrazione tra componenti

### py-Agent-Design
Task architetturali prima dell'implementazione:
- Definire struttura di un nuovo componente
- Scegliere pattern da applicare
- Progettare interfacce e contratti
- Valutare alternative di design

### py-Agent-Validate
Task di verifica post-implementazione:
- Verificare che il codice superi i test
- Controllare type safety con mypy
- Applicare linting
- Validare quality gates

## Regola di precedenza

Design → Code → Validate. Non saltare fasi per task complessi.
Per task semplici e ben definiti, vai diretto a py-Agent-Code.
