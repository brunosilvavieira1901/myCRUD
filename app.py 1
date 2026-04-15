import mysql.connector
import tkinter as tk
from tkinter import messagebox

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="escola"
)

cursor = con.cursor()

def inserir():
    nome = entry_nome.get()
    idade = entry_idade.get()
    curso = entry_curso.get()

    sql = "INSERT INTO alunos (nome, idade, curso) VALUES (%s, %s, %s)"
    cursor.execute(sql, (nome, idade, curso))
    con.commit()

    messagebox.showinfo("Sucesso", "Inserido!")

def pesquisar():
    cursor.execute("SELECT * FROM alunos")
    dados = cursor.fetchall()

    texto = ""
    for d in dados:
        texto += str(d) + "\n"

    messagebox.showinfo("Dados", texto)

def atualizar():
    id_aluno = entry_id.get()
    nome = entry_nome.get()
    idade = entry_idade.get()
    curso = entry_curso.get()

    sql = "UPDATE alunos SET nome=%s, idade=%s, curso=%s WHERE id=%s"
    cursor.execute(sql, (nome, idade, curso, id_aluno))
    con.commit()

    messagebox.showinfo("Sucesso", "Atualizado!")

def excluir():
    id_aluno = entry_id.get()

    sql = "DELETE FROM alunos WHERE id=%s"
    cursor.execute(sql, (id_aluno,))
    con.commit()

    messagebox.showinfo("Sucesso", "Excluído!")

janela = tk.Tk()
janela.title("Sistema Escola")

tk.Label(janela, text="ID").pack()
entry_id = tk.Entry(janela)
entry_id.pack()

tk.Label(janela, text="Nome").pack()
entry_nome = tk.Entry(janela)
entry_nome.pack()

tk.Label(janela, text="Idade").pack()
entry_idade = tk.Entry(janela)
entry_idade.pack()

tk.Label(janela, text="Curso").pack()
entry_curso = tk.Entry(janela)
entry_curso.pack()

tk.Button(janela, text="Inserir", command=inserir).pack()
tk.Button(janela, text="Pesquisar", command=pesquisar).pack()
tk.Button(janela, text="Atualizar", command=atualizar).pack()
tk.Button(janela, text="Excluir", command=excluir).pack()

janela.mainloop()
