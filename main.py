import json
import os

from livereload import Server, shell

from jinja2 import Environment, FileSystemLoader, select_autoescape
from more_itertools import chunked

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

os.makedirs(name='pages', exist_ok=True)

with open('files/books_descriptions.json', 'r', encoding='UTF-8') as file:
    books = file.read()
books = json.loads(books)

start = 0
for end in range(10, len(books), 10):
    rendered_page = template.render(
        books=list(chunked(books[start:end], 2)),
        pages=[1, 2, 3, 4, 5, 6, 7]
    )
    with open(f'pages/index_{start}-{end}.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)
    start = end

server = Server()
server.watch('pages/*.html')
server.serve(root='.')
