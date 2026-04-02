---
name: validate-accessibility
package: scf-pycode-crafter
version: 2.0.0
description: >
  Checklist accessibilità per componenti UI Python.
  Copre wxPython e altri toolkit grafici Python.
  Richiamabile da py-Agent-Validate e py-Agent-Code per verificare
  che ogni componente UI sia navigabile da tastiera e compatibile
  con screen reader (NVDA su Windows 11).
---

# Skill: Validate Accessibility

## Principi generali di accessibilità UI Python

Per qualsiasi toolkit UI Python (wxPython, tkinter, PyQt, PySide):

- Ogni controllo interattivo deve avere un label testuale esplicito
- La navigazione da tastiera deve seguire un ordine logico (TAB order)
- Nessun feedback esclusivamente visivo: ogni stato deve avere alternativa testuale
- I dialog devono avere focus sul primo controllo logico all'apertura
- ESC deve chiudere dialog senza effetti collaterali

## Checklist wxPython

Per ogni dialog, panel o controllo wxPython verifica:

- [ ] `SetLabel()` con testo descrittivo e non ambiguo
- [ ] Bottoni critici con acceleratori tastiera (`&OK`, `&Annulla`)
- [ ] `SetTitle()` semantico sul dialog/frame
- [ ] `SetFocus()` impostato sul primo controllo logico all'apertura
- [ ] `ESC` chiude il dialog senza effetti collaterali
- [ ] `TAB` naviga i controlli in ordine logico (usa `MoveAfterInTabOrder` se necessario)
- [ ] Nessun feedback visivo esclusivo (colore, icona) senza alternativa testuale

## Requisiti NVDA su Windows 11

- Evitare aggiornamenti dinamici silenziosi: usare `wx.PostEvent` o
  `AccessibleDescription` per notificare cambiamenti di stato
- Label su tutti i controlli anche se visivamente ovvi
- No testo in immagini o icone senza equivalente testuale

## Output atteso

Report strutturato:
```
Componente: <NomeClasse>
Checklist: [N/7] voci OK
Issues: <lista problemi rilevati o "nessuno">
Stato: PASS / FAIL
```
