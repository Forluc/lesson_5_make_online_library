import argparse
import json
import os

from jinja2 import Environment, FileSystemLoader, select_autoescape
from livereload import Server
from more_itertools import chunked


def on_reload(books_descriptions):
    os.makedirs('pages', exist_ok=True)
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml']),
    )
    template = env.get_template('template.html')

    with open(books_descriptions, 'r', encoding='UTF-8') as file:
        books = json.load(file)

    books_number_on_page = 10
    books_by_page = list(chunked(books, books_number_on_page))
    num_pages = len(books_by_page)

    for current_page, books_on_page in enumerate(books_by_page, 1):
        columns_number = 2
        filename = f'pages/index{current_page}.html'
        books_by_columns = list(chunked(books_on_page, columns_number))

        rendered_page = template.render(
            books_by_columns=books_by_columns,
            current_page=current_page,
            num_pages=num_pages,
        )
        with open(filename, 'w', encoding='UTF-8') as file:
            file.write(rendered_page)


def main():
    books_descriptions = os.path.join('media', 'books_descriptions.json')
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-b', '--books_descriptions', help='Путь к файлу с описанием книг',
                        default=books_descriptions)
    args = parser.parse_args()
    books_descriptions = args.books_descriptions

    on_reload(books_descriptions)


if __name__ == '__main__':
    main()
    server = Server()
    server.watch('template.html', main)
    server.serve(root='.')
