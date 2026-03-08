from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def criar_banco():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        senha TEXT,
        telefone TEXT
    )
    """)

    conn.commit()
    conn.close()

criar_banco()


@app.route('/')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/dashboard', methods=['GET','POST'])
def dashboard():

    resultado = ""

    if request.method == 'POST':

        nota = float(request.form['nota'])

        if nota >= 7:
            resultado = "Aluno Aprovado"
        elif nota >= 5:
            resultado = "Aluno em Recuperação"
        else:
            resultado = "Aluno Reprovado"

    return render_template("dashboard.html", resultado=resultado)


if __name__ == '__main__':
    app.run(debug=True)