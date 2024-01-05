import os
import pathlib
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

from jinja2 import Environment, FileSystemLoader, select_autoescape
print(os.getcwd())
env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape()
)

examples_path = pathlib.Path('examples/')

files = os.listdir(examples_path)

css_style = 'default'

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
            
            html_path = str(file_path).replace(".py", ".html")
            ready_example = ''.join(formatted_example)
            with open(html_path, 'w') as f:
                template=env.get_template("conversion/template.html")
                f.write(template.render(body=ready_example))

    

with open(examples_path.joinpath("styles.css"), "w") as f:
    f.write(HtmlFormatter(style=css_style).get_style_defs('.highlight'))
    