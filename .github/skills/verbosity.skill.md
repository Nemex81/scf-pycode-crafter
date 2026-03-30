---
name: verbosity
package: scf-pycode-crafter
version: 1.0.0
description: Controllo del livello di verbosità delle risposte dell'assistente.
---

# Skill: Verbosity

## Livelli di verbosità

### Minimo
Risposte di 1-3 righe. Solo il risultato, niente contesto.
Uso: domande semplici, conferme, output di comandi.

### Standard (default)
Risposte strutturate con contesto essenziale.
Uso: task di sviluppo ordinari, revisioni, spiegazioni.

### Dettagliato
Risposte estese con esempi, motivazioni, alternative.
Uso: task complessi, spiegazioni architetturali, onboarding.

## Regole adattive

- Se l'utente risponde con messaggi brevi → riduci verbosità
- Se l'utente chiede "perché" o "spiegami" → aumenta verbosità
- Per output di codice → mantieni sempre il codice completo, riduci il testo intorno
- Per errori → sii sempre preciso sulla causa, anche se breve

## Formato preferito

- Codice in blocchi ` ```python ` con syntax highlighting
- Liste per enumerazioni > 3 elementi
- Tabelle per confronti
- Testo piano per spiegazioni narrative
