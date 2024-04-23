from flask import Flask, render_template
app = Flask('__name__')

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/jedis')
def jedis():
    return render_template("jedis.html")

@app.route('/lightsabers')
def lightsabers():
    return render_template("lightsabers.html")

if __name__ == '__main__':
    app.run(debug = True)