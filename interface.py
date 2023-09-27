import tkinter as tk
from tkinter import messagebox
from funcoes import *

# Função para atualizar informações do usuário
def atualizar_informacoes():
    cpf = entry_cpf.get()
    conta = next((conta for conta in contas if conta["usuario"]["cpf"] == cpf), None)
    
    if conta is not None:
        nome_usuario.set(f"Nome: {conta['usuario']['nome']}")
        saldo_conta.set(f"Saldo: R$ {conta['saldo']:.2f}")
        limite_conta.set(f"Limite: R$ {conta['limite']:.2f}")
        numero_conta.set(f"Número da Conta: {conta['numero_conta']}")
        agencia_conta.set(f"Agência: {conta['agencia']}")
        mostrar_opcoes()
        tela_login_frame.grid_forget()
    else:
        esconder_opcoes()
        messagebox.showinfo("Erro", "Conta não encontrada.")

# Função para mostrar opções de funcionalidade
def mostrar_opcoes():
    botoes_opcoes_frame.grid(row=1, column=0, padx=20, pady=10)
    botao_logout.grid(row=2, column=0, padx=20, pady=10)

# Função para esconder opções de funcionalidade
def esconder_opcoes():
    botoes_opcoes_frame.grid_forget()
    botao_logout.grid_forget()

# Função para realizar logout
def logout():
    entry_cpf.delete(0, tk.END)
    entry_cpf.focus()
    nome_usuario.set("")
    saldo_conta.set("")
    limite_conta.set("")
    numero_conta.set("")
    agencia_conta.set("")
    esconder_opcoes()
    tela_login_frame.grid(row=1, column=0, padx=20, pady=10)

# Função para abrir a tela de criar conta
def abrir_criar_conta():
    criar_conta_frame.grid(row=1, column=0, padx=20, pady=10)
    tela_login_frame.grid_forget()  # Ocultar a tela de login
    entry_nome.delete(0, tk.END)
    entry_data_nascimento.delete(0, tk.END)
    entry_cpf_criar.delete(0, tk.END)
    entry_cep.delete(0, tk.END)

# Função para cadastrar usuário e criar conta corrente
def cadastrar_usuario_e_criar_conta():
    nome = entry_nome.get()
    data_nascimento = entry_data_nascimento.get()
    cpf = entry_cpf_criar.get()
    cep = entry_cep.get()
    
    resultado = cadastrar_usuario(nome, data_nascimento, cpf, cep)
    
    if resultado == "Usuário cadastrado com sucesso!":
        criar_conta_corrente(cpf)
        criar_conta_frame.grid_forget()
        tela_login_frame.grid(row=1, column=0, padx=20, pady=10)
        entry_cpf.delete(0, tk.END)
        entry_cpf.focus()
    else:
        messagebox.showinfo("Erro", resultado)

# Função para abrir a tela de saque
def abrir_saque():
    esconder_opcoes()
    tela_saque_frame.grid(row=1, column=0, padx=20, pady=10)

# Função para realizar saque
def realizar_saque():
    numero_conta_saque = entry_numero_conta_saque.get()
    valor_saque = entry_valor_saque.get()

    resultado = saque(numero_conta_saque, float(valor_saque))

    messagebox.showinfo("Resultado", resultado)
    abrir_saque()
    
    # Função para abrir a tela de depósito
# Função para abrir a tela de depósito
def abrir_deposito():
    esconder_opcoes()
    tela_deposito_frame.grid(row=1, column=0, padx=20, pady=10)
    
    # Função para realizar depósito
def realizar_deposito():
    numero_conta_deposito = entry_numero_conta_deposito.get()
    valor_deposito = entry_valor_deposito.get()

    resultado = deposito(numero_conta_deposito, float(valor_deposito))

    messagebox.showinfo("Resultado", resultado)
    abrir_deposito()
    
    # Função para abrir a tela de transferência
def abrir_transferencia():
    esconder_opcoes()
    tela_transferencia_frame.grid(row=1, column=0, padx=20, pady=10)

# Função para realizar transferência
def realizar_transferencia():
    numero_conta_origem = entry_numero_conta_origem.get()
    numero_conta_destino = entry_numero_conta_destino.get()
    valor_transferencia = entry_valor_transferencia.get()

    resultado = transferencia(numero_conta_origem, numero_conta_destino, float(valor_transferencia))

    messagebox.showinfo("Resultado", resultado)
    abrir_transferencia()

# Criar janela principal
janela = tk.Tk()
janela.title("Sistema Bancário")

