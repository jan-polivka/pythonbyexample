import os
import pathlib
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

from jinja2 import Environment, FileSystemLoader, select_autoescape
env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape()
)

examples_path = pathlib.Path('examples/')
output_path = pathlib.Path('docs/')

files = os.listdir(examples_path)

css_style = 'default'

with open(examples_path.joinpath("examples.txt")) as f:
    example_names = f.read().split("\n")
    example_mapping = [{name: name.replace(" ", "-").lower()} for name in example_names]

with open(output_path.joinpath("index.html"), 'w') as f:
    template=env.get_template("conversion/template_index.html")
    f.write(template.render(examples=example_mapping))


for file in files:
    if file.endswith('.py'):
        file_path = examples_path.joinpath(file)
        with open(file_path) as f:
            formatted_example = []
            code = f.read()
            split_code = code.split("\n")
            for line in split_code:
                if line.startswith('# '):
                    formatted_example.append(line.replace('# ','')+'\n')
                else:
                    if (len(line.strip()) > 0):
                        formatted_example.append(highlight(line+'\n', PythonLexer(), HtmlFormatter(style=css_style)))
                    else:
                        formatted_example.append('<br/>\n')
            
            html_path = output_path.joinpath(file_path.name.replace(".py", ".html"))
            ready_example = ''.join(formatted_example)
            with open(html_path, 'w') as f:
                template=env.get_template("conversion/template.html")
                f.write(template.render(body=ready_example))

    

with open(output_path.joinpath("styles.css"), "w") as f:
    f.write(HtmlFormatter(style=css_style).get_style_defs('.highlight'))
    