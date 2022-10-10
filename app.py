from flask import Flask
import json
import mariadb

config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': 'obelix',
    'database': 'todos_db'
}


app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hola Mundo Containerizado!'

# Ruta para devolver todos los ToDos.
@app.route('/api/todos', methods=['GET'])
def index():
   # Conexión a MariaDB.
   conn = mariadb.connect(**config)
   # Creación de cursor.
   cur = conn.cursor()
   # Ejecutamos la instrucción SQL.
   cur.execute("select * from todos")

   # Serializamos en JSON....
   row_headers=[x[0] for x in cur.description]
   rv = cur.fetchall()
   json_data=[]
   for result in rv:
        json_data.append(dict(zip(row_headers,result)))

   # Y devolvemos todo.
   return json.dumps(json_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
