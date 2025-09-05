import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext, font
import sqlite3
import re
import webbrowser

# --- Setup do Banco de Dados ---
def setup_database():
    """Configura o banco de dados e as tabelas, garantindo a estrutura correta."""
    conn = None
    try:
        conn = sqlite3.connect('cadastro.db')
        cursor = conn.cursor()
        
        # Cria a tabela de cadastros, se não existir
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS pessoas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                matricula TEXT NOT NULL UNIQUE,
                nome TEXT NOT NULL,
                data_nascimento TEXT,
                endereco TEXT,
                rg TEXT,
                cpf TEXT,
                email TEXT,
                readaptado TEXT,
                setor TEXT,
                local_trabalho TEXT,
                habilidades TEXT,
                telefone TEXT
            )
        ''')

        # Cria a tabela de usuários, se não existir
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                matricula TEXT NOT NULL UNIQUE,
                login_apelido TEXT NOT NULL UNIQUE,
                username TEXT NOT NULL,
                is_admin INTEGER DEFAULT 0,
                password TEXT NOT NULL
            )
        ''')

        # Insere ou atualiza o usuário padrão 'admin'
        try:
            cursor.execute("INSERT INTO usuarios (matricula, login_apelido, username, is_admin, password) VALUES (?, ?, ?, ?, ?)", ('0000', 'admin', 'Administrador', 1, 'admin123'))
            conn.commit()
        except sqlite3.IntegrityError:
            cursor.execute("UPDATE usuarios SET is_admin = 1, matricula = '0000', username = 'Administrador', password = 'admin123' WHERE login_apelido = 'admin'")
            conn.commit()

    except sqlite3.Error as e:
        messagebox.showerror("Erro de Banco de Dados", f"Ocorreu um erro ao configurar o banco de dados: {e}")
    finally:
        if conn:
            conn.close()

# --- Classes de Interface ---

class ChangePasswordWindow(tk.Toplevel):
    def __init__(self, master, login_apelido, password_callback):
        super().__init__(master)
        self.master = master
        self.login_apelido = login_apelido
        self.password_callback = password_callback
        self.title("Primeiro Acesso - Crie sua Senha")
        self.geometry("350x180")
        self.resizable(False, False)
        
        # Centraliza a janela
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.master.winfo_screenwidth() // 2) - (width // 2)
        y = (self.master.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'{width}x{height}+{x}+{y}')
        
        self.frame = ttk.Frame(self, padding="10")
        self.frame.pack(expand=True)
        
        ttk.Label(self.frame, text=f"Bem-vindo(a), {self.login_apelido}!").pack(pady=5)
        ttk.Label(self.frame, text="Sua senha é temporária. Por favor, crie uma nova.").pack(pady=5)

        ttk.Label(self.frame, text="Nova Senha:").pack(pady=2)
        self.new_password_entry = ttk.Entry(self.frame, show="*")
        self.new_password_entry.pack(pady=2)
        
        ttk.Label(self.frame, text="Confirmar Senha:").pack(pady=2)
        self.confirm_password_entry = ttk.Entry(self.frame, show="*")
        self.confirm_password_entry.pack(pady=2)
        
        self.change_button = ttk.Button(self.frame, text="Salvar Nova Senha", command=self.save_new_password)
        self.change_button.pack(pady=10)

    def save_new_password(self):
        new_password = self.new_password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if not new_password or not confirm_password:
            messagebox.showerror("Erro", "Todos os campos de senha são obrigatórios.")
            return

        if new_password != confirm_password:
            messagebox.showerror("Erro", "As senhas não coincidem.")
            return

        conn = None
        try:
            conn = sqlite3.connect('cadastro.db')
            cursor = conn.cursor()
            cursor.execute("UPDATE usuarios SET password = ? WHERE login_apelido = ?", (new_password, self.login_apelido))
            conn.commit()
            messagebox.showinfo("Sucesso", "Senha alterada com sucesso!")
            self.destroy()
            self.password_callback()
        except sqlite3.Error as e:
            messagebox.showerror("Erro de Banco de Dados", f"Ocorreu um erro: {e}")
        finally:
            if conn:
                conn.close()

