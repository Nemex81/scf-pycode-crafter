---
name: changelog-entry
package: scf-pycode-crafter
version: 1.2.1
description: Genera una voce di changelog strutturata in formato Keep a Changelog.
spark: true
---

# Skill: Changelog Entry

## Formato standard

Usa il formato [Keep a Changelog](https://keepachangelog.com/it/1.0.0/).

```markdown
## [X.Y.Z] - YYYY-MM-DD

### Added
- Descrizione funzionalità aggiunta

### Changed
- Descrizione modifica comportamento esistente

### Fixed
- Descrizione bug risolto

### Removed
- Descrizione funzionalità rimossa

### Deprecated
- Descrizione funzionalità deprecata

### Security
- Descrizione fix di sicurezza
```

## Regole

- Includi solo le sezioni con contenuto effettivo
- Descrizioni al passato, terza persona: "Aggiunge X", non "Aggiungo X"
- Una riga per voce, concisa ma informativa
- Versione in formato semver: MAJOR.MINOR.PATCH
- Data in formato ISO 8601: YYYY-MM-DD
- Non includere dettagli implementativi interni
- Le voci breaking change vanno in `Changed` con prefisso **BREAKING:**