# Frame para a tela de login
tela_login_frame = tk.Frame(janela)
tela_login_frame.grid(row=1, column=0, padx=20, pady=10)

# Frame para a tela de criar conta
criar_conta_frame = tk.Frame(janela)

# Frame para a tela de saque
tela_saque_frame = tk.Frame(janela)

# Frame para a tela de depósito
tela_deposito_frame = tk.Frame(janela)

# Frame para a tela de transferências
tela_transferencia_frame = tk.Frame(janela)

# Frame para mostrar as opções de funcionalidade
botoes_opcoes_frame = tk.Frame(janela)

# Variáveis de controle
nome_usuario = tk.StringVar()
saldo_conta = tk.StringVar()
limite_conta = tk.StringVar()
numero_conta = tk.StringVar()
agencia_conta = tk.StringVar()

# Campos de texto e rótulos
label_cpf = tk.Label(tela_login_frame, text="CPF:")
entry_cpf = tk.Entry(tela_login_frame)
botao_entrar = tk.Button(tela_login_frame, text="Entrar", command=atualizar_informacoes)
botao_criar_conta = tk.Button(tela_login_frame, text="Criar Conta", command=abrir_criar_conta)

# Campos de texto e rótulos para criar conta
label_nome = tk.Label(criar_conta_frame, text="Nome:")
entry_nome = tk.Entry(criar_conta_frame)
label_data_nascimento = tk.Label(criar_conta_frame, text="Data de Nascimento (DD-MM-YYYY):")
entry_data_nascimento = tk.Entry(criar_conta_frame)
label_cpf_criar = tk.Label(criar_conta_frame, text="CPF (XXX.XXX.XXX-XX):")
entry_cpf_criar = tk.Entry(criar_conta_frame)
label_cep = tk.Label(criar_conta_frame, text="CEP (XXXXX-XX):")
entry_cep = tk.Entry(criar_conta_frame)
botao_cadastrar = tk.Button(criar_conta_frame, text="Cadastrar", command=cadastrar_usuario_e_criar_conta)
botao_voltar_criar = tk.Button(criar_conta_frame, text="Voltar", command=lambda: (criar_conta_frame.grid_forget(), tela_login_frame.grid(row=1, column=0, padx=20, pady=10)))

# Campos de texto e rótulos para saque
label_numero_conta_saque = tk.Label(tela_saque_frame, text="Número da Conta:")
entry_numero_conta_saque = tk.Entry(tela_saque_frame)
label_valor_saque = tk.Label(tela_saque_frame, text="Valor do Saque:")
entry_valor_saque = tk.Entry(tela_saque_frame)
botao_confirmar_saque = tk.Button(tela_saque_frame, text="Confirmar Saque", command=realizar_saque)
botao_voltar_saque = tk.Button(tela_saque_frame, text="Voltar", command=lambda: (tela_saque_frame.grid_forget(), mostrar_opcoes()))

# Campos de texto e rótulos para realizar depósito
label_numero_conta_deposito = tk.Label(tela_deposito_frame, text="Número da Conta:")
entry_numero_conta_deposito = tk.Entry(tela_deposito_frame)
label_valor_deposito = tk.Label(tela_deposito_frame, text="Valor do Depósito:")
entry_valor_deposito = tk.Entry(tela_deposito_frame)
botao_confirmar_deposito = tk.Button(tela_deposito_frame, text="Confirmar Depósito", command=realizar_deposito)
botao_voltar_opcoes = tk.Button(tela_deposito_frame, text="Voltar", command=lambda: (tela_deposito_frame.grid_forget(),mostrar_opcoes()))

# Campos de texto e rótulos para transferência
label_numero_conta_origem = tk.Label(tela_transferencia_frame, text="Conta de Origem:")
entry_numero_conta_origem = tk.Entry(tela_transferencia_frame)
label_numero_conta_destino = tk.Label(tela_transferencia_frame, text="Conta de Destino:")
entry_numero_conta_destino = tk.Entry(tela_transferencia_frame)
label_valor_transferencia = tk.Label(tela_transferencia_frame, text="Valor da Transferência:")
entry_valor_transferencia = tk.Entry(tela_transferencia_frame)
botao_confirmar_transferencia = tk.Button(tela_transferencia_frame, text="Confirmar Transferência", command=realizar_transferencia)
botao_voltar_transferencia = tk.Button(tela_transferencia_frame, text="Voltar", command=lambda: (tela_transferencia_frame.grid_forget(), mostrar_opcoes()))

