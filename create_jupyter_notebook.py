import json
import re

def create_jupyter_notebook(markdown_file, output_file):
    with open(markdown_file, 'r', encoding="utf-8") as file:
        markdown_content = file.read()

    cells = []
    chunks = re.split(r'```python\n(.*?)```', markdown_content, flags=re.DOTALL)

    for i in range(len(chunks)):
        if i % 2 == 0:
            if chunks[i].strip():
                cells.append({
                    'cell_type': 'markdown',
                    'source': chunks[i].strip().split('\n')
                })
        else:
            code_lines = chunks[i].strip().split('\n')
            if any(line.startswith(' ') for line in code_lines):
                cells.append({
                    'cell_type': 'markdown',
                    'source': ['```python\n' + chunks[i].strip() + '\n```']
                })
            else:
                cells.append({
                    'cell_type': 'code',
                    'execution_count': None,
                    'metadata': {},
                    'outputs': [],
                    'source': code_lines
                })

    notebook = {
        'nbformat': 4,
        'nbformat_minor': 0,
        'metadata': {
            'colab': {
                'provenance': []
            },
            'kernelspec': {
                'name': 'python3',
                'display_name': 'Python 3'
            },
            'language_info': {
                'name': 'python'
            }
        },
        'cells': cells
    }

    with open(output_file, 'w') as file:
        json.dump(notebook, file, indent=2)

# 使用例
markdown_file = 'example.md'
output_file = 'example.ipynb'
create_jupyter_notebook(markdown_file, output_file)