# ScopeForge

**ScopeForge** is a Python CLI that compiles a directory of human‑authored Markdown notes into a scoped, structured JSON payload ready for LLM context injection. It helps teams turn documented project knowledge into machine‑usable prompts.

---

## 🧠 What It Does

- Reads your `index.md` overview plus atomic notes from `notes/`
- Validates and orders them according to `notes.config.json`
- Outputs a JSON object with:
  - `prompt` (system, user, context_string)
  - `source` (project, index, notes, order)
  - `meta` (generated_at, tool_version, token_estimate)
- Renders just the `context_string` for manual copy‑paste if needed

---

## 🔧 Installation

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

🚀 Quickstart

    Initialize your project (creates scopeforge.json):

scopeforge config init

Validate your configs:

scopeforge config validate

Create a new atomic note:

scopeforge note create

List all notes:

scopeforge note list

Generate your LLM prompt JSON:

scopeforge prompt generate > context.json

Render the flattened context for copy‑paste:

    scopeforge prompt render context.json
    scopeforge prompt render context.json --markdown

📁 Project Layout

ScopeForge/
├── scopeforge.json         # Team/project settings
├── notes.config.json       # Note ordering
├── index.md                # High‑level overview
├── notes/                  # Atomic .md notes
│   └── 01_ProjectGoals.md
│   └── 02_Users.md
│   └── ...
├── scopeforge/             # Python CLI package
│   ├── config.py
│   ├── note.py
│   ├── prompt.py
│   ├── utils.py
│   └── main.py
├── pyproject.toml
├── requirements.txt
└── README.md

📦 Example Output (context.json)

{
  "prompt": {
    "system": "You are an assistant supporting development of an enterprise CRM product. Prioritize alignment with architectural patterns and developer-written constraints.",
    "user": "Use the following curated context to generate accurate responses.",
    "context_string": "[MODEL CONTEXT PROTOCOL]\n:: MCP OVERVIEW ::\n...\n:: PROJECTGOALS ::\n...\n:: END OF CONTEXT ::"
  },
  "source": {
    "project": "EnterpriseCRM",
    "index": { "content": "..." },
    "notes": [
      { "slug": "ProjectGoals", "content": "..." },
      { "slug": "Users", "content": "..." }
    ],
    "order": ["01_ProjectGoals.md", "02_Users.md"]
  },
  "meta": {
    "generated_at": "2025-07-24T14:00:00Z",
    "tool_version": "0.1.0",
    "token_estimate": 3052
  }
}

🧩 Philosophy

ScopeForge ensures your models operate within real project constraints, not hallucinated defaults. By forging structured context from human‑authored rules, you get:

    Clear epistemic boundaries

    Traceable source meta

    Flexible, machine‑readable format

📜 License

MIT. See LICENSE.md.

© 2025 Peter Salvato. Licensed under CC BY‑NC‑ND 4.0.