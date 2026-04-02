---
name: project-doc-bootstrap
package: scf-pycode-crafter
version: 2.0.0
description: Bootstrap documentazione iniziale per un nuovo progetto Python.
---

# Skill: Project Doc Bootstrap

## Scopo

Crea la struttura documentale minima per un nuovo progetto Python.

## File da creare

### README.md (radice)
```markdown
# Nome Progetto

Breve descrizione del progetto.

## Requisiti
- Python >= 3.10

## Installazione
```bash
pip install -r requirements.txt
```

## Uso
<istruzioni base di utilizzo>

## Struttura
```
src/     — sorgenti
tests/   — test automatici
docs/    — documentazione
```

## Sviluppo
```bash
pip install -r requirements-dev.txt
pytest
```
```

### CHANGELOG.md
```markdown
# Changelog

Tutte le modifiche notevoli sono documentate in questo file.
Formato: [Keep a Changelog](https://keepachangelog.com/it/1.0.0/)

## [Unreleased]
```

### docs/
- `docs/adr/` — decisioni architetturali
- `docs/api/` — documentazione API (se applicabile)

## Quando usare

All'inizio di un nuovo progetto o quando la documentazione
esistente è assente o completamente obsoleta.
