import typer
from scopeforge.config import config_app
from scopeforge.note import note_app
from scopeforge.prompt import prompt_app

app = typer.Typer()
app.add_typer(config_app, name="config")
app.add_typer(note_app, name="note")
app.add_typer(prompt_app, name="prompt")

def main():
    app()

if __name__ == "__main__":
    main()