class LoginWindow(tk.Toplevel):
    def __init__(self, master, login_callback):
        super().__init__(master)
        self.master = master
        self.login_callback = login_callback
        self.title("Login")
        self.geometry("300x150")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.master.quit)
        
        # Centralizar janela
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.master.winfo_screenwidth() // 2) - (width // 2)
        y = (self.master.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'{width}x{height}+{x}+{y}')

        self.frame = ttk.Frame(self, padding="10")
        self.frame.pack(expand=True)
        
        ttk.Label(self.frame, text="Login/Apelido:").grid(row=0, column=0, pady=5)
        self.login_entry = ttk.Entry(self.frame)
        self.login_entry.grid(row=0, column=1, pady=5)
        
        ttk.Label(self.frame, text="Senha:").grid(row=1, column=0, pady=5)
        self.password_entry = ttk.Entry(self.frame, show="*")
        self.password_entry.grid(row=1, column=1, pady=5)
        
        self.login_button = ttk.Button(self.frame, text="Entrar", command=self.check_login)
        self.login_button.grid(row=2, columnspan=2, pady=10)

        self.bind('<Return>', lambda event=None: self.check_login())

    def check_login(self):
        login_apelido = self.login_entry.get()
        password = self.password_entry.get()
        
        conn = None
        try:
            conn = sqlite3.connect('cadastro.db')
            cursor = conn.cursor()
            cursor.execute("SELECT matricula, login_apelido, username, is_admin, password FROM usuarios WHERE login_apelido=? AND password=?", (login_apelido, password))
            user = cursor.fetchone()
            if user:
                is_admin = bool(user[3])
                
                # Verifica se é o primeiro acesso (se a senha for a temporária) e não é o admin
                if password == 'mudar123' and not is_admin:
                    self.destroy()
                    ChangePasswordWindow(self.master, login_apelido, lambda: self.login_callback(is_admin))
                else:
                    self.destroy()
                    self.login_callback(is_admin)
            else:
                messagebox.showerror("Erro de Login", "Apelido ou senha incorretos.")
        except sqlite3.Error as e:
            messagebox.showerror("Erro de Banco de Dados", f"Ocorreu um erro: {e}")
        finally:
            if conn:
                conn.close()

