def menu():
    menu = """
    ============== MENU ==============
    [d] Depositar
    [s] Sacar
    [e] Exibir Extrato
    [nc] Nova Conta
    [lc] Listar contas
    [nu] Novo Usuario
    [q] Sair
    => """
    return input(menu)

def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado.")
    else:
        print("Não foi possível. O valor informado é inválido.")
    return saldo, extrato

def sacar(saldo, valor, extrato, numero_saques, limite, LIMITE_SAQUES):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Não foi possível. Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Não foi possível. O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Não foi possível. Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado.")
    
    else:
        print("Não foi possível. O valor informado é inválido.")
    return saldo, extrato, numero_saques

def exibir_extrato (saldo, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def nova_conta(agencia, numero_conta, usuarios, contas):
    agencia = "0001"
    numero_conta = len(contas) +1
    cpf = input("Digite o CPF do usuário: ")

    usuario = filtrar_usuario(cpf, usuarios)
    if not usuario:
        print("Usuário não encontrado. Por favor, crie um usuário para que possa criar uma conta.")
        return
    
    else:
        contas.append({"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario})
        print(f"Conta criada. Número da conta: {numero_conta}")

def listar_contas(contas):
    if not contas:
        print("Não existem contas cadastradas.")
        return
    for conta in contas:
        linha = f"Agência: {conta['agencia']} / Número da conta: {conta['numero_conta']} / Titular: {conta['usuario']['nome']}"
        print(linha)

def novo_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")

    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Já existe usuário com esse CPF.")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com sucesso.")

def filtrar_usuario(cpf, usuarios):
    usuario_filtrado = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuario_filtrado[0] if usuario_filtrado else None

saldo = 0
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
limite = 500
usuarios = []
contas = []

while True:

    opcao = menu()

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        saldo, extrato = depositar(saldo, valor, extrato)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        saldo, extrato, numero_saques = sacar(saldo, valor, extrato, numero_saques, limite, LIMITE_SAQUES)

    elif opcao == "e":
        exibir_extrato(saldo, extrato)
    
    elif opcao == "nc":
        nova_conta("0001", len(contas) +1, usuarios, contas)

    elif opcao == "lc":
        listar_contas(contas)

    elif opcao == "nu":
        novo_usuario(usuarios)
        
    elif opcao == "q":
        break

    else:
        print("Operação inválida. Por favor, selecione novamente a operação desejada.")