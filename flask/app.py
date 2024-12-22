from flask import (Flask, render_template, request, make_response, session, redirect, url_for, flash, abort)
from werkzeug.utils import secure_filename
from markupsafe import escape

# init
app = Flask(__name__)
app.secret_key = "hai"

# halaman error
@app.errorhandler(401)
def page_not_found(e):
    return render_template('error_page/401.html'), 401

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error_page/401.html'), 404

@app.errorhandler(405)
def page_not_method(e):
    return render_template('error_page/405.html'), 405

@app.errorhandler(500)
def page_not_method(e):
    return render_template('error_page/500.html'), 500

# upload gambar
ALLOWED_EXTENSION = {'png','jpeg','jpg','svg','jfif'}
# wadah file upload
app.config['UPLOAD_FOLDER'] = 'files/'

# diuji 3 x
# nama file sama extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSION

@app.route('/upload', methods=["GET", "POST"])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        # 1
        # memastikan atribut file
        if 'file' not in request.files:
            return redirect(request.url)
        
        # 2
        # ketika user tidak memilih file sama sekali
        if file.filename == '':
            return redirect(request.url)
        
        # 3
        # jika filenya ada
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            # simpan
            file.save(app.config['UPLOAD_FOLDER'] + filename)
            return f"file berhasil diupload : {filename}"
    return render_template('upload.html')


# aturan variabel

# 1. int
@app.route('/id/<int:angka>')
# response
def angka(angka): # %d untuk integer
    return f"angka yang diambil dari url: {escape(angka)}"

# 2. string
@app.route('/nama/<nama>')
def tampilkan_nama(nama):
    return f"nama yang diambil dari url {escape(nama)}"

# 3. float
@app.route('/float/<float:float>')
def tampilkan_float(float):
    return f"angka float yang diambil url {escape(float)}"

# 4. path
@app.route('/path/<path:subpath>')
def show_path(subpath):
    return f"path yang diambil dari url :{escape(subpath)}"
    
# 5. uuid
@app.route('/uuid/<uuid:uuid>')
def show_uuid(uuid):
    return f"uuid yang diambil dari url : {escape(uuid)}"

# index
@app.route('/')
def index():
    # ini mengambil get dalam bentuk dict
    title = 'flask library'
    search = request.args.get("search")
    id = request.args.get("id")
    return render_template("index.html", search=search,id=id, title=title)

@app.route('/user/<username>/<email>/<password>')
def show_user(username,email,password):
    return render_template("profile.html",username=username,email=email,password=password)

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        
        if request.form['password'] == '':
            abort(401)
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        # membuat response
        # response = make_response(redirect(url_for('show_user',username=username,email=email,password=password)))
        
        # simpan cookie
        # response.set_cookie("username_user", username)
        # response.set_cookie("password_user", password)
        # response.set_cookie("email_user", email)
        
        # simpan session
        session['username'] = username
        session['password'] = password
        session['email'] = email
        
        # flash message / alert
        flash("kamu berhasil login", "succes")
        return redirect(url_for('show_user',username=username,email=email,password=password))
        
    # kondisi jika user sudah login
    if 'username' in session and 'password' in session and "email" in session:
        print(session)
        username = session["username"]
        password = session["password"]
        email = session["email"]
        return redirect(url_for('show_user',username=username, password=password, email=email))
                    
    return render_template("login.html")

# !! fitur cookie dimatikan karena belajar flash message

# mengambil set cookie dan menampilkannya
@app.route("/getcookie")
def getCookie():
    password = request.cookies.get("password_user")
    username = request.cookies.get("username_user")
    email = request.cookies.get("email_user")
    return f"BIO Cookie <br><br>username: {username}<br>password: {password}<br>email: {email}"

# ruter logout
@app.route("/logout")
def logout():
    # jika user klik akan menghapus session yang dipilih
    session.pop("username",None)
    return redirect(url_for('login'))