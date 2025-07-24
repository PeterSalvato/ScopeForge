# ScopeForge

**ScopeForge** is a CLI tool that compiles a directory of human-authored Markdown rules into scoped, structured JSON suitable for LLM context injection. It is designed to support durable, high-trust AI collaboration by transforming documented project knowledge into machine-usable prompt context.

> Part of the [Model Context Protocol](#) ecosystem.  
> Successor to Validator — hardened for local and agentic use.

---

## 🧠 What It Does

- Traverses a directory of Markdown rule files
- Parses and validates their structure
- Outputs a clean, scannable JSON context object
- Enables LLMs to operate inside your project’s architecture, constraints, and semantics

---

## ✅ Use Cases

- Inject scoped context into a local or hosted LLM session
- Support structured agentic workflows (RAG, CLI copilots, evals)
- Define shared rulesets across design, dev, and product teams
- Enforce architectural boundaries in AI-augmented systems
- Surface codified knowledge without exposing full documentation

---

## 🔧 Example

### Markdown Ruleset (`/rules/components/button.md`)

```markdown
---
id: ui.button
tags: [ui, component, design-system]
title: Button Component
---

### Purpose
Buttons trigger user actions. They must use semantic `<button>` tags and follow accessibility patterns.

### Constraints
- Never use `<div>` for interactive elements.
- Must follow design token system.
- Variants: primary, secondary, destructive.
````

### ScopeForge Output (`context.json`)

```json
{
  "entries": [
    {
      "id": "ui.button",
      "tags": ["ui", "component", "design-system"],
      "title": "Button Component",
      "purpose": "Buttons trigger user actions...",
      "constraints": [
        "Never use <div> for interactive elements.",
        "Must follow design token system.",
        "Variants: primary, secondary, destructive."
      ]
    }
  ]
}
```

---

## 🚀 Quickstart

```bash
# Install (if released as a package)
npm install -g scopeforge

# Compile a Markdown ruleset directory into LLM-usable JSON
scopeforge compile ./rules/ > context.json

# Validate Markdown ruleset structure
scopeforge validate ./rules/

# Extract only entries with specific tags
scopeforge extract --tags ui,accessibility ./rules/
```

---

## 🧱 Project Structure

```
/rules/
├── components/
│   └── button.md
├── tokens/
│   └── colors.md
└── architecture/
    └── layout.md
```

---

## 🧩 Philosophy

**ScopeForge** is built on the idea that AI should not guess.
Structured, human-authored knowledge deserves:

* Epistemic boundaries
* Scoped access
* Machine-readable formatting
* Durable, explainable structure

This tool enables your models to operate inside your system’s **real constraints**—not hallucinated defaults.

---

## 📦 Roadmap

* [ ] Tag-based filtering
* [ ] Output compression (chunked JSON, flat array, etc.)
* [ ] Context previews (markdown → terminal)
* [ ] Plug-ins for prompt injection (OpenAI, Claude, local LLMs)
* [ ] LLM eval harness (with ScopeForge context)

---

## 🧑‍💻 Contributing

This project is under active development. Open to:

* Plugin ideas
* Markdown schema improvements
* LLM-specific context export formats
* Performance tuning and CLI enhancements

---

## 📜 License

MIT or equivalent, to be determined.

---

## 🔗 Related Projects

* [Savepoint.Protocol](#)
* [Validator (legacy precursor)](#)
* [Model Context Protocol](#)

---
---

© 2025 Peter Salvato.  
Licensed under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/).  
Attribution required. No commercial use or redistribution of modified versions permitted.  
See the [LICENSE](./LICENSE) file for details.
