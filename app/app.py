from flask import Flask, render_template, request,url_for, redirect
from flask_mysqldb import MySQL
import pymysql

app = Flask("__name__,template_folder='template'")

def create_connection():
    try:
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='fatec',
            database='trabdev4',
            cursorclass=pymysql.cursors.DictCursor
        )
        return conn
    except pymysql.MySQLError as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/jedis')
def jedis():
    return render_template("jedis.html")

@app.route('/lightsabers')
def lightsabers():
    return render_template("lightsabers.html")

@app.route('/contatos')
def contact():
    return render_template("contatos.html")

@app.route('/exibir')
def exibir():
    conn = create_connection()
    try:
        cursor = conn.cursor() 
        cursor.execute("SELECT * FROM comentario")
        trabdev4 = cursor.fetchall()
        print(trabdev4)
        conn.commit()
    except pymysql.MySQLError as e:
        print(f"Erro ao executar a query: {e}")
    finally:
        conn.close()
    return render_template("exibir.html", trabdev4=trabdev4)


@app.route('/comentario', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return "Login via the login Form"
     
    if request.method == 'POST':
        email = request.form['email']
        assunto = request.form['assunto']
        escrito = request.form['escrito']
        conn = create_connection()
        cursor = conn.cursor() 
        cursor.execute('''INSERT INTO comentario (email,assunto,escrito) VALUES(%s,%s,%s)''',(email, assunto ,escrito))
        cursor.connection.commit()
        cursor.close()
        return redirect('/exibir')

if __name__ == '__main__':
    app.run(debug = True)