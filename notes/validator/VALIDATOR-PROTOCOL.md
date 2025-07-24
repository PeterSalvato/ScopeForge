Version: 0.1
Maintainer: Peter Salvato
Status: draft

---

# Validator Protocol Index

This document declares the complete set of symbolic, structural, and semantic enforcement domains governed by the Savepoint Validator. Each enforcement domain links to a dedicated rule specification and associated test fixtures.

---

## 🔐 Enforcement Domains

### 1. Render Contract
- Rule file: `render-contract.md`
- Fixture path: `fixtures/router-contract/`, `fixtures/layout-contract/`
- Enforces:  
  - `$title` declaration in all routers  
  - `ob_start()` and `ob_get_clean()` content wrapping  
  - No direct string assignment to `$content`  
  - No `<html>` tags in routers  
  - Layouts must be resolved via `LayoutResolver::resolve()`  
  - Layout filenames must follow `layout.[type].[context].php` format

---

### 2. Naming Conventions
- Rule file: `naming-conventions.md`
- Fixture path: `fixtures/naming-conventions/`
- Enforces:
  - All filenames and paths must use `kebab-case`
  - No PascalCase, camelCase, or underscores allowed
  - Layout slugs must also use kebab-case

---

### 3. Symbolic Constraints
- Rule file: `symbolic-constraints.md`
- Fixture path: `fixtures/symbolic-violations/`
- Enforces:
  - No conditionals: `if`, `else`, `switch`
  - No loops: `for`, `foreach`, `while`
  - No runtime branching or dynamic generation
  - All content must be statically authored

---

### 4. Savepoint Instructions
- Rule file: `savepoint-instructions.md`
- Fixture path: `fixtures/savepoint-blocks/`
- Enforces:
  - All Savepoints must be self-closing  
  - Required fields: `protocol_version`, `category`, `function`, `timestamp`  
  - Timestamp must follow ISO 8601  
  - Content must be plaintext only (no emoji, markdown, smart quotes)

---

### 5. SEO & Semantics
- Rule file: `seo-and-semantics.md`
- Fixture path: `fixtures/meta-opengraph/`, `jsonld-home/`, `data-attributes/`, etc.
- Enforces:
  - Required `<meta>`, OpenGraph, and Twitter tags in `<head>`
  - Proper JSON-LD schemas (`WebSite`, `Article`, `SoftwareApplication`, etc.)
  - ARIA landmarks and Microformats2 classes
  - Sitemap, pagination, RDFa, hreflang, WebMention, oEmbed

---

### 6. GPT Role & Instruction Compliance
- Rule file: `instructions-gpt-validator.md`
- Fixture path: `fixtures/gpt-instructions/`
- Enforces:
  - GPT instruction memory matches this file
  - Self-verification occurs before enforcement
  - Misalignment triggers `[VALIDATOR ALERT]` and aborts

---

### 7. Structural Layout
- Rule file: `file-structure-guide.md`
- Describes:
  - Project folder layout (`/src`, `/docs`, `/public`)
  - Expected location of routers, layouts, journals, and systems
  - Validator files live in `/docs/validator/`

---

## 🛠 Validator Enforcement Toolkit

- `validate-validator-structure.sh` → Verifies this validator system is intact
- Scripts in `/scripts/verify/` should reference validator rules and fixtures directly

---

## 📂 All Rule Definitions Live In:

- Markdown: `*.md` files in `/docs/validator/`
- YAML: `site-manifest.yaml`
- Fixtures: `/docs/validator/fixtures/`

Only these sources may be used for enforcement.

---
