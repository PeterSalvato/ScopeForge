Version: 3.0
Protocol: Savepoint Protocol
Maintainer: Peter Salvato
Status: draft

---

# Savepoint Instructions

This document defines the required syntax for Savepoint blocks when used in journal entries or system documentation.

These blocks are symbolic metadata and must be statically authored, structurally correct, and isolated from logic.

---

## ✅ Format

A Savepoint must be:

- A single, self-closing XML-like tag  
- Written as `<Savepoint ... />`  
- Not wrapped in markdown, JSON, or prose  
- One line only (no multiline formatting)

---

## ✅ Required Fields

Each Savepoint **must** include:

- `protocol_version` (literal string, must be `3.0`)
- `category` (human-readable category, lowercase kebab-case)
- `function` (descriptive function name, lowercase kebab-case)
- `timestamp` (ISO 8601 full datetime string)

Example:

```plaintext
<Savepoint protocol_version="3.0" category="semantic-alignment" function="journal-trace" timestamp="2025-05-01T14:36:00Z" />

❌ Forbidden in Savepoints

    No emojis

    No markdown syntax

    No smart quotes or curly quotes

    No <savepoint> lowercase or other case variants

    No partial syntax (e.g., <Savepoint 14:03>)

    No inline Savepoints inside prose

🔒 Symbolic Purpose

Savepoints are used to:

    Mark transitions in journal entries

    Signal structure without introducing logic

    Act as statically detectable symbolic anchors

They are not part of runtime enforcement or parsing.
They exist for authorship integrity and symbolic tracking.
📎 Clarification

This validator enforces Savepoint syntax only.
It does not require the use of Savepoints in any content.
It only ensures that if they are used, they are valid.
🔎 Fixture Reference

See:

    fixtures/savepoint-blocks/good.txt

    fixtures/savepoint-blocks/bad.txt


---