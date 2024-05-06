from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask('__name__')

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'fatec'
app.config['MYSQL_DB'] = 'trabdev4'
 
mysql = MySQL(app)


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

@app.route('/comentario', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return "Login via the login Form"
     
    if request.method == 'POST':
        email = request.form['email']
        assunto = request.form['assunto']
        escrito = request.form['escrito']
        cursor = mysql.connection.cursor()
        cursor.execute('''INSERT INTO comentario (email,assunto,escrito) VALUES(%s,%s,%s)''',(email, assunto ,escrito))
        mysql.connection.commit()
        cursor.close()
        return f"Done!!"

if __name__ == '__main__':
    app.run(debug = True)