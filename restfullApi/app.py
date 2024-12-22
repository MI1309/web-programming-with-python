import flask
import flask_restful
from flask_cors import CORS
import flask_restful.reqparse

app = flask.Flask(__name__)
api = flask_restful.Api(app)
api_resource = flask_restful.Resource

# poin penting di tulis angka, sub materi 1.1

# 1. mengizinkan flask untuk CORS (cross origin resource sharing)
CORS(app)

# 2. argument parsing
parser = flask_restful.reqparse.RequestParser()

# 2.1 menambahkan parsing argument
parser.add_argument('rate', type=int, required=True, help='isi pakai integer kocak', location='args')
parser.add_argument('bool', type=bool, help='isi pakai boolean kocak', location='args')
parser.add_argument('name', type=str, help='isi memakai str', location='args')

# 2.2 contoh parsing argument
class Parsing(api_resource):
    def get(self):
        # 2.3 memuat beberapa argumen dari url
        args = parser.parse_args()
        print(args)
        return {"pesan":"berhasil!", "data": args}, 200

# 2.3 akan mengeluarkan error 415 media type error
api.add_resource(Parsing, '/parse')
# 3. json
data_json = {
    "minuman":"aqua"
}

# 4. mengatur resource url
class products(api_resource):
    def get(self):
        return data_json

# 5.
todos = {}
class Todos(api_resource):
    def get(self,todo_id):
        return {todo_id: todos[todo_id]}
    
    def put(self,todo_id):
        todos[todo_id] = flask.request.form['data']
        return {todo_id: todos[todo_id]}

# 6. bisa iterable request dari class
class Api(api_resource):
    def get(self):
        return {"Task": "halo dunia"}, 201, {'test':'1234'}

class Api1(api_resource):
    def get(self):
        return {"Task": "halo dunia"}, 201
    
class Api2(api_resource):
    def get(self):
        return {"task": "halo dunia"}, 201, {'Etag':'test'}
    

# 7. menambahkan resource api / endpoint
# 7.1 bisa menambahkan beberapa endpoint ke url
api.add_resource(products, "/", '/hello')

# 7.2 endpoint dengan tipe data
api.add_resource(Todos, "/todo/<string:todo_id>")

# 7.3 dengan args
api.add_resource(Api,'/api' ,endpoint='api1')
api.add_resource(Api2,'/api2' ,endpoint='Etag')

# 8. data formatting
from flask_restful import fields, marshal_with, abort, reqparse

# 8.1 dictionary sumber
bagian_sumber = {
    'task': fields.String,
    'uri': fields.Url('api1')
}

class TodoApp(api_resource):
    def __init__(self, todo_id, task):
        self.todo_id = todo_id
        self.task = task
        self.status = 'active'
        
class Todo(api_resource):
    # 8.2 membuat dict bagian_sumber
    @marshal_with(bagian_sumber)
    def get(self, **kwargs):
        return TodoApp(todo_id='imron', task="lagi ngoding")
api.add_resource(Todo, '/todos')

# 8.3 contoh lengkap di -> todos_api.py


# kontent type json
# @app.route("/api", methods=['PUT'])
# def isi_put():
#     # ambil json dari server
#     data = flask.request.get_json()
#     if not data:
#         return {"error":"invalid json"}, 400
#     data_json = flask.jsonify({"put variabel":data})
#     print(data_json)


if __name__ == "__main__":
    app.run(debug=True)