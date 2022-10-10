import requests


def add_todo(texto):
    url = 'http://localhost/api/todo'
    item = {'texto': texto}
    x = requests.post(url, json = item)


if __name__ == "__main__":
    add_todo("Texto 1")
    add_todo("Texto 2")
    add_todo("Texto 3")

