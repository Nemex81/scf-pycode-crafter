# CHANGELOG — scf-pycode-crafter

## [1.1.0] — 2026-04-01

### Breaking Changes

- Tutti gli agenti rinominati con prefisso `py-` per namespace plugin in ecosistemi SCF multi-plugin.
  Riferimenti a `Agent-Code`, `Agent-Plan`, `Agent-Validate`, ecc. vanno aggiornati a
  `py-Agent-Code`, `py-Agent-Plan`, `py-Agent-Validate`, ecc.

### Modificato

- Rinominati 11 file agente da `Agent-Xxx.md` a `py-Agent-Xxx.md`
- Aggiornato campo `name:` nel frontmatter di ciascun agente
- Aggiornato `AGENTS.md` con i nuovi nomi nella tabella indice
- Aggiornate skill `agent-selector`, `code-routing`, `framework-index`, `validate-accessibility`
- Aggiornato `package-manifest.json` con i nuovi path agenti

---

## [1.0.1] — 2026-03-31

### Manutenzione

- Rimosso `.github/FRAMEWORK_CHANGELOG.md` (legacy redirect).
  Il changelog canonico e esclusivamente questo file.
  Richiede spark-framework-engine >= 1.2.1.

### Infrastruttura

- Aggiunto `.github/workflows/sync-registry.yml`: workflow GitHub Actions che sincronizza
  automaticamente `scf-registry/registry.json` ad ogni push su `main` che modifica
  `package-manifest.json`. Apre una PR automatica sul registry con `latest_version` e
  `engine_min_version` aggiornati dai valori del manifest (fonte canonica).
  Prerequisito operativo: secret `REGISTRY_WRITE_TOKEN` configurato nel repo.

## [1.0.0] — 2026-03-30

### Prima release pubblica

- Pacchetto SCF iniziale per progetti Python.
- 11 agenti specializzati: Analyze, Code, CodeRouter, Design, Docs, Git, Helper, Orchestrator, Plan, Release, Validate.
- 26 skill operative: accessibilità, architettura pulita, changelog, commit convenzionali, documentazione, error recovery, framework guard, git, profilo progetto, rollback, semantic gate, semver, stile, test, verbosità.
- 10 instruction files: framework-guard, git-policy, model-policy, personality, project-reset, python, tests, verbosity, workflow-standard.
- Compatibile con spark-framework-engine >= 1.2.0.
