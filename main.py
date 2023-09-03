import logging
import json
import os
from pathlib import Path
from jinja2 import Environment, FileSystemLoader, select_autoescape
from livereload import Server
from more_itertools import chunked


def on_reload():
    os.makedirs('docs', exist_ok=True)
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml']),
    )
    template = env.get_template('template.html')
    books_file = os.path.join('static', 'books_descriptions.json')
    with open(books_file, 'r', encoding='UTF-8') as file:
        books = json.loads(file.read())

    books_by_page = list(chunked(books, 10))
    num_pages = len(books_by_page)

    for current_page, books_on_page in enumerate(books_by_page, 1):
        filename = f'docs/index{current_page}.html'
        books_by_columns = list(chunked(books_on_page, 2))

        rendered_page = template.render(
            books_by_columns=books_by_columns,
            current_page=current_page,
            num_pages=num_pages,
        )
        with open(filename, 'w', encoding="UTF-8") as file:
            file.write(rendered_page)


def main():
    on_reload()

    server = Server()
    server.watch('template.html', on_reload)
    server.serve(root='.', default_filename='docs/index.html')


if __name__ == '__main__':
    main()
