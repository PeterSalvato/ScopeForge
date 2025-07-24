Version: 3.0
Protocol: Savepoint Protocol
Maintainer: Peter Salvato
Status: draft

---

# Validator Index

This document provides a human-readable table of contents for the Savepoint Validator enforcement suite. It includes direct references to all protocol documents, their rule domains, and associated fixtures.

---

## 📚 Spec Files

| File                          | Purpose                                     |
|-------------------------------|---------------------------------------------|
| `VALIDATOR-PROTOCOL.md`       | Index of all enforced domains               |
| `render-contract.md`          | Rules for layout and router rendering       |
| `naming-conventions.md`       | Rules for filenames and directory slugs     |
| `symbolic-constraints.md`     | Logic, branching, and generation prohibitions |
| `savepoint-instructions.md`   | Syntax rules for Savepoint blocks           |
| `seo-and-semantics.md`        | Semantic and metadata validation            |
| `instructions-gpt-validator.md` | GPT config and role enforcement           |
| `file-structure-guide.md`     | Expected project layout structure           |
| `site-manifest.yaml`          | Content map and validator targeting         |
| `.rules-in-draft.md`          | Experimental rule staging area              |
| `glossary.md`                 | Canonical definitions and terms             |

---

## 🧪 Fixture Folders

| Path                                      | Linked Rule Domain              |
|-------------------------------------------|----------------------------------|
| `fixtures/meta-opengraph/`                | SEO & Semantics                 |
| `fixtures/jsonld-home/`                   | SEO & Semantics                 |
| `fixtures/data-attributes/`               | SEO & Semantics                 |
| `fixtures/router-contract/`               | Render Contract                 |
| `fixtures/layout-contract/`               | Render Contract / Constraints   |
| `fixtures/savepoint-blocks/`              | Savepoint Syntax                |
| `fixtures/naming-conventions/`            | Naming Rules                    |
| `fixtures/symbolic-violations/`           | Symbolic Logic Ban              |
| `fixtures/gpt-instructions/`              | GPT Validator Memory Alignment  |

---

## 🔎 How to Traverse

Every rule is defined declaratively in its corresponding `.md` file.  
Every enforcement case has `good.*` and `bad.*` examples in `fixtures/`.

The validator reads this structure only. No rules are inferred.  
No logic is computed. All behavior is derived from authored files.

---
