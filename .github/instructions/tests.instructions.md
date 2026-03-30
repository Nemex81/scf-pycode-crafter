---
applyTo: "tests/**/*.py"
package: scf-pycode-crafter
version: 1.0.0
---

# Instruction: Tests

Questa instruction si applica a tutti i file in `tests/`.

- Framework: pytest
- Un file di test per ogni modulo sorgente
- Naming test: `test_<cosa>_<condizione>_<risultato_atteso>`
- Usa fixture pytest per setup condiviso
- Isola i test: ogni test deve essere indipendente dagli altri
- Non usare `print()` nei test — usa `logging` o assert
- Mock solo le dipendenze esterne (I/O, rete, DB)
- Non testare implementazioni interne — testa comportamenti osservabili
- Coverage minima logica di business: 70%
