import json
from livereload import Server, shell

from jinja2 import Environment, FileSystemLoader, select_autoescape
from more_itertools import chunked

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

with open('files/books_descriptions.json', 'r', encoding='UTF-8') as file:
    books = file.read()
books = json.loads(books)

rendered_page = template.render(
    books=list(chunked(books, 2)),
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = Server()
server.watch('index.html', shell('index html'))
server.serve(root='.')
