Version: 3.0
Protocol: Savepoint Protocol
Maintainer: Peter Salvato
Status: draft

---

# Naming Conventions

This document defines the enforced naming patterns for all files, folders, slugs, layouts, and rendered paths in the Savepoint system. These constraints are absolute and apply globally.

---

## 🐍 Kebab-Case Only

All names must use `kebab-case`:
- Lowercase
- Words separated by hyphens (`-`)
- No underscores (`_`)
- No camelCase
- No PascalCase
- No spaces

---

## 📁 Directories

All folder names must be:

- Fully lowercase
- Kebab-case where multi-word
- Human-readable and match their purpose

✅ Correct:
```plaintext
journal/
about/
systems/savepoint-validator/

❌ Incorrect:

SavepointValidator/
savepoint_validator/
SavepointValidator/

📄 Files

All file names must:

    Use kebab-case (unless standard file like index.html)

    Be lowercase

    Never use underscores or camelCase

    Use only .php, .md, .html, .yaml where applicable

✅ Correct:

contact-submit.php
layout.static.php
instructions-gpt-validator.md

❌ Incorrect:

ContactSubmit.php
layout_Static.php
InstructionsGPTValidator.md

🧱 Layout Slugs

Layout filenames must follow:

layout.[type].[context].php

Both type and context must be in kebab-case.

✅ Examples:

layout.journal.index.php
layout.project.gallery.php

🔎 Fixture Reference

See:

    fixtures/naming-conventions/good.txt

    fixtures/naming-conventions/bad.txt

These files list folder and filename patterns that comply and violate this rule respectively.


---