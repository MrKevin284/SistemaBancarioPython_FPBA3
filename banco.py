# banco.py

# Lista para armazenar os usuários
usuarios = []

# Lista para armazenar as contas correntes
contas = []

# Função para realizar saque
def saque(saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        return saldo, extrato + "Operação falhou! Você não tem saldo suficiente.\n"
    elif excedeu_limite:
        return saldo, extrato + "Operação falhou! O valor do saque excede o limite.\n"
    elif excedeu_saques:
        return saldo, extrato + "Operação falhou! Número máximo de saques excedido.\n"
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

    return saldo, extrato

# Função para realizar depósito
def deposito(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        extrato += "Operação falhou! O valor informado é inválido.\n"

    return saldo, extrato

# Função para exibir o extrato
def exibir_extrato(saldo, extrato):
    result = "\n================ EXTRATO ================\n"
    result += "Não foram realizadas movimentações.\n" if not extrato else extrato
    result += f"\nSaldo: R$ {saldo:.2f}\n"
    result += "==========================================\n"
    return result

# Função para cadastrar usuário
def cadastrar_usuario(nome, data_nascimento, cpf, endereco):
    # Verifica se o CPF já está cadastrado
    cpf_existente = any(usuario["cpf"] == cpf for usuario in usuarios)

    if cpf_existente:
        return "Operação falhou! Já existe um usuário cadastrado com o CPF informado.\n"

    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })
    return "Usuário cadastrado com sucesso!\n"

# Função para criar conta corrente
def criar_conta_corrente(cpf):
    # Filtra a lista de usuários buscando o CPF informado
    usuario = next((usuario for usuario in usuarios if usuario["cpf"] == cpf), None)

    if usuario is None:
        return "Operação falhou! Não foi encontrado um usuário com o CPF informado.\n"

    numero_conta = len(contas) + 1
    contas.append({
        "agencia": "0001",
        "numero_conta": numero_conta,
        "usuario": usuario,
        "saldo": 0,
        "extrato": []
    })
    return "Conta corrente criada com sucesso!\n"
