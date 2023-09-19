import tkinter as tk
import tkinter.simpledialog
from banco import *

class InterfaceBanco:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Bancário")
        self.usuario_logado = None

        # Variáveis para armazenar os valores do Entry
        self.cpf_var = tk.StringVar()
        self.nome_var = tk.StringVar()

        # Label e Entry para CPF
        self.label_cpf = tk.Label(root, text="CPF:")
        self.label_cpf.pack()
        self.entry_cpf = tk.Entry(root, textvariable=self.cpf_var)
        self.entry_cpf.pack()

        # Label e Entry para Nome
        self.label_nome = tk.Label(root, text="Nome:")
        self.label_nome.pack()
        self.entry_nome = tk.Entry(root, textvariable=self.nome_var)
        self.entry_nome.pack()

        # Botão de login
        self.botao_login = tk.Button(root, text="Login", command=self.login)
        self.botao_login.pack()

        # Label para exibir mensagem de erro
        self.label_erro = tk.Label(root, text="", fg="red")
        self.label_erro.pack()

        # Botão para ir para a tela de cadastro
        self.botao_cadastro = tk.Button(root, text="Cadastrar", command=self.abrir_tela_cadastro)
        self.botao_cadastro.pack()

    def mostrar_mensagem(self, mensagem):
        mensagem_box = tk.Toplevel(self.root)
        mensagem_box.title("Mensagem")
        mensagem_label = tk.Label(mensagem_box, text=mensagem)
        mensagem_label.pack()
        ok_button = tk.Button(mensagem_box, text="OK", command=mensagem_box.destroy)
        ok_button.pack()

    def tela_principal(self):
        self.limpar_tela()

        # Label para exibir informações do usuário
        if self.usuario_logado:
            nome = self.usuario_logado['nome']
            cpf = self.usuario_logado['cpf']
            saldo = self.usuario_logado['saldo']
            agencia = self.usuario_logado['agencia']

            info_label = tk.Label(self.root, text=f"Nome: {nome}\nCPF: {cpf}\nSaldo: R$ {saldo:.2f}\nAgência: {agencia}")
            info_label.pack()

            # Botões para realizar operações
            self.botao_saque = tk.Button(self.root, text="Realizar Saque", command=self.realizar_saque)
            self.botao_saque.pack()

            self.botao_deposito = tk.Button(self.root, text="Realizar Depósito", command=self.realizar_deposito)
            self.botao_deposito.pack()

            self.botao_consultar_saldo = tk.Button(self.root, text="Consultar Saldo", command=self.consultar_saldo)
            self.botao_consultar_saldo.pack()

            self.botao_logout = tk.Button(self.root, text="Logout", command=self.logout)
            self.botao_logout.pack()

        else:
            self.mostrar_mensagem("Este login não possui um cadastro.")

    def limpar_tela(self):
        for widget in self.root.winfo_children():
            widget.pack_forget()

    def login(self):
        cpf = self.cpf_var.get()
        nome = self.nome_var.get()

        # Verifique se o usuário existe na lista de usuários
        usuario = next((usuario for usuario in usuarios if usuario["cpf"] == cpf and usuario["nome"] == nome), None)

        if usuario:
            self.usuario_logado = usuario
            self.tela_principal()
        else:
            self.label_erro.config(text="Login ou senha incorretos.")

    def abrir_tela_cadastro(self):
        self.limpar_tela()
        self.botao_cadastro.pack_forget()
        self.botao_login.pack_forget()

        # Adicione aqui a interface para cadastro (labels, entries e botão de cadastrar)
        # Exemplo:
        # self.label_cadastro = tk.Label(self.root, text="Preencha os campos abaixo para se cadastrar:")
        # self.label_cadastro.pack()

        # self.label_nome_cadastro = tk.Label(self.root, text="Nome:")
        # self.label_nome_cadastro.pack()
        # self.entry_nome_cadastro = tk.Entry(self.root)
        # self.entry_nome_cadastro.pack()

        # self.label_cpf_cadastro = tk.Label(self.root, text="CPF:")
        # self.label_cpf_cadastro.pack()
        # self.entry_cpf_cadastro = tk.Entry(self.root)
        # self.entry_cpf_cadastro.pack()

        # self.botao_cadastrar = tk.Button(self.root, text="Cadastrar", command=self.cadastrar)
        # self.botao_cadastrar.pack()

    # Implemente a função "cadastrar" para criar um novo usuário no banco

    def logout(self):
        self.usuario_logado = None
        self.limpar_tela()
        self.cpf_var.set("")
        self.nome_var.set("")
        self.botao_login.pack()
        self.label_erro.config(text="")
    
    def realizar_saque(self):
        if self.usuario_logado:
            # Obtém o valor do saque a partir de uma caixa de diálogo
            valor_saque = float(tk.simpledialog.askstring("Saque", "Informe o valor do saque:"))
            
            if valor_saque <= 0:
                self.mostrar_mensagem("Operação falhou! O valor informado é inválido.")
            elif valor_saque > self.usuario_logado['saldo']:
                self.mostrar_mensagem("Operação falhou! Você não tem saldo suficiente.")
            else:
                # Atualiza o saldo e o extrato do usuário
                self.usuario_logado['saldo'] -= valor_saque
                self.usuario_logado['extrato'].append(f"Saque: R$ {valor_saque:.2f}")

                self.mostrar_mensagem(f"Saque de R$ {valor_saque:.2f} realizado com sucesso!")

    def realizar_deposito(self):
        if self.usuario_logado:
            # Obtém o valor do depósito a partir de uma caixa de diálogo
            valor_deposito = float(tk.simpledialog.askstring("Depósito", "Informe o valor do depósito:"))
            
            if valor_deposito <= 0:
                self.mostrar_mensagem("Operação falhou! O valor informado é inválido.")
            else:
                # Atualiza o saldo e o extrato do usuário
                self.usuario_logado['saldo'] += valor_deposito
                self.usuario_logado['extrato'].append(f"Depósito: R$ {valor_deposito:.2f}")

                self.mostrar_mensagem(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso!")

    def consultar_saldo(self):
        if self.usuario_logado:
            saldo = self.usuario_logado['saldo']
            extrato = "\n".join(self.usuario_logado['extrato'])

            mensagem = f"Saldo: R$ {saldo:.2f}\n\nExtrato:\n{extrato}"
            self.mostrar_mensagem(mensagem)


if __name__ == "__main__":
    root = tk.Tk()
    app = InterfaceBanco(root)
    root.mainloop()
