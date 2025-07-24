Version: 3.0
Protocol: Savepoint Protocol
Maintainer: Peter Salvato
Status: draft

---

# Glossary of Symbolic Terms

This document defines canonical terms used throughout the Savepoint Validator system. These definitions are frozen, literal, and deterministic.

---

## Symbolic Authoring  
Content is composed by explicit human authorship.  
It is not generated, inferred, or computed.  
No runtime logic may affect authored structure.

---

## Deterministic Publishing  
Every page, route, and structure is statically declared and validated.  
Behavior is fully knowable from authored files.  
There is no dynamic behavior at render or runtime.

---

## Fixture  
A file that demonstrates correct or incorrect structure.  
All fixtures live in `/docs/validator/fixtures/`.  
Each fixture pair (`good.*`, `bad.*`) defines the boundaries of a rule.

---

## Enforcement Domain  
A symbolic category of rules (e.g., layout, naming, SEO)  
Each domain has:
- A markdown rule file  
- One or more fixture folders  
- Coverage in `VALIDATOR-PROTOCOL.md`

---

## Self-Validating Validator  
The validator must check its own memory and instruction set against `instructions-gpt-validator.md` before enforcing any rules.  
Any misalignment invalidates the validation session.

---

## Savepoint  
A plaintext, declarative, self-closing metadata block used in journals and semantic artifacts.  
While Savepoint format is enforced, Savepoints themselves are **not** required in validator specs.

---

## Semantic-Packing  
The inclusion of structured metadata (e.g., OpenGraph, JSON-LD, Microformats2) in content files.  
Semantic-packing enables indexing, interoperability, and discoverability.

---

## Structural Drift  
Any deviation from the frozen architectural model defined in `/docs/validator/`  
The validator exists to detect and halt such drift before it spreads.

---

## Violations  
Symbolic violations are always output in the form:

```plaintext
- [VIOLATION] <description>

No markdown, no emoji, no speculative commentary.


---