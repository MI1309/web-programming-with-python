from flask_restful import abort, reqparse, Api, Resource
from flask import Flask
from flask_cors import CORS

# Restfull API Sederhana

# GOAL
# 1. C DONE
# 2. R DONE
# 3. U DONE
# 4. D DONE

# init
app = Flask(__name__)
api = Api(app)
api_resource = Resource

# memberi izin CORS
CORS(app)

# TODOS
TODOS = {
    'todo1':{'task':'lagi ngoding'},
    'todo2':{'task':'lagi buat api'},
    'todo3':{'task':'besok dapat nilai 100 yuk cihuyy'}
}

# 8.4 membuat abort validasi
def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, pesan=f"todo {todo_id} ga ada atau ga tersedia")

# 8.5 membuat parser argumen
parser = reqparse.RequestParser()
# 8.6 menambahkan task sebagai tanda di todo id
parser.add_argument('task')

# tampungan hal yang dapat dilakukan
class TODO(api_resource):
    def get(self, todo_id):
        # abort validasi
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]
    
    def delete(self, todo_id):
        # abort validasi
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204
    
    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201

# list dari todo
class TODOLIST(api_resource):
    def get(self):
        return TODOS
    
    def post(self):
        args = parser.parse_args()
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], 201
    
api.add_resource(TODOLIST,'/todos')
api.add_resource(TODO,'/todos/<todo_id>')

if __name__ == "__main__":
    app.run(debug=False)
    

# Langkah-langkah Perbaikan:
# Install dan konfigurasi Gunicorn untuk menangani permintaan aplikasi.
# Atur CORS dengan lebih ketat di produksi.
# Gunakan log untuk memantau dan mendiagnosis masalah.
# Pastikan koneksi database dan pengaturan lingkungan sesuai untuk produksi.
# Optimalkan aplikasi dan server web untuk memastikan stabilitas dan kinerja yang lebih baik.