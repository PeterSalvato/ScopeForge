Version: 3.0
Protocol: Savepoint Protocol
Maintainer: Peter Salvato
Status: draft

---

# Render Contract Rules

This file defines the structural and symbolic constraints for all PHP files responsible for rendering output in the Savepoint system — including routers and layout files.

All enforcement is static and must be validated by direct inspection or fixture matching.

---

## 🧭 Scope of Enforcement

This contract applies to:
- All files in `/src/Router/`
- All files in `/src/Layout/`

---

## 🔒 Router Requirements

Every Router must:

- Declare at top of file:  
  ```php
  $title = "Page Name";

    Use output buffering for content:

    ob_start();
    // Render content
    $content = ob_get_clean();

    May not assign $content directly with a string (e.g. $content = "<h1>Welcome</h1>";)

    Must not contain Layout::render() calls

    Must not include an <html> tag

    Must not use conditionals, loops, or dynamic logic of any kind

🔒 Layout Requirements

Layout files must:

    Only be resolved via LayoutResolver::resolve()

    Never use logic to decide which layout is chosen

    Never include conditional logic inside layout files

    Only wrap static content produced from routers

    Never perform rendering decisions or data evaluation

📛 Filename Format

All layout filenames must follow the format:

layout.[type].[context].php

Where:

    type = domain (e.g., journal, project, static)

    context = page or use (e.g., index, explainer, gallery)

Example:

layout.journal.index.php
layout.project.gallery.php

No camelCase, PascalCase, underscores, or mixed notation allowed.
🔎 Fixture Reference

See:

    fixtures/router-contract/good.php

    fixtures/router-contract/bad.php

    fixtures/layout-contract/good.php

    fixtures/layout-contract/bad.php

These define the baseline for structure matching.


---
