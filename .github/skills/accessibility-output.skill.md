---
name: accessibility-output
package: scf-pycode-crafter
version: 1.2.1
description: >
  Standard di output per tutti gli agenti del framework.
  Garantisce che ogni risposta sia navigabile da tastiera e
  compatibile con screen reader (NVDA su Windows 11).
  Richiamabile da tutti gli agenti del framework.
spark: true
---

# Skill: Accessibility Output

## Regola fondamentale

Ogni output testuale prodotto da un agente deve essere navigabile
con screen reader (NVDA su Windows 11). Utile in ambienti dove
l'utente utilizza tecnologie assistive.

## Struttura output obbligatoria

- Header gerarchici Markdown (`##`, `###`) per ogni sezione
- Liste puntate per enumerazioni, mai paragrafi densi non strutturati
- Nessuna tabella complessa: usa liste o coppie chiave-valore
- Nessuna emoji decorativa o ASCII art
- Blocchi di codice sempre in fenced code block con language tag

## Feedback strutturato (standard per tutte le risposte operative)

Ogni risposta che propone modifiche deve seguire questo schema:

```
1. Cosa cambia: <file + righe coinvolte>
2. Perché: <motivazione tecnica>
3. Impatto docs: <file di documentazione da aggiornare, se presenti>
```

## Formato report di completamento

Ogni agente al termine del suo task deve produrre un report così strutturato:

```
TASK COMPLETATO
────────────────────────────────────────
Agente: <Agent-Name>
File modificati: <lista>
Gate superati: <lista>
Prossimo agente: <Agent-Name> oppure "Azione utente richiesta"
────────────────────────────────────────
```
