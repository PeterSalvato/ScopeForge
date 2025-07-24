import os
import json
import datetime
import pathlib
import typer
from pathlib import Path

def load_scopeforge_config():
    config_path = Path('scopeforge.json')
    if not config_path.exists():
        typer.secho('scopeforge.json not found. Run `scopeforge config init`.', fg=typer.colors.RED)
        raise typer.Exit(code=1)
    return json.loads(config_path.read_text())

def load_notes_config():
    config_path = Path(load_scopeforge_config()['config_file'])
    if not config_path.exists():
        typer.secho(f"{config_path} not found.", fg=typer.colors.RED)
        raise typer.Exit(code=1)
    return json.loads(config_path.read_text())

def slugify(text: str) -> str:
    text = text.replace(' ', '')
    return ''.join(e for e in text if e.isalnum())

def load_markdown_file(path: Path) -> str:
    return path.read_text(encoding='utf-8')

def collect_notes(notes_dir: str, notes_config):
    dir_path = Path(notes_dir)
    if notes_config and 'order' in notes_config:
        files = notes_config['order']
    else:
        files = sorted([f.name for f in dir_path.glob('*.md')])
    notes = []
    for fname in files:
        path = dir_path / fname
        if path.exists():
            content = load_markdown_file(path)
            notes.append({
                'slug': fname.replace('.md',''),
                'content': content
            })
    return notes

def format_context_string(index_content: str, notes: list) -> str:
    parts = ['[MODEL CONTEXT PROTOCOL]']
    parts.append(':: MCP OVERVIEW ::')
    parts.append(index_content.strip())
    for note in notes:
        header = note['slug']
        parts.append(f":: {header.upper()} ::")
        parts.append(note['content'].strip())
    parts.append(':: END OF CONTEXT ::')
    return '\n'.join(parts)

def estimate_tokens(text: str) -> int:
    # crude estimation: 1 token per 4 chars
    return len(text) // 4

