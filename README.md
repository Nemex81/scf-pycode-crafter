# scf-pycode-crafter

Pacchetto SCF per progetti Python — ottimizza Copilot Agent mode con agenti, skill e instruction dedicati allo sviluppo Python professionale.

## Contenuto

Questo pacchetto installa nella cartella `.github/` del tuo workspace:

- **Agenti:** Analyze, Code, CodeRouter, Design, Docs, Git, Helper, Orchestrator, Plan, Release, Validate
- **Skill:** (in definizione)
- **Instruction:** (in definizione)
- **Prompt:** (in definizione)

## Installazione

Tramite il server MCP `spark-framework-engine`:

```
scf_install_package("scf-pycode-crafter")
```

Oppure manualmente: copia la cartella `.github/` di questo repo nella root del tuo progetto Python.

## Compatibilità

- `spark-framework-engine` >= 1.2.0
- Python >= 3.10
- VS Code con GitHub Copilot

## Manifest Pacchetto

Il pacchetto usa `package-manifest.json` schema `2.0` con metadati espliciti per
compatibilita motore, dipendenze dichiarative e ownership dei file.

## Convenzione Changelog

Il changelog canonico del pacchetto e:

`.github/changelogs/scf-pycode-crafter.md`

Il motore deve leggere il path dichiarato nel campo `changelog_path` del manifest
del pacchetto, senza reintrodurre `FRAMEWORK_CHANGELOG.md` come riferimento canonico.

---

*SPARK Code Framework — pacchetto dominio Python*
