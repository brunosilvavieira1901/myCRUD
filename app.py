from flask import Flask, render_template, request, jsonify
import mysql.connector

app = Flask(__name__)

def get_db():
    return mysql.connector.connect(
        host="localhost", user="root", password="", database="escola"
    )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/listar')
def listar():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM alunos")
    alunos = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(alunos)

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    dados = request.json
    nome = dados.get('nome')
    idade = dados.get('idade')
    
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO alunos (nome, idade) VALUES (%s, %s)", (nome, idade))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"status": "sucesso"})

@app.route('/excluir/<int:id>', methods=['DELETE'])
def excluir(id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM alunos WHERE id = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"status": "apagado"})

if __name__ == '__main__':
    app.run(debug=True)
