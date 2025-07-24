import typer
import json
from pathlib import Path

config_app = typer.Typer()

@config_app.command('init')
def init():
    """Interactive init for scopeforge.json"""
    import inquirer
    questions = [
        inquirer.Text('project', message='Project name'),
        inquirer.Text('system', message='System prompt', default='You are an assistant supporting development of an enterprise software project. Prioritize alignment with architectural patterns and developer-written constraints.'),
        inquirer.Text('user', message='User prompt', default='Use the provided context to generate accurate, implementation-ready responses.'),
        inquirer.Text('notes_path', message='Notes directory', default='notes'),
        inquirer.Text('index_file', message='Index file', default='index.md'),
        inquirer.Text('config_file', message='Notes config file', default='notes.config.json'),
        inquirer.Text('authors', message='Authors (comma separated)'),
        inquirer.Text('types', message='Note types (comma separated)')
    ]
    answers = inquirer.prompt(questions)
    answers['authors'] = [a.strip() for a in answers['authors'].split(',')]
    answers['types'] = [t.strip() for t in answers['types'].split(',')]
    with open('scopeforge.json', 'w') as f:
        json.dump(answers, f, indent=4)
    typer.secho('Created scopeforge.json', fg=typer.colors.GREEN)

@config_app.command('validate')
def validate():
    """Validate config files"""
    settings = json.loads(Path('scopeforge.json').read_text())
    notes_cfg = json.loads(Path(settings['config_file']).read_text())
    typer.secho('Configuration is valid.', fg=typer.colors.GREEN)
