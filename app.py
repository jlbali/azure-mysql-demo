from flask import Flask, request
import json
from db import delete_todo, get_todo, get_todos, add_todo, update_todo, commit, rollback

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hola Mundo Containerizado!'

# Ruta para devolver todos los ToDos.
@app.route('/api/todos', methods=['GET'])
def api_get_todos():
    items = get_todos()
    return json.dumps([item.as_dict() for item in items])

# Ruta para devolver un Todo en particular en función de un id..
@app.route('/api/todo/:id', methods=['GET'])
def api_get_todo(id):
    item = get_todo(id)
    return item.as_json()

# Ruta para agregar un Todo.
@app.route('/api/todo', methods=['POST'])
def api_add_todo():
    request_data = request.get_json()
    texto = request_data["texto"]
    item = add_todo(texto)
    commit()
    return item.as_json()

# Ruta para modificar un Todo.
@app.route('/api/todo/:id', methods=['PUT'])
def api_update_todo(id):
    request_data = request.get_json()
    texto = request_data["texto"]
    item = update_todo(id, texto)
    commit()
    return item.as_json()

# Ruta para eliminar un Todo.
@app.route('/api/todo/:id', methods=['DELETE'])
def api_delete_todo(id):
    delete_todo(id)
    commit()
    return json.dumps({"status": "ok"})



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
