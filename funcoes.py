import re

# Lista para armazenar os usuários
usuarios = []

# Lista para armazenar as contas correntes
contas = []

# Função para realizar saque
def saque(numero_conta, valor):
    conta = next((conta for conta in contas if conta["numero_conta"] == numero_conta), None)
    if conta is not None:
        saldo = conta['saldo']
        extrato = conta['extrato']
        limite = conta['limite']
        numero_saques = conta['numero_saques']
        limite_saques = conta['limite_saques']

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= limite_saques

        if excedeu_saldo:
            return "Operação falhou! Você não tem saldo suficiente."
        elif excedeu_limite:
            return "Operação falhou! O valor do saque excede o limite."
        elif excedeu_saques:
            return "Operação falhou! Número máximo de saques excedido."
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        conta['saldo'] = saldo
        conta['extrato'] = extrato
        conta['numero_saques'] = numero_saques
        return "Saque realizado com sucesso."
    else:
        return "Conta não encontrada."

# Função para realizar depósito
def deposito(numero_conta, valor):
    conta = next((conta for conta in contas if conta["numero_conta"] == numero_conta), None)
    if conta is not None:
        saldo = conta['saldo']
        extrato = conta['extrato']
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            conta['saldo'] = saldo
            conta['extrato'] = extrato
            return "Depósito realizado com sucesso."
        else:
            return "Operação falhou! O valor informado é inválido."
    else:
        return "Conta não encontrada."

# Função para exibir o extrato
def exibir_extrato(numero_conta):
    conta = next((conta for conta in contas if conta["numero_conta"] == numero_conta), None)
    if conta is not None:
        saldo = conta['saldo']
        extrato = conta['extrato']
        return extrato, f"Saldo: R$ {saldo:.2f}"
    else:
        return "Conta não encontrada."

# Função para cadastrar usuário
def cadastrar_usuario(nome, data_nascimento, cpf, cep):
    # Validar formato de data (DD-MM-YYYY)
    if not re.match(r'\d{2}-\d{2}-\d{4}', data_nascimento):
        return "Operação falhou! Data de nascimento no formato incorreto (DD-MM-YYYY)."

    # Validar formato de CPF (inserir pontos e traço)
    if not re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf):
        return "Operação falhou! CPF no formato incorreto (XXX.XXX.XXX-XX)."

    # Validar formato de CEP
    if not re.match(r'\d{5}-\d{3}', cep):
        return "Operação falhou! CEP no formato incorreto (XXXXX-XXX)."

    # Verifica se o CPF já está cadastrado
    cpf_existente = any(usuario["cpf"] == cpf for usuario in usuarios)

    if cpf_existente or not nome or not cpf:
        return "Operação falhou! Preencha todos os campos e/ou CPF já cadastrado."
    else:
        usuarios.append({
            "nome": nome,
            "data_nascimento": data_nascimento,
            "cpf": cpf,
            "cep": cep
        })
        return "Usuário cadastrado com sucesso!"

# Função para criar conta corrente
def criar_conta_corrente(cpf):
    usuario = next((usuario for usuario in usuarios if usuario["cpf"] == cpf), None)

    if usuario is None:
        return "Operação falhou! Não foi encontrado um usuário com o CPF informado."
    else:
        conta_existente = any(conta["usuario"]["cpf"] == cpf for conta in contas)

        if conta_existente:
            return "Operação falhou! O usuário já possui uma conta corrente."
        else:
            numero_conta = len(contas) + 1
            contas.append({
                "agencia": "0001",
                "numero_conta": numero_conta,
                "usuario": usuario,
                "saldo": 0,
                "limite": 500,
                "extrato": "",
                "numero_saques": 0,
                "limite_saques": 3,
                "limite_transferencia": 500  # Limite de transferência inicial
            })
            return "Conta corrente criada com sucesso!"

# Função para realizar transferência
def transferencia(numero_conta_origem, numero_conta_destino, valor):
    conta_origem = next((conta for conta in contas if conta["numero_conta"] == numero_conta_origem), None)
    conta_destino = next((conta for conta in contas if conta["numero_conta"] == numero_conta_destino), None)

    if conta_origem is None or conta_destino is None:
        return "Operação falhou! Conta de origem ou destino não encontrada."
    elif valor > conta_origem['saldo']:
        return "Operação falhou! Você não tem saldo suficiente para realizar a transferência."
    elif valor > conta_origem['limite_transferencia']:
        return "Operação falhou! O valor da transferência excede o limite permitido."
    else:
        saldo_origem = conta_origem['saldo']
        extrato_origem = conta_origem['extrato']

        saldo_destino = conta_destino['saldo']
        extrato_destino = conta_destino['extrato']

        saldo_origem -= valor
        extrato_origem += f"Transferência enviada para Conta {numero_conta_destino}: R$ {valor:.2f}\n"

        saldo_destino += valor
        extrato_destino += f"Transferência recebida da Conta {numero_conta_origem}: R$ {valor:.2f}\n"

        conta_origem['saldo'] = saldo_origem
        conta_origem['extrato'] = extrato_origem

        conta_destino['saldo'] = saldo_destino
        conta_destino['extrato'] = extrato_destino

        return "Transferência realizada com sucesso."

# Função para consultar saldo
def consultar_saldo(numero_conta):
    conta = next((conta for conta in contas if conta["numero_conta"] == numero_conta), None)
    if conta is not None:
        saldo = conta['saldo']
        return f"Saldo: R$ {saldo:.2f}"
    else:
        return "Conta não encontrada."

# Função para atualizar limite de transferência
def atualizar_limite_transferencia(numero_conta, novo_limite):
    conta = next((conta for conta in contas if conta["numero_conta"] == numero_conta), None)
    if conta is not None:
        conta['limite_transferencia'] = novo_limite
        return "Limite de transferência atualizado com sucesso."
    else:
        return "Conta não encontrada."

# Função para consultar conta por CPF
def consultar_conta_por_cpf(cpf):
    conta = next((conta for conta in contas if conta["usuario"]["cpf"] == cpf), None)
    if conta is not None:
        numero_conta = conta['numero_conta']
        saldo = conta['saldo']
        return f"Conta: {numero_conta}, Saldo: R$ {saldo:.2f}"
    else:
        return "Conta não encontrada."
