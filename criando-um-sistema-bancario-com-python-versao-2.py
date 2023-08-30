def menu(): 
    return f"""
{10*'='} MENU {10*'='}
    
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
[u] Criar usuário
[c] Criar conta
[l] Listar contas

=> """

def depositar(saldo, valor, extrato,/):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print('Depósito realizado com sucesso!')
    else:            
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

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
        numero_saques += 1
        print('Saque realizado com sucesso!')
    else:
        print("Operação falhou! O valor informado é inválido.")    
    return saldo, extrato

def vizualizar_extrato(saldo,/,*,extrato):
    print(f"\n{16*'='} EXTRATO {16*'='}")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print(f"{41*'='}")

def sair():
    return

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (apenas números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('Já existe usuário cadastrado com esse CPF!')
        return
    
    nome = input('Informe o nome completo: ')
    data_nascimento = input('Informe a data de nascimento (dd-mm-aa): ')
    endereco = input('Informe o endereço logradouro, nro - bairro - cidade/sigla do estado: ')

    usuarios.append({"nome":nome,"data_nascimento":data_nascimento,"cpf":cpf,"endereco":endereco})

    print('Usuário criado com sucesso!')

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF (apenas números): ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print('Contra criada com sucesso!')
        return {"agencia":agencia,"numero_conta":numero_conta,"usuario":usuario}
    
    print('\nUsuário não encontrado, procedimento de criação de conta encerrado!')
    return None # só pra demonstrar que essa linha existe, não sendo obrigatória

def listar_contas(contas):
    for conta in contas:
        linha = f'''
            Agência:{conta['agencia']}
            C/C:{conta['numero_conta']}
            Titular:{conta['usuario']['nome']}
        '''
        print('='*100)
        print(linha)

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
# passe de usuário em usuário na lista usuários, se o cpf que passei 
# na função for igual ao cpf do usuário percorrido na lista, ele 
# retorna o usuário, se não, a lista fica vazia
    return usuarios_filtrados[0] if usuarios_filtrados else None
# se não for uma lista vazia, ou seja, tiver o usuário, ele retorna, se não, traz None
# sempre retorna o primeiro elemento por que sempre haverá apenas um usuário por CPF

def main():

    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuarios = []
    contas = []

    while True:

        opcao = input(menu())

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato) 
            # aqui estão sendo passadas as variáveis para que utilize o valor mais atual na função
        
        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            
            saldo, extrato = sacar(
            saldo = saldo,
            valor = valor,
            extrato = extrato,
            limite = limite,
            numero_saques = numero_saques,
            limite_saques = LIMITE_SAQUES,
            )

        elif opcao == "e":
            vizualizar_extrato(saldo, extrato=extrato)

        elif opcao == "q":
            break

        elif opcao == "u":
            criar_usuario(usuarios) 
        
        elif opcao == "c":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "l":
            listar_contas(contas)

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()         