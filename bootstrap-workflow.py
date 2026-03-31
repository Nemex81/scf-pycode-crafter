#!/usr/bin/env python3
"""
Bootstrap script — esegui UNA VOLTA per creare .github/workflows/sync-registry.yml.

Uso: python bootstrap-workflow.py
Poi: elimina questo file e committa .github/workflows/sync-registry.yml

Generato da GitHub Copilot il 2026-03-31.
"""
from pathlib import Path

WORKFLOW_CONTENT = """\
# .github/workflows/sync-registry.yml
# Repo: scf-pycode-crafter
#
# Ogni volta che package-manifest.json cambia su main,
# questo workflow legge i dati dal manifest e apre una PR
# su scf-registry con registry.json aggiornato.
#
# PREREQUISITO: creare il secret REGISTRY_WRITE_TOKEN nel repo
# (PAT con write su Nemex81/scf-registry).

name: Sync registry on manifest change

on:
  push:
    branches: [main]
    paths: [package-manifest.json]

jobs:
  sync:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      # --- 1. Legge i campi dal manifest (mai hardcodati) ---
      - name: Read manifest fields
        id: manifest
        run: |
          echo "pkg_id=$(jq -r '.package' package-manifest.json)" >> $GITHUB_OUTPUT
          echo "version=$(jq -r '.version' package-manifest.json)" >> $GITHUB_OUTPUT
          echo "engine_min=$(jq -r '.min_engine_version' package-manifest.json)" >> $GITHUB_OUTPUT

      # --- 2. Valida che i campi siano presenti e non null ---
      - name: Validate manifest fields
        run: |
          if [ -z "${{ steps.manifest.outputs.pkg_id }}" ] || [ "${{ steps.manifest.outputs.pkg_id }}" = "null" ]; then
            echo "ERROR: Campo 'package' mancante o null in package-manifest.json" >&2
            exit 1
          fi
          if [ -z "${{ steps.manifest.outputs.version }}" ] || [ "${{ steps.manifest.outputs.version }}" = "null" ]; then
            echo "ERROR: Campo 'version' mancante o null in package-manifest.json" >&2
            exit 1
          fi
          if [ -z "${{ steps.manifest.outputs.engine_min }}" ] || [ "${{ steps.manifest.outputs.engine_min }}" = "null" ]; then
            echo "ERROR: Campo 'min_engine_version' mancante o null in package-manifest.json" >&2
            exit 1
          fi
          echo "Manifest OK: pkg=${{ steps.manifest.outputs.pkg_id }} ver=${{ steps.manifest.outputs.version }} engine_min=${{ steps.manifest.outputs.engine_min }}"

      # --- 3. Fa checkout di scf-registry ---
      - name: Checkout scf-registry
        uses: actions/checkout@v4
        with:
          repository: Nemex81/scf-registry
          token: ${{ secrets.REGISTRY_WRITE_TOKEN }}
          path: registry-repo

      # --- 4. Aggiorna registry.json ---
      # Se il pacchetto non viene trovato -> errore esplicito, nessuna scrittura parziale.
      - name: Update registry.json
        run: |
          cd registry-repo
          python3 - <<'EOF'
          import json
          import os
          import sys
          from datetime import datetime, timezone

          with open('registry.json', 'r', encoding='utf-8') as f:
              data = json.load(f)

          pkg_id = os.environ['PKG_ID']
          version = os.environ['VERSION']
          engine_min = os.environ['ENGINE_MIN']

          found = False
          for pkg in data['packages']:
              if pkg.get('id') == pkg_id:
                  pkg['latest_version'] = version
                  pkg['engine_min_version'] = engine_min
                  found = True
                  break

          if not found:
              print(
                  f"ERROR: Pacchetto '{pkg_id}' non trovato in registry.json. "
                  "Aggiungilo manualmente prima di usare questo workflow.",
                  file=sys.stderr,
              )
              sys.exit(1)

          data['updated_at'] = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

          with open('registry.json', 'w', encoding='utf-8') as f:
              json.dump(data, f, indent=2, ensure_ascii=False)
              f.write('\\n')

          print(f"registry.json aggiornato: {pkg_id} -> version={version}, engine_min={engine_min}")
          EOF
        env:
          PKG_ID: ${{ steps.manifest.outputs.pkg_id }}
          VERSION: ${{ steps.manifest.outputs.version }}
          ENGINE_MIN: ${{ steps.manifest.outputs.engine_min }}

      # --- 5. Apre la PR su scf-registry ---
      - name: Open PR on scf-registry
        id: create-pr
        uses: peter-evans/create-pull-request@v6
        with:
          path: registry-repo
          token: ${{ secrets.REGISTRY_WRITE_TOKEN }}
          commit-message: "sync: ${{ steps.manifest.outputs.pkg_id }} -> ${{ steps.manifest.outputs.version }}"
          title: "sync: ${{ steps.manifest.outputs.pkg_id }} ${{ steps.manifest.outputs.version }}"
          body: |
            Aggiornamento automatico generato da `sync-registry.yml` in `${{ github.repository }}`.

            **Pacchetto:** `${{ steps.manifest.outputs.pkg_id }}`
            **Versione:** `${{ steps.manifest.outputs.version }}`
            **Engine min:** `${{ steps.manifest.outputs.engine_min }}`

            Commit di origine: ${{ github.sha }}
          branch: "sync/${{ steps.manifest.outputs.pkg_id }}-${{ steps.manifest.outputs.version }}"
          base: main

      # --- 6. Riporta il risultato in log ---
      - name: Report PR result
        if: steps.create-pr.outputs.pull-request-number
        run: |
          echo "PR creata: #${{ steps.create-pr.outputs.pull-request-number }}"
          echo "URL: ${{ steps.create-pr.outputs.pull-request-url }}"

      # --- 7. Apre un'issue di avviso se il workflow fallisce ---
      # Evita che il registry rimanga silenziosamente stale su token scaduto o errori di rete.
      - name: Notify on failure
        if: failure()
        uses: actions/github-script@v7
        with:
          script: |
            await github.rest.issues.create({
              owner: context.repo.owner,
              repo: context.repo.repo,
              title: `⚠️ sync-registry.yml fallito — ${context.sha.substring(0, 7)}`,
              body: [
                `Il workflow \\`sync-registry.yml\\` ha fallito per il commit ${context.sha}.`,
                ``,
                `**Pacchetto:** \\`${{ steps.manifest.outputs.pkg_id }}\\``,
                `**Versione tentata:** \\`${{ steps.manifest.outputs.version }}\\``,
                ``,
                `Controlla il log del workflow: ${context.serverUrl}/${context.repo.owner}/${context.repo.repo}/actions/runs/${context.runId}`,
                ``,
                `Azione richiesta: verifica il secret \\`REGISTRY_WRITE_TOKEN\\` e il file \\`registry.json\\` su scf-registry.`
              ].join('\\n'),
              labels: ['bug', 'automation']
            })
"""

def main() -> None:
    repo_root = Path(__file__).parent
    workflows_dir = repo_root / ".github" / "workflows"
    workflow_file = workflows_dir / "sync-registry.yml"

    workflows_dir.mkdir(parents=True, exist_ok=True)
    workflow_file.write_text(WORKFLOW_CONTENT, encoding="utf-8")

    print(f"✅ Creato: {workflow_file}")
    print()
    print("Prossimi passi:")
    print("  1. Verifica il file .github/workflows/sync-registry.yml")
    print("  2. Elimina questo file (bootstrap-workflow.py)")
    print("  3. git add .github/workflows/sync-registry.yml")
    print("  4. git commit -m 'feat: aggiungi workflow sync-registry.yml automatico'")
    print("  5. git push")
    print()
    print("PREREQUISITO: crea il secret REGISTRY_WRITE_TOKEN nelle impostazioni GitHub del repo")
    print("  Settings -> Secrets and variables -> Actions -> New repository secret")
    print("  Nome: REGISTRY_WRITE_TOKEN")
    print("  Valore: PAT con write su Nemex81/scf-registry")


if __name__ == "__main__":
    main()