# Botões de funcionalidade
botao_saque = tk.Button(botoes_opcoes_frame, text="Realizar Saque", command=abrir_saque)
botao_deposito = tk.Button(botoes_opcoes_frame, text="Realizar Depósito", command=abrir_deposito)
botao_extrato = tk.Button(botoes_opcoes_frame, text="Exibir Extrato", command=lambda: messagebox.showinfo("Aviso", "Funcionalidade de Extrato ainda não implementada."))
botao_transferencia = tk.Button(botoes_opcoes_frame, text="Realizar Transferência", command=abrir_transferencia)
botao_atualizar_limite = tk.Button(botoes_opcoes_frame, text="Atualizar Limite de Transferência", command=lambda: messagebox.showinfo("Aviso", "Funcionalidade de Atualização de Limite de Transferência ainda não implementada."))

# Botão de logout
botao_logout = tk.Button(janela, text="Logout", command=logout)

# Posicionamento dos elementos na tela de login
label_cpf.grid(row=0, column=0)
entry_cpf.grid(row=0, column=1)
botao_entrar.grid(row=1, column=0, columnspan=2, pady=10)
botao_criar_conta.grid(row=2, column=0, columnspan=2)

# Posicionamento dos elementos na tela de criar conta
label_nome.grid(row=0, column=0)
entry_nome.grid(row=0, column=1)
label_data_nascimento.grid(row=1, column=0)
entry_data_nascimento.grid(row=1, column=1)
label_cpf_criar.grid(row=2, column=0)
entry_cpf_criar.grid(row=2, column=1)
label_cep.grid(row=3, column=0)
entry_cep.grid(row=3, column=1)
botao_cadastrar.grid(row=4, column=0, columnspan=2, pady=10)
botao_voltar_criar.grid(row=5, column=0, columnspan=2, pady=10)

# Posicionamento dos elementos na tela de saque
label_numero_conta_saque.grid(row=0, column=0)
entry_numero_conta_saque.grid(row=0, column=1)
label_valor_saque.grid(row=1, column=0)
entry_valor_saque.grid(row=1, column=1)
botao_confirmar_saque.grid(row=2, column=0, columnspan=2, pady=10)
botao_voltar_saque.grid(row=3, column=0, columnspan=2, pady=10)

# Posicionamento dos elementos na tela de depósito
label_numero_conta_deposito.grid(row=0, column=0)
entry_numero_conta_deposito.grid(row=0, column=1)
label_valor_deposito.grid(row=1, column=0)
entry_valor_deposito.grid(row=1, column=1)
botao_confirmar_deposito.grid(row=2, column=0, columnspan=2, pady=10)
botao_voltar_opcoes.grid(row=3, column=0, columnspan=2, pady=10)

# Posicionamento dos elementos na tela de transferência
label_numero_conta_origem.grid(row=0, column=0)
entry_numero_conta_origem.grid(row=0, column=1)
label_numero_conta_destino.grid(row=1, column=0)
entry_numero_conta_destino.grid(row=1, column=1)
label_valor_transferencia.grid(row=2, column=0)
entry_valor_transferencia.grid(row=2, column=1)
botao_confirmar_transferencia.grid(row=3, column=0, columnspan=2, pady=10)
botao_voltar_transferencia.grid(row=4, column=0, columnspan=2, pady=10)

# Posicionamento dos elementos na tela de informações do usuário
info_usuario_label = tk.Label(janela, textvariable=nome_usuario)
info_saldo_label = tk.Label(janela, textvariable=saldo_conta)
info_limite_label = tk.Label(janela, textvariable=limite_conta)
info_numero_conta_label = tk.Label(janela, textvariable=numero_conta)
info_agencia_label = tk.Label(janela, textvariable=agencia_conta)

info_usuario_label.grid(row=0, column=1, padx=10)
info_saldo_label.grid(row=1, column=1, padx=10)
info_limite_label.grid(row=2, column=1, padx=10)
info_numero_conta_label.grid(row=3, column=1, padx=10)
info_agencia_label.grid(row=4, column=1, padx=10)

# Posicionamento dos botões de funcionalidade
botao_saque.grid(row=0, column=0, padx=10, pady=5)
botao_deposito.grid(row=0, column=1, padx=10, pady=5)
botao_extrato.grid(row=0, column=2, padx=10, pady=5)
botao_transferencia.grid(row=1, column=0, padx=10, pady=5)
botao_atualizar_limite.grid(row=1, column=1, padx=10, pady=5)

# Ocultar opções de funcionalidade inicialmente
esconder_opcoes()

janela.mainloop()