class EditUserWindow(tk.Toplevel):
    def __init__(self, master, user_data, callback_reload):
        super().__init__(master)
        self.master = master
        self.user_data = user_data
        self.callback_reload = callback_reload
        self.title(f"Editar Usuário: {user_data[2]}")
        self.geometry("400x250")
        self.resizable(False, False)

        frame = ttk.Frame(self, padding="10")
        frame.pack(expand=True, fill="both")

        ttk.Label(frame, text="Matrícula:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.matricula_entry = ttk.Entry(frame, width=30)
        self.matricula_entry.grid(row=0, column=1, padx=5, pady=5)
        self.matricula_entry.insert(0, self.user_data[1])

        ttk.Label(frame, text="Apelido/Login:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.login_entry = ttk.Entry(frame, width=30)
        self.login_entry.grid(row=1, column=1, padx=5, pady=5)
        self.login_entry.insert(0, self.user_data[2])
        
        ttk.Label(frame, text="Nome Completo:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.username_entry = ttk.Entry(frame, width=30)
        self.username_entry.grid(row=2, column=1, padx=5, pady=5)
        self.username_entry.insert(0, self.user_data[3])
        
        # --- CORREÇÃO: Converte a string "Sim" ou "Não" para 1 ou 0 ---
        is_admin_value = 1 if self.user_data[4] == "Sim" else 0
        self.admin_var = tk.IntVar(value=is_admin_value)
        # --- FIM DA CORREÇÃO ---
        
        ttk.Checkbutton(frame, text="É Administrador", variable=self.admin_var).grid(row=3, columnspan=2, pady=10)
        
        btn_save = ttk.Button(frame, text="Salvar Alterações", command=self.save_changes)
        btn_save.grid(row=4, columnspan=2, pady=10)

    def save_changes(self):
        new_matricula = self.matricula_entry.get()
        new_login = self.login_entry.get()
        new_username = self.username_entry.get()
        new_is_admin = self.admin_var.get()

        if not new_matricula or not new_login or not new_username:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios.")
            return

        conn = None
        try:
            conn = sqlite3.connect('cadastro.db')
            cursor = conn.cursor()
            
            cursor.execute('''
                UPDATE usuarios
                SET matricula = ?, login_apelido = ?, username = ?, is_admin = ?
                WHERE id = ?
            ''', (new_matricula, new_login, new_username, new_is_admin, self.user_data[0]))
            
            conn.commit()
            messagebox.showinfo("Sucesso", "Usuário atualizado com sucesso!")
            self.callback_reload()
            self.destroy()
        except sqlite3.IntegrityError:
            messagebox.showerror("Erro", "O Apelido/Login ou Matrícula já existe para outro usuário.")
        except sqlite3.Error as e:
            messagebox.showerror("Erro de Banco de Dados", f"Ocorreu um erro: {e}")
        finally:
            if conn:
                conn.close()

# --- Classe Principal da Aplicação ---
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Cadastro")
        self.geometry("800x600")
        self.config(bg="#f0f2f5")
        self.withdraw()

        self.fonte_padrao = font.Font(family="Helvetica", size=10, weight="normal")
        self.fonte_titulo = font.Font(family="Helvetica", size=16, weight="bold")
        self.fonte_subtitulo = font.Font(family="Helvetica", size=12, weight="bold")
        
        style = ttk.Style(self)
        style.theme_use('clam')
        style.configure("TFrame", background="#f0f2f5")
        style.configure("TLabel", background="#f0f2f5", font=self.fonte_padrao)
        style.configure("TButton", font=self.fonte_padrao, padding=6)
        style.map("TButton", background=[("active", "#d4d4d4")])
        
        self.show_login_window()

    def show_login_window(self):
        self.login_window = LoginWindow(self, self.on_login_success)

    def on_login_success(self, is_admin):
        self.is_admin = is_admin
        self.deiconify()
        self.setup_main_app()

    def logout(self):
        """Método para realizar o logout do usuário e retornar à tela de login."""
        if messagebox.askyesno("Confirmar Saída", "Tem certeza que deseja sair?"):
            self.withdraw()  # Oculta a janela principal
            if hasattr(self, 'notebook'):
                self.notebook.destroy()
            self.show_login_window()

    def setup_main_app(self):
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill="both", padx=10, pady=10)

        self.frame_cadastro = ttk.Frame(self.notebook)
        self.frame_consulta = ttk.Frame(self.notebook)
        self.frame_relatorio = ttk.Frame(self.notebook)

        self.notebook.add(self.frame_cadastro, text="Cadastro")
        self.notebook.add(self.frame_consulta, text="Consulta e Exclusão")
        self.notebook.add(self.frame_relatorio, text="Relatório")
        
        if self.is_admin:
            self.frame_usuarios = ttk.Frame(self.notebook)
            self.notebook.add(self.frame_usuarios, text="Gerenciar Usuários")
            self.setup_user_management()

        self.setup_cadastro()
        self.setup_consulta()
        self.setup_relatorio()

    def setup_cadastro(self):
        titulo = ttk.Label(self.frame_cadastro, text="Cadastro de Pessoas", font=self.fonte_titulo)
        titulo.pack(pady=10)

        frame_campos = ttk.Frame(self.frame_cadastro)
        frame_campos.pack(padx=20, pady=10)

        campos = [
            ("Matrícula:", "matricula"),
            ("Nome:", "nome"),
            ("Data de Nascimento:", "data_nascimento"),
            ("Endereço:", "endereco"),
            ("RG:", "rg"),
            ("CPF:", "cpf"),
            ("E-mail:", "email"),
            ("Readaptado s/n:", "readaptado"),
            ("Setor:", "setor"),
            ("Local de Trabalho:", "local_trabalho"),
            ("Telefone:", "telefone")
        ]
        
        self.entradas = {}
        row = 0
        for label_text, key in campos:
            ttk.Label(frame_campos, text=label_text).grid(row=row, column=0, sticky="w", padx=5, pady=2)
            entrada = ttk.Entry(frame_campos, width=50, font=self.fonte_padrao)
            entrada.grid(row=row, column=1, padx=5, pady=2)
            self.entradas[key] = entrada
            row += 1

        ttk.Label(frame_campos, text="Habilidades:").grid(row=row, column=0, sticky="nw", padx=5, pady=2)
        self.habilidades_text = scrolledtext.ScrolledText(frame_campos, width=48, height=4, wrap=tk.WORD, font=self.fonte_padrao)
        self.habilidades_text.grid(row=row, column=1, padx=5, pady=2)

        btn_salvar = ttk.Button(self.frame_cadastro, text="Salvar Cadastro", command=self.salvar_cadastro)
        btn_salvar.pack(pady=10)

    def salvar_cadastro(self):
        dados = {key: entry.get() for key, entry in self.entradas.items()}
        dados["habilidades"] = self.habilidades_text.get("1.0", tk.END).strip()
        
        if not dados["matricula"] or not dados["nome"]:
            messagebox.showerror("Erro de Validação", "Matrícula e Nome são campos obrigatórios.")
            return
        
        if dados["cpf"] and not re.match(r'^\d{3}\.?\d{3}\.?\d{3}-?\d{2}$', dados["cpf"]):
            messagebox.showerror("Erro de Validação", "Formato de CPF inválido. Use 000.000.000-00 ou 00000000000.")
            return
        
        if dados["email"] and not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', dados["email"]):
            messagebox.showerror("Erro de Validação", "Formato de e-mail inválido.")
            return

        conn = None
        try:
            conn = sqlite3.connect('cadastro.db')
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO pessoas (
                    matricula, nome, data_nascimento, endereco, rg, cpf, email,
                    readaptado, setor, local_trabalho, habilidades, telefone
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                dados["matricula"], dados["nome"], dados["data_nascimento"], dados["endereco"],
                dados["rg"], dados["cpf"], dados["email"],
                dados["readaptado"], dados["setor"], dados["local_trabalho"], dados["habilidades"], dados["telefone"]
            ))
            conn.commit()
            messagebox.showinfo("Sucesso", "Cadastro salvo com sucesso!")
            self.limpar_campos()
        except sqlite3.IntegrityError:
            messagebox.showerror("Erro de Banco de Dados", "Matrícula já existe no banco de dados.")
        except sqlite3.Error as e:
            messagebox.showerror("Erro de Banco de Dados", f"Ocorreu um erro: {e}")
        finally:
            if conn:
                conn.close()

    def limpar_campos(self):
        for entry in self.entradas.values():
            entry.delete(0, tk.END)
        self.habilidades_text.delete("1.0", tk.END)

    def setup_consulta(self):
        titulo = ttk.Label(self.frame_consulta, text="Consultar e Excluir Cadastro", font=self.fonte_titulo)
        titulo.pack(pady=10)

        frame_busca = ttk.Frame(self.frame_consulta)
        frame_busca.pack(padx=20, pady=10)
        
        ttk.Label(frame_busca, text="Termo de Busca:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.entrada_busca = ttk.Entry(frame_busca, width=30)
        self.entrada_busca.grid(row=0, column=1, padx=5, pady=5)

        # Botões de busca específicos
        btn_buscar_matricula = ttk.Button(frame_busca, text="Buscar por Matrícula", command=lambda: self.buscar_cadastro_por('matricula'))
        btn_buscar_matricula.grid(row=1, column=0, padx=5, pady=2, sticky=tk.W)
        
        btn_buscar_nome = ttk.Button(frame_busca, text="Buscar por Nome", command=lambda: self.buscar_cadastro_por('nome'))
        btn_buscar_nome.grid(row=1, column=1, padx=5, pady=2, sticky=tk.W)
        
        btn_buscar_setor = ttk.Button(frame_busca, text="Buscar por Setor", command=lambda: self.buscar_cadastro_por('setor'))
        btn_buscar_setor.grid(row=2, column=0, padx=5, pady=2, sticky=tk.W)
        
        btn_buscar_local = ttk.Button(frame_busca, text="Buscar por Local de Trabalho", command=lambda: self.buscar_cadastro_por('local_trabalho'))
        btn_buscar_local.grid(row=2, column=1, padx=5, pady=2, sticky=tk.W)
        
        self.resultado_busca = scrolledtext.ScrolledText(self.frame_consulta, width=80, height=15, wrap=tk.WORD, font=self.fonte_padrao)
        self.resultado_busca.pack(padx=20, pady=10)

        frame_botoes_consulta = ttk.Frame(self.frame_consulta)
        frame_botoes_consulta.pack(pady=10)
        
        btn_excluir = ttk.Button(frame_botoes_consulta, text="Excluir Cadastro", command=self.excluir_cadastro)
        btn_excluir.pack(side=tk.LEFT, padx=5)

        btn_imprimir = ttk.Button(frame_botoes_consulta, text="Imprimir Cadastro", command=self.imprimir_cadastro_individual)
        btn_imprimir.pack(side=tk.LEFT, padx=5)

        self.btn_email = ttk.Button(frame_botoes_consulta, text="Enviar por E-mail", command=self.enviar_email_cadastro)
        self.btn_email.pack(side=tk.LEFT, padx=5)
        self.btn_email["state"] = "disabled"

    def buscar_cadastro_por(self, campo):
        termo_busca = self.entrada_busca.get()
        if not termo_busca:
            messagebox.showerror("Erro", "Por favor, insira um termo para a busca.")
            self.btn_email["state"] = "disabled"
            return

        conn = None
        try:
            conn = sqlite3.connect('cadastro.db')
            cursor = conn.cursor()
            
            query = f"SELECT * FROM pessoas WHERE {campo} LIKE ?"
            cursor.execute(query, (f'%{termo_busca}%',))
            
            resultados = cursor.fetchall()
            self.resultado_busca.delete("1.0", tk.END)
            
            if resultados:
                for idx, resultado in enumerate(resultados):
                    self.resultado_busca.insert(tk.END, f"--- Resultado {idx + 1} ---\n")
                    self.resultado_busca.insert(tk.END, self.formatar_registro(resultado))
                    self.resultado_busca.insert(tk.END, "\n\n")
                self.btn_email["state"] = "normal"
            else:
                self.resultado_busca.insert(tk.END, "Nenhum cadastro encontrado.")
                self.btn_email["state"] = "disabled"

        except sqlite3.Error as e:
            messagebox.showerror("Erro de Banco de Dados", f"Ocorreu um erro: {e}")
        finally:
            if conn:
                conn.close()

    def enviar_email_cadastro(self):
        dados_formatados = self.resultado_busca.get("1.0", tk.END).strip()
        if not dados_formatados:
            messagebox.showerror("Erro", "Nenhum cadastro para enviar. Por favor, realize uma busca primeiro.")
            return

        subject = "Dados de Cadastro"
        body = dados_formatados.replace('\n', '%0A')
        
        mailto_url = f"mailto:?subject={subject}&body={body}"
        
        try:
            webbrowser.open(mailto_url)
        except webbrowser.Error:
            messagebox.showerror("Erro", "Não foi possível abrir o cliente de e-mail padrão. Verifique a configuração do seu sistema.")

    def excluir_cadastro(self):
        matricula = self.entrada_busca.get()
        if not matricula:
            messagebox.showerror("Erro", "Por favor, insira a matrícula do cadastro que deseja excluir.")
            return

        if messagebox.askyesno("Confirmação", f"Tem certeza que deseja excluir o cadastro da matrícula {matricula}?"):
            conn = None
            try:
                conn = sqlite3.connect('cadastro.db')
                cursor = conn.cursor()
                cursor.execute("DELETE FROM pessoas WHERE matricula=?", (matricula,))
                conn.commit()
                if cursor.rowcount > 0:
                    messagebox.showinfo("Sucesso", "Cadastro excluído com sucesso!")
                    self.resultado_busca.delete("1.0", tk.END)
                    self.entrada_busca.delete(0, tk.END)
                    self.btn_email["state"] = "disabled"
                else:
                    messagebox.showerror("Erro", "Nenhum cadastro encontrado com essa matrícula para exclusão.")
            except sqlite3.Error as e:
                messagebox.showerror("Erro de Banco de Dados", f"Ocorreu um erro: {e}")
            finally:
                if conn:
                    conn.close()

    def imprimir_cadastro_individual(self):
        dados_formatados = self.resultado_busca.get("1.0", tk.END).strip()
        if dados_formatados:
            messagebox.showinfo("Imprimir Cadastro", "Simulando impressão:\n\n" + dados_formatados)
        else:
            messagebox.showerror("Erro", "Nenhum cadastro para imprimir. Por favor, realize uma busca primeiro.")

    def setup_relatorio(self):
        titulo = ttk.Label(self.frame_relatorio, text="Relatório e Impressão", font=self.fonte_titulo)
        titulo.pack(pady=10)

        frame_botoes_geral = ttk.Frame(self.frame_relatorio)
        frame_botoes_geral.pack(pady=10)

        btn_gerar_relatorio = ttk.Button(frame_botoes_geral, text="Gerar Relatório Completo", command=self.gerar_relatorio)
        btn_gerar_relatorio.pack(side=tk.LEFT, padx=5)

        btn_imprimir_relatorio = ttk.Button(frame_botoes_geral, text="Imprimir Relatório", command=self.imprimir_relatorio_completo)
        btn_imprimir_relatorio.pack(side=tk.LEFT, padx=5)
        
        self.btn_email_relatorio = ttk.Button(frame_botoes_geral, text="Enviar por E-mail", command=self.enviar_email_relatorio_completo)
        self.btn_email_relatorio.pack(side=tk.LEFT, padx=5)
        self.btn_email_relatorio["state"] = "disabled"

        frame_busca_relatorio = ttk.Frame(self.frame_relatorio)
        frame_busca_relatorio.pack(padx=20, pady=10)
        
        ttk.Label(frame_busca_relatorio, text="Termo de Busca para Relatório:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.entrada_busca_relatorio = ttk.Entry(frame_busca_relatorio, width=30)
        self.entrada_busca_relatorio.grid(row=0, column=1, padx=5, pady=5)
        
        btn_relatorio_setor = ttk.Button(frame_busca_relatorio, text="Gerar por Setor", command=self.gerar_relatorio_por_setor)
        btn_relatorio_setor.grid(row=1, column=0, padx=5, pady=2, sticky=tk.W)
        
        btn_relatorio_local = ttk.Button(frame_busca_relatorio, text="Gerar por Local de Trabalho", command=self.gerar_relatorio_por_local)
        btn_relatorio_local.grid(row=1, column=1, padx=5, pady=2, sticky=tk.W)

        self.relatorio_text = scrolledtext.ScrolledText(self.frame_relatorio, width=80, height=20, wrap=tk.WORD, font=self.fonte_padrao)
        self.relatorio_text.pack(padx=20, pady=10)

    def gerar_relatorio_por_setor(self):
        self.gerar_relatorio_filtrado('setor', self.entrada_busca_relatorio.get())

    def gerar_relatorio_por_local(self):
        self.gerar_relatorio_filtrado('local_trabalho', self.entrada_busca_relatorio.get())

    def gerar_relatorio_filtrado(self, campo, termo_busca):
        if not termo_busca:
            messagebox.showerror("Erro", "Por favor, insira um termo para a busca.")
            self.btn_email_relatorio["state"] = "disabled"
            return
            
        conn = None
        try:
            conn = sqlite3.connect('cadastro.db') 
            cursor = conn.cursor()
            query = f"SELECT * FROM pessoas WHERE {campo} LIKE ?"
            cursor.execute(query, (f'%{termo_busca}%',))
            resultados = cursor.fetchall()
            self.relatorio_text.delete("1.0", tk.END)
            
            if resultados:
                for idx, pessoa in enumerate(resultados):
                    self.relatorio_text.insert(tk.END, f"--- Registro {idx + 1} ---\n")
                    self.relatorio_text.insert(tk.END, self.formatar_registro(pessoa))
                    self.relatorio_text.insert(tk.END, "\n\n")
                self.btn_email_relatorio["state"] = "normal"
            else:
                self.relatorio_text.insert(tk.END, "Nenhum cadastro encontrado.")
                self.btn_email_relatorio["state"] = "disabled"
        except sqlite3.Error as e:
            messagebox.showerror("Erro de Banco de Dados", f"Ocorreu um erro: {e}")
            self.btn_email_relatorio["state"] = "disabled"
        finally:
            if conn:
                conn.close()

    def gerar_relatorio(self):
        conn = None
        try:
            conn = sqlite3.connect('cadastro.db')
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM pessoas")
            resultados = cursor.fetchall()
            self.relatorio_text.delete("1.0", tk.END)
            
            if resultados:
                for idx, pessoa in enumerate(resultados):
                    self.relatorio_text.insert(tk.END, f"--- Registro {idx + 1} ---\n")
                    self.relatorio_text.insert(tk.END, self.formatar_registro(pessoa))
                    self.relatorio_text.insert(tk.END, "\n\n")
                self.btn_email_relatorio["state"] = "normal"
            else:
                self.relatorio_text.insert(tk.END, "Nenhum cadastro encontrado.")
                self.btn_email_relatorio["state"] = "disabled"
                
        except sqlite3.Error as e:
            messagebox.showerror("Erro de Banco de Dados", f"Ocorreu um erro: {e}")
            self.btn_email_relatorio["state"] = "disabled"
        finally:
            if conn:
                conn.close()

    def enviar_email_relatorio_completo(self):
        dados_formatados = self.relatorio_text.get("1.0", tk.END).strip()
        if not dados_formatados:
            messagebox.showerror("Erro", "Nenhum relatório para enviar. Por favor, gere o relatório primeiro.")
            return

        subject = "Relatório Completo de Cadastros"
        body = dados_formatados.replace('\n', '%0A')
        
        mailto_url = f"mailto:?subject={subject}&body={body}"
        
        try:
            webbrowser.open(mailto_url)
        except webbrowser.Error:
            messagebox.showerror("Erro", "Não foi possível abrir o cliente de e-mail padrão. Verifique a configuração do seu sistema.")

    def formatar_registro(self, registro):
        campos_formatados = [
            "ID", "Matrícula", "Nome", "Data de Nascimento", "Endereço", "RG", "CPF",
            "E-mail", "Readaptado", "Setor", "Local de Trabalho", "Habilidades", "Telefone"
        ]
        
        texto_formatado = ""
        for i, campo in enumerate(campos_formatados):
            texto_formatado += f"{campo}: {registro[i]}\n"
        return texto_formatado

    def imprimir_relatorio_completo(self):
        dados_formatados = self.relatorio_text.get("1.0", tk.END).strip()
        if dados_formatados:
            messagebox.showinfo("Imprimir Relatório", "Simulando impressão do relatório completo.")
        else:
            messagebox.showerror("Erro", "Nenhum relatório para imprimir.")
    
    def setup_user_management(self):
        titulo = ttk.Label(self.frame_usuarios, text="Gerenciar Usuários", font=self.fonte_titulo)
        titulo.pack(pady=10)
        
        frame_adicionar = ttk.LabelFrame(self.frame_usuarios, text="Adicionar Novo Usuário", padding="10")
        frame_adicionar.pack(padx=20, pady=10, fill="x")

        ttk.Label(frame_adicionar, text="Matrícula:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.new_matricula_entry = ttk.Entry(frame_adicionar, width=30)
        self.new_matricula_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame_adicionar, text="Apelido/Login:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.new_login_entry = ttk.Entry(frame_adicionar, width=30)
        self.new_login_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(frame_adicionar, text="Nome Completo:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.new_full_name_entry = ttk.Entry(frame_adicionar, width=30)
        self.new_full_name_entry.grid(row=2, column=1, padx=5, pady=5)

        btn_add_user = ttk.Button(frame_adicionar, text="Adicionar Usuário", command=self.add_user)
        btn_add_user.grid(row=3, columnspan=2, pady=10)

        frame_excluir = ttk.LabelFrame(self.frame_usuarios, text="Usuários Existentes", padding="10")
        frame_excluir.pack(padx=20, pady=10, fill="both", expand=True)
        
        tree_frame = ttk.Frame(frame_excluir)
        tree_frame.pack(fill="both", expand=True)

        self.user_tree = ttk.Treeview(tree_frame, columns=("ID", "Matrícula", "Apelido/Login", "Nome Completo", "Admin"), show="headings")
        self.user_tree.heading("ID", text="ID")
        self.user_tree.heading("Matrícula", text="Matrícula")
        self.user_tree.heading("Apelido/Login", text="Apelido/Login")
        self.user_tree.heading("Nome Completo", text="Nome Completo")
        self.user_tree.heading("Admin", text="Admin")
        
        self.user_tree.column("ID", width=50, stretch=tk.NO)
        self.user_tree.column("Matrícula", width=100, stretch=tk.NO)
        self.user_tree.column("Apelido/Login", width=120, stretch=tk.NO)
        self.user_tree.column("Nome Completo", width=200, stretch=tk.YES)
        self.user_tree.column("Admin", width=80, stretch=tk.NO)

        self.user_tree.pack(side="left", fill="both", expand=True)
        
        scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=self.user_tree.yview)
        scrollbar.pack(side="right", fill="y")
        self.user_tree.configure(yscrollcommand=scrollbar.set)
        
        # Cria e popula o menu de contexto
        self.user_context_menu = tk.Menu(self.user_tree, tearoff=0)
        self.user_context_menu.add_command(label="Editar Usuário", command=self.edit_user)
        self.user_context_menu.add_command(label="Excluir Usuário", command=self.excluir_usuario)

        # Binda o evento de clique direito
        self.user_tree.bind("<Button-3>", self.show_user_context_menu)
        self.user_tree.bind('<<TreeviewSelect>>', self.on_user_select)
        
        # Carrega os usuários na Treeview
        self.load_users()

        # Adiciona o botão de Resetar Senha
        btn_reset_password = ttk.Button(frame_excluir, text="Resetar Senha para 'mudar123'", command=self.reset_user_password)
        btn_reset_password.pack(pady=10)
        
        # --- INÍCIO DA MODIFICAÇÃO ---
        # Adiciona um botão de logout na parte inferior da aba de gerenciamento de usuários
        btn_logout_user_tab = ttk.Button(self.frame_usuarios, text="Sair (Logout)", command=self.logout)
        btn_logout_user_tab.pack(side=tk.BOTTOM, pady=20)
        # --- FIM DA MODIFICAÇÃO ---

    # --- INÍCIO DAS FUNÇÕES ADICIONADAS PARA COMPLETAR O CÓDIGO ---

    def load_users(self):
        """Carrega ou recarrega os usuários na Treeview."""
        for i in self.user_tree.get_children():
            self.user_tree.delete(i)
        
        conn = None
        try:
            conn = sqlite3.connect('cadastro.db')
            cursor = conn.cursor()
            cursor.execute("SELECT id, matricula, login_apelido, username, is_admin FROM usuarios")
            users = cursor.fetchall()
            for user in users:
                is_admin_text = "Sim" if user[4] else "Não"
                self.user_tree.insert("", "end", values=(user[0], user[1], user[2], user[3], is_admin_text))
        except sqlite3.Error as e:
            messagebox.showerror("Erro de Banco de Dados", f"Não foi possível carregar os usuários: {e}")
        finally:
            if conn:
                conn.close()

    def add_user(self):
        """Adiciona um novo usuário ao banco de dados."""
        matricula = self.new_matricula_entry.get()
        login = self.new_login_entry.get()
        full_name = self.new_full_name_entry.get()
        
        if not matricula or not login or not full_name:
            messagebox.showerror("Erro", "Todos os campos para adicionar um usuário são obrigatórios.")
            return

        temp_password = "mudar123"

        conn = None
        try:
            conn = sqlite3.connect('cadastro.db')
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO usuarios (matricula, login_apelido, username, password, is_admin)
                VALUES (?, ?, ?, ?, 0)
            ''', (matricula, login, full_name, temp_password))
            conn.commit()
            messagebox.showinfo("Sucesso", f"Usuário '{login}' adicionado com sucesso!\nA senha temporária é 'mudar123'.")
            self.load_users()
            self.new_matricula_entry.delete(0, tk.END)
            self.new_login_entry.delete(0, tk.END)
            self.new_full_name_entry.delete(0, tk.END)
        except sqlite3.IntegrityError:
            messagebox.showerror("Erro", "O Apelido/Login ou Matrícula já existe.")
        except sqlite3.Error as e:
            messagebox.showerror("Erro de Banco de Dados", f"Ocorreu um erro: {e}")
        finally:
            if conn:
                conn.close()

    def on_user_select(self, event):
        """Ação a ser executada quando um usuário é selecionado na Treeview."""
        pass

    def show_user_context_menu(self, event):
        """Mostra o menu de contexto ao clicar com o botão direito em um item."""
        selected_item = self.user_tree.identify_row(event.y)
        if selected_item:
            self.user_tree.selection_set(selected_item)
            self.user_context_menu.post(event.x_root, event.y_root)

    def edit_user(self):
        """Abre a janela de edição para o usuário selecionado."""
        selected_item = self.user_tree.selection()
        if not selected_item:
            messagebox.showerror("Erro", "Por favor, selecione um usuário para editar.")
            return
        
        user_data = self.user_tree.item(selected_item[0])['values']
        EditUserWindow(self, user_data, self.load_users)

    def excluir_usuario(self):
        """Exclui o usuário selecionado."""
        selected_item = self.user_tree.selection()
        if not selected_item:
            messagebox.showerror("Erro", "Por favor, selecione um usuário para excluir.")
            return

        user_data = self.user_tree.item(selected_item[0])['values']
        user_id = user_data[0]
        user_login = user_data[2]

        if user_login == 'admin':
            messagebox.showerror("Ação Proibida", "O usuário 'admin' não pode ser excluído.")
            return

        if messagebox.askyesno("Confirmar Exclusão", f"Tem certeza que deseja excluir o usuário '{user_login}'?"):
            conn = None
            try:
                conn = sqlite3.connect('cadastro.db')
                cursor = conn.cursor()
                cursor.execute("DELETE FROM usuarios WHERE id=?", (user_id,))
                conn.commit()
                messagebox.showinfo("Sucesso", "Usuário excluído com sucesso!")
                self.load_users()
            except sqlite3.Error as e:
                messagebox.showerror("Erro de Banco de Dados", f"Ocorreu um erro: {e}")
            finally:
                if conn:
                    conn.close()
    
    def reset_user_password(self):
        """Reseta a senha do usuário selecionado para 'mudar123'."""
        selected_item = self.user_tree.selection()
        if not selected_item:
            messagebox.showerror("Erro", "Por favor, selecione um usuário para resetar a senha.")
            return

        user_data = self.user_tree.item(selected_item[0])['values']
        user_id = user_data[0]
        user_login = user_data[2]

        if messagebox.askyesno("Confirmar Reset", f"Tem certeza que deseja resetar a senha do usuário '{user_login}' para 'mudar123'?"):
            conn = None
            try:
                conn = sqlite3.connect('cadastro.db')
                cursor = conn.cursor()
                cursor.execute("UPDATE usuarios SET password = 'mudar123' WHERE id=?", (user_id,))
                conn.commit()
                messagebox.showinfo("Sucesso", f"Senha do usuário '{user_login}' resetada com sucesso!")
            except sqlite3.Error as e:
                messagebox.showerror("Erro de Banco de Dados", f"Ocorreu um erro: {e}")
            finally:
                if conn:
                    conn.close()
    # --- FIM DAS FUNÇÕES ADICIONADAS ---

# --- Ponto de Entrada da Aplicação ---
if __name__ == "__main__":
    setup_database()
    app = App()
    app.mainloop()
    