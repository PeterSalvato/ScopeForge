# generate_prompt.py
import os
import json
import argparse

def load_config(config_path):
    if not os.path.exists(config_path):
        return None
    with open(config_path, 'r') as f:
        return json.load(f)

def load_markdown_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def collect_notes(notes_dir, config):
    if config and 'order' in config:
        files = config['order']
    else:
        files = sorted([f for f in os.listdir(notes_dir) if f.endswith('.md')])
    return [(f, load_markdown_file(os.path.join(notes_dir, f))) for f in files]

def format_prompt(index_summary, notes):
    prompt = ["[MODEL CONTEXT PROTOCOL]"]
    prompt.append("\n:: OVERVIEW ::\n" + index_summary.strip())

    for filename, content in notes:
        section_name = os.path.splitext(filename)[0].replace('_', ' ').replace('-', ' ').title()
        prompt.append(f"\n:: {section_name} ::\n{content.strip()}")

    prompt.append("\n:: END OF CONTEXT ::")
    return "\n".join(prompt)

def main():
    parser = argparse.ArgumentParser(description="Generate structured LLM prompt from atomic notes.")
    parser.add_argument('--notes', default='notes', help='Directory containing atomic markdown notes')
    parser.add_argument('--index', default='index.md', help='Index or overview markdown file')
    parser.add_argument('--config', default='mcp.config.json', help='Optional config file for ordering')
    args = parser.parse_args()

    config = load_config(args.config)
    index_summary = load_markdown_file(args.index)
    notes = collect_notes(args.notes, config)
    prompt = format_prompt(index_summary, notes)

    print(prompt)

if __name__ == "__main__":
    main()
