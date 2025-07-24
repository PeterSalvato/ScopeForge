Version: 3.0
Protocol: Savepoint Protocol
Maintainer: Peter Salvato
Status: draft

---

# File Structure Guide

This document describes the required structure of the project repository, including enforced directories, placement of content, and layout of validator files.

All file locations must be static, authored, and match this guide exactly.

---

## 🗂 Required Top-Level Directories

```plaintext
/
├── src/
├── public/
├── docs/
├── scripts/
├── vendor/

📁 /src/ — PHP Source

    Router/ → All route files (e.g. about.php, journal-entry.php)

    Layout/ → All layout files (e.g. layout.journal.index.php)

    Partials/ → Head, footer, nav components

    Projects/ → Project content (e.g. SavepointProtocol/)

    Utils/ → Helpers (e.g. Loader.php)

    Journal/ → Journal entries (subfolders for each post)

📁 /public/ — HTML Output & Assets

    index.php → public entry point

    assets/ → images/, stylesheets/, js/

    Any .html pages exported here must match site-manifest.yaml

📁 /docs/ — Validator & Protocol Files

    validator/ → All rule files, fixtures, and metadata

        *.md → Rule definitions

        site-manifest.yaml → Declared route structure and rule scope

        fixtures/ → good.* / bad.* test files by rule

    Other Markdown documentation allowed (e.g., README.md)

📁 /scripts/ — Build & Validation Scripts

    verify/ → GPT and shell validation calls

    cleanup/ → Standardization passes

    journal/, projects/ → System-specific scaffold tools

✅ Required Files

    bootstrap.sh → Environment setup

    validate-validator-structure.sh → Validator integrity self-test

    servesite.sh → Local preview

    composer.json / vendor/ → PHP dependency management

🔐 Ruleset Enforcement

Each path in this structure is monitored by one or more rulesets. See:

    site-manifest.yaml → ruleset_dependencies block

    VALIDATOR-PROTOCOL.md → Index of enforcement domains


---