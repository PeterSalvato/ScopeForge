Version: 3.0
Protocol: Savepoint Protocol
Maintainer: Peter Salvato
Status: draft

---

# Symbolic Constraints

This document enforces the fundamental constraint of symbolic authorship:  
**no logic, no computation, no generation.**

All files must be authored as declarative content.  
No runtime decision-making or conditional logic is permitted in any renderer or layout.

---

## 🚫 Forbidden Constructs

These must never appear in any router, layout, or content file:

- `if`, `else`, `elseif`
- `switch`, `case`
- `for`, `foreach`, `while`, `do`
- `rand()`, `date()`, `$_SERVER`, `isset()`, `empty()`, `count()`
- Any function call that varies output based on runtime state

---

## 🚫 Forbidden Patterns

Examples that will trigger `[VIOLATION]`:

```php
if ($isAdmin) { echo "Welcome"; }           // ❌ logic
foreach ($posts as $post) { echo $post; }   // ❌ loop
$content = generateContent();               // ❌ function call with hidden logic

✅ Allowed Patterns

$title = "Systems Overview";                // ✅ constant assignment
ob_start();                                 // ✅ declarative buffering
$content = ob_get_clean();                  // ✅ deterministic capture

Only static authoring is permitted.
The validator must be able to read and verify all structure from file contents without evaluation.
📍 Enforced Locations

This applies to:

    All files in /src/Router/

    All files in /src/Layout/

    Any custom layout logic in /src/Utils/

    Any embedded render content in *.php

📎 Related Rule: Render Contract

The render-contract.md file enforces required symbols.
This file forbids dynamic symbols.

Together, they define a safe render domain.
🔎 Fixture Reference

See:

    fixtures/symbolic-violations/good.php

    fixtures/symbolic-violations/bad.php

These demonstrate a compliant symbolic file and a logic-violating example.