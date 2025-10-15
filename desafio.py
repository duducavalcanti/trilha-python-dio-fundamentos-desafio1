"""
Retorna o menu de opções do sistema bancário como string.
"""
def exibir_menu():

    menu = """
[d]\tDepositar
[s]\tSacar
[e]\tExtrato
[nu]\tNovo usuário
[lu]\tListar usuários
[nc]\tNova conta
[lc]\tListar contas
[lcu]\tListar contas por usuário
[q]\tSair
=> """
    return menu


"""
Função responsável por realizar depósitos em uma conta bancária.
Recebe o saldo atual, o valor do depósito e o extrato.
"""
def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato


"""
Função responsável por efetuar saques em uma conta bancária.
Valida saldo, limite e quantidade máxima de saques diários.
"""
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques = numero_saques + 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques


"""
Função responsável por exibir o extrato de movimentações da conta.
Mostra depósitos, saques e o saldo atual.
"""
def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("===========================================")


"""
Função que valida um CPF conforme o algoritmo da Receita Federal.
Remove caracteres não numéricos e confere os dígitos verificadores.
"""
def validar_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))  # mantém apenas números

    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma * 10 % 11) % 10

    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma * 10 % 11) % 10

    return cpf[-2:] == f"{digito1}{digito2}"


"""
Função que busca um usuário pelo CPF dentro da lista de usuários.
Retorna o dicionário do usuário encontrado ou None se não existir.
"""
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


"""
Função que cadastra um novo usuário no sistema bancário.
Solicita CPF, nome, data de nascimento e endereço, 
garantindo que o CPF seja válido e único.
"""
def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ").strip()

    if not validar_cpf(cpf):
        print("CPF inválido!")
        return

    usuario_existente = filtrar_usuario(cpf, usuarios)
    if usuario_existente:
        print("Já existe um usuário com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nº, bairro, cidade/sigla do estado): ")

    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco,
        "contas": []  # <-- inicializa lista de contas do usuário
    })

    print("Usuário criado com sucesso!")


"""
Função para listar todos os usuários cadastrados no sistema.
Exibe nome, CPF e endereço de cada usuário.
"""
def listar_usuarios(usuarios):
    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return

    print("\n========== LISTA DE USUÁRIOS ==========")
    for usuario in usuarios:
        print(f"Nome: {usuario['nome']}")
        print(f"CPF: {usuario['cpf']}")
        print(f"Data de Nascimento: {usuario['data_nascimento']}")
        print(f"Endereço: {usuario['endereco']}")
        print(f"Total de Contas: {len(usuario.get('contas', []))}")
        print("----------------------------------------")
    print("========================================\n")


"""
Função responsável por criar uma nova conta bancária.
Cada conta é vinculada a um usuário existente através do CPF.
"""
def criar_conta(agencia, numero_conta, usuarios):
    """
    Cria uma conta vinculada a um usuário existente.
    Retorna o dicionário da conta se criada, caso contrário None.
    Também anexa a conta na lista interna do usuário para suportar várias contas.
    """
    cpf = input("Informe o CPF do usuário: ").strip()

    if not validar_cpf(cpf):
        print("CPF inválido!")
        return

    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        conta = {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
        # adiciona a conta à lista de contas do usuário (permite múltiplas contas)
        usuario.setdefault("contas", []).append({
            "agencia": agencia,
            "numero_conta": numero_conta
        })
        print("Conta criada com sucesso!")
        return conta

    print("Usuário não encontrado! Fluxo de criação de conta encerrado.")
    return None


"""
Função que lista todas as contas cadastradas no sistema,
exibindo agência, número da conta e nome do titular.
"""
def listar_contas(contas):
    """Lista todas as contas cadastradas (global)."""
    if not contas:
        print("Nenhuma conta cadastrada.")
        return

    for conta in contas:
        linha = f"""
Agência: {conta['agencia']}
C/C: {conta['numero_conta']}
Titular: {conta['usuario']['nome']} (CPF: {conta['usuario']['cpf']})
"""
        print(linha)


"""
Função que lista todas as contas cadastradas no sistema para
um usuário específico(CPF).
"""
def listar_contas_por_usuario(cpf, usuarios):
    if not validar_cpf(cpf):
        print("CPF inválido!")
        return
    
    usuario = filtrar_usuario(cpf, usuarios)
    if not usuario:
        print("Usuário não encontrado.")
        return

    contas_usuario = usuario.get("contas", [])
    if not contas_usuario:
        print(f"O usuário {usuario['nome']} não possui contas vinculadas.")
        return

    print(f"Contas do usuário {usuario['nome']} (CPF: {usuario['cpf']}):")
    for c in contas_usuario:
        print(f"  - Agência: {c['agencia']} | Conta: {c['numero_conta']}")


"""
Função principal que inicializa e gerencia o fluxo do sistema bancário,
controlando o menu de operações e a interação com o usuário.
"""
def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    menu = exibir_menu()

    while True:
        opcao = input(menu)

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "lu":
            listar_usuarios(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "lcu":
            cpf_busca = input("Informe o CPF do usuário (somente números): ").strip()
            listar_contas_por_usuario(cpf_busca, usuarios)

        elif opcao == "q":
            print("Saindo do sistema... até logo!")
            break

        else:
            print("Operação inválida, tente novamente.")


if __name__ == "__main__":
    main()