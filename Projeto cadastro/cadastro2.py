import tkinter as tk
from tkinter import messagebox
import sqlite3


# --- Funções do Banco de Dados (as mesmas do exemplo anterior) ---
def criar_tabela():
    conn = sqlite3.connect('banco_de_dados.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS funcionarios (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            data_nascimento TEXT,
            endereco TEXT,
            rg TEXT,
            cpf TEXT,
            telefone TEXT,
            email TEXT,
            readaptado TEXT,
            setor TEXT,
            local_trabalho TEXT,
            habilidades TEXT
        )
    ''')
    conn.commit()
    conn.close()


def inserir_funcionario(dados):
    conn = sqlite3.connect('banco_de_dados.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO funcionarios (
            nome, data_nascimento, endereco, rg, cpf, telefone, email,
            readaptado, setor, local_trabalho, habilidades
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        dados['nome'], dados['data_nascimento'], dados['endereco'],
        dados['rg'], dados['cpf'], dados['telefone'], dados['email'],
        dados['readaptado'], dados['setor'], dados['local_trabalho'],
        dados['habilidades']
    ))
    conn.commit()
    conn.close()


def buscar_funcionario(nome):
    conn = sqlite3.connect('banco_de_dados.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM funcionarios WHERE nome=?", (nome,))
    resultado = cursor.fetchone()
    conn.close()
    return resultado


def apagar_funcionario(nome):
    conn = sqlite3.connect('banco_de_dados.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM funcionarios WHERE nome=?", (nome,))
    conn.commit()
    conn.close()


# --- Funções da Interface Gráfica ---
def cadastrar():
    """Função para a janela de cadastro."""
    janela_cadastro = tk.Toplevel(root)
    janela_cadastro.title("Cadastrar Novo Funcionário")

    campos = ['nome', 'data_nascimento', 'endereco', 'rg', 'cpf', 'telefone', 'email', 'readaptado (s/n)', 'setor',
              'local_trabalho', 'habilidades']
    entradas = {}

    for i, campo in enumerate(campos):
        tk.Label(janela_cadastro, text=campo.replace('_', ' ').title() + ":").grid(row=i, column=0, padx=5, pady=5,
                                                                                   sticky="w")
        entrada = tk.Entry(janela_cadastro, width=40)
        entrada.grid(row=i, column=1, padx=5, pady=5)
        entradas[campo.split()[0]] = entrada

    def salvar_dados():
        dados = {campo: entradas[campo.split()[0]].get() for campo in campos}
        try:
            inserir_funcionario(dados)
            messagebox.showinfo("Sucesso", "Funcionário cadastrado!")
            janela_cadastro.destroy()
        except sqlite3.Error as e:
            messagebox.showerror("Erro", f"Erro ao cadastrar: {e}")

    tk.Button(janela_cadastro, text="Salvar", command=salvar_dados).grid(row=len(campos), columnspan=2, pady=10)


def consultar():
    """Função para a janela de consulta."""
    janela_consulta = tk.Toplevel(root)
    janela_consulta.title("Consultar Funcionário")

    tk.Label(janela_consulta, text="Nome do Funcionário:").grid(row=0, column=0, padx=5, pady=5)
    entrada_nome = tk.Entry(janela_consulta, width=40)
    entrada_nome.grid(row=0, column=1, padx=5, pady=5)

    def buscar_dados():
        nome = entrada_nome.get()
        if not nome:
            messagebox.showwarning("Atenção", "Por favor, digite um nome para buscar.")
            return

        resultado = buscar_funcionario(nome)
        if resultado:
            messagebox.showinfo("Resultado da Busca", f"Funcionário encontrado:\n\n"
                                                      f"ID: {resultado[0]}\n"
                                                      f"Nome: {resultado[1]}\n"
                                                      f"Data de Nascimento: {resultado[2]}\n"
                                                      f"Endereço: {resultado[3]}\n"
                                                      f"RG: {resultado[4]}\n"
                                                      f"CPF: {resultado[5]}\n"
                                                      f"Telefone: {resultado[6]}\n"
                                                      f"E-mail: {resultado[7]}\n"
                                                      f"Readaptado: {resultado[8]}\n"
                                                      f"Setor: {resultado[9]}\n"
                                                      f"Local de Trabalho: {resultado[10]}\n"
                                                      f"Habilidades: {resultado[11]}")
        else:
            messagebox.showinfo("Resultado da Busca", f"Funcionário '{nome}' não encontrado.")

    tk.Button(janela_consulta, text="Buscar", command=buscar_dados).grid(row=0, column=2, padx=5)


def apagar():
    """Função para a janela de apagar."""
    janela_apagar = tk.Toplevel(root)
    janela_apagar.title("Apagar Funcionário")

    tk.Label(janela_apagar, text="Nome do Funcionário:").grid(row=0, column=0, padx=5, pady=5)
    entrada_nome = tk.Entry(janela_apagar, width=40)
    entrada_nome.grid(row=0, column=1, padx=5, pady=5)

    def apagar_dados():
        nome = entrada_nome.get()
        if not nome:
            messagebox.showwarning("Atenção", "Por favor, digite um nome para apagar.")
            return

        if messagebox.askyesno("Confirmação", f"Tem certeza que deseja apagar o funcionário '{nome}'?"):
            apagar_funcionario(nome)
            messagebox.showinfo("Sucesso", "Funcionário apagado com sucesso!")
            janela_apagar.destroy()

    tk.Button(janela_apagar, text="Apagar", command=apagar_dados).grid(row=0, column=2, padx=5)


# --- Configuração da janela principal ---
root = tk.Tk()
root.title("Sistema de Cadastro de Funcionários")

criar_tabela()

tk.Button(root, text="Cadastrar Funcionário", command=cadastrar, width=25).pack(pady=10)
tk.Button(root, text="Consultar Funcionário", command=consultar, width=25).pack(pady=10)
tk.Button(root, text="Apagar Funcionário", command=apagar, width=25).pack(pady=10)
tk.Button(root, text="Sair", command=root.quit, width=25).pack(pady=10)

root.mainloop()