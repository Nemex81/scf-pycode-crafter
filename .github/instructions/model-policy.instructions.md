---
applyTo: "**"
package: scf-pycode-crafter
version: 1.0.0
---

# Instruction: Model Policy

## Comportamento generale

- Leggi sempre i file esistenti prima di modificarli
- Non assumere il contenuto di un file senza averlo letto
- Non fare refactoring non richiesti durante l'implementazione
- Proponi architettura prima di implementare per task complessi
- Segnala trade-off tecnici quando esistono alternative significative

## Limiti operativi

- Non eliminare file senza conferma esplicita
- Non modificare più di un componente alla volta senza piano condiviso
- Non assumere che i test passino — verificare esplicitamente
- Non cambiare interfacce pubbliche senza valutare l'impatto

## Gestione incertezza

- Se mancano informazioni critiche per completare un task, chiedi prima di agire
- Se esistono più approcci validi, presenta le opzioni con pro/contro
- Se un task sembra ambiguo, chiarisci lo scope prima di iniziare
- Segnala esplicitamente quando qualcosa è fuori dalla tua conoscenza

## Qualità output

- Codice prodotto deve rispettare i quality gate definiti in `semantic-gate`
- Non produrre codice incompleto senza indicarlo esplicitamente con `# TODO:`
- Le funzioni pubbliche devono avere type hints e docstring
