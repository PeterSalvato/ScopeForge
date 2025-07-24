import typer
import os
from pathlib import Path
from scopeforge.utils import load_scopeforge_config, slugify

note_app = typer.Typer()

@note_app.command('create')
def create():
    """Create a new atomic note"""
    settings = load_scopeforge_config()
    notes_dir = Path(settings['notes_path'])
    notes_dir.mkdir(exist_ok=True)
    existing = sorted(notes_dir.glob('*.md'))
    next_num = len(existing) + 1
    title = typer.prompt('Title')
    slug = slugify(title)
    filename = f"{next_num:02d}_{slug}.md"
    filepath = notes_dir / filename
    author = typer.prompt('Author', type=typer.Choice(settings['authors']))
    note_type = typer.prompt('Type', type=typer.Choice(settings['types']))
    tags = typer.prompt('Tags (comma separated)')
    tags_list = [t.strip() for t in tags.split(',')]
    frontmatter = ['---',
                   f'title: {title}',
                   f'slug: {slug}',
                   f'author: {author}',
                   f'type: {note_type}',
                   f'tags: {tags_list}',
                   f'level: Atomic',
                   '---',
                   '']
    filepath.write_text('\n'.join(frontmatter))
    typer.secho(f'Created note: {filepath}', fg=typer.colors.GREEN)
    # open in editor
    editor = os.environ.get('EDITOR', 'nano')
    os.system(f"{editor} {filepath}")

@note_app.command('list')
def list_notes():
    """List all atomic notes"""
    settings = load_scopeforge_config()
    notes_dir = Path(settings['notes_path'])
    files = sorted(notes_dir.glob('*.md'))
    for f in files:
        typer.echo(f.name)

@note_app.command('view')
def view(slug: str):
    """View note content by slug"""
    settings = load_scopeforge_config()
    notes_dir = Path(settings['notes_path'])
    matches = [f for f in notes_dir.glob(f'*{slug}*.md')]
    if not matches:
        typer.secho('Note not found.', fg=typer.colors.RED)
        raise typer.Exit(1)
    typer.echo(matches[0].read_text())

@note_app.command('edit')
def edit(slug: str):
    """Edit note in default editor by slug"""
    settings = load_scopeforge_config()
    notes_dir = Path(settings['notes_path'])
    matches = [f for f in notes_dir.glob(f'*{slug}*.md')]
    if not matches:
        typer.secho('Note not found.', fg=typer.colors.RED)
        raise typer.Exit(1)
    editor = os.environ.get('EDITOR', 'nano')
    os.system(f"{editor} {matches[0]}")
