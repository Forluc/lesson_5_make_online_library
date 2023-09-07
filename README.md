# Сайт онлайн-библиотеки

Можно ознакомиться по [ссылке](https://forluc.github.io/lesson_5_make_online_library/)
![gh_pages](https://github.com/Forluc/lesson_5_make_online_library/assets/75582238/e2172a7d-d689-453b-9b76-feacebdc9a8e)

## Окружение

### Требования к установке

Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки
зависимостей:

```bash
pip install -r requirements.txt
``` 

## Запуск скрипта для запуска сервера по адресу http://127.0.0.1:5500 и создания ссылок(index-файлов в папке docs)

Запуск на Linux(Python 3) или Windows:

В файле static/books_descriptiions.json добавить(убрать) нужные книги. Книги добавить в static/books. Картинки добавить в static/images. 

Можно воспользоваться [парсером](https://github.com/Forluc/lesson_3_books-library-restyle).

```bash
$ python main.py
```

### Цель проекта

Скрипт написан в образовательных целях на онлайн-курсе [Devman](dvmn.org)
