import json
import datetime
import typer
from pathlib import Path
from scopeforge.utils import load_scopeforge_config, load_notes_config, load_markdown_file, collect_notes, format_context_string, estimate_tokens

prompt_app = typer.Typer()

@prompt_app.command('generate')
def generate(output: typer.FileTextWrite = typer.Option('-', help='Output file (JSON)')):
    """Generate prompt JSON from notes and index"""
    settings = load_scopeforge_config()
    notes_cfg = load_notes_config()
    index_content = load_markdown_file(Path(settings['index_file']))
    notes = collect_notes(settings['notes_path'], notes_cfg)
    context_str = format_context_string(index_content, notes)
    prompt_obj = {
        'prompt': {
            'system': settings['system'],
            'user': settings['user'],
            'context_string': context_str
        },
        'source': {
            'project': settings['project'],
            'index': {'content': index_content},
            'notes': [{'slug': n['slug'], 'content': n['content']} for n in notes],
            'order': notes_cfg.get('order', [])
        },
        'meta': {
            'generated_at': datetime.datetime.utcnow().isoformat() + 'Z',
            'tool_version': '0.1.0',
            'token_estimate': estimate_tokens(context_str)
        }
    }
    json.dump(prompt_obj, output, indent=4)

@prompt_app.command('render')
def render(input_file: typer.FileTextRead = typer.Argument(...), markdown: bool = False):
    """Render context_string from a prompt JSON file"""
    data = json.load(input_file)
    ctx = data['prompt']['context_string']
    if markdown:
        typer.echo('# MCP Context\n' + ctx)
    else:
        typer.echo(ctx)
