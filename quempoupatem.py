
# cria a lista com todos os clientes cadastrados
clientes = []

# função para buscar clientes
def BuscaCliente(cpf):
    for i in range(len(clientes)):
        if cpf == clientes[i][2]:
            return clientes[i]

def BuscaClienteSenha(cpf, senha):
    for i in range(len(clientes)):
        if cpf == clientes[i][1] and senha == clientes[i][4]:
            return clientes[i]
    return False


# função que cria um novo cliente
def NovoCliente():
    print("_______________________________________________________________________\n")
    
    cliente = []  # cada vez que essa função for chamada ela cria uma nova lista para inserir os dados desse cliente específico

    print("Dados solicitados") 

    # o cliente insere os dados diretamente dentro da lista

    cliente.append(input("Insira seu nome: "))                       #cadastra o nome
    cliente.append(int(input("Insira seu cpf: ")))                   #cadastra o cpf no formato de um inteiro
    cliente.append(input("Qual conta você quer criar? "))            #cadastra o tipo de conta
    cliente.append(int(input("Insira o valor inicial da conta: ")))  #cadastra o valor inicial da conta
    cliente.append(input("Crie sua senha: "))                        #cadastra a senha do cliente

    clientes.append(cliente)  # a lista com esse cliente é inserida dentro da lista geral
    

# função que apaga clientes

def ApagaCliente():
    print()
    print("_______________________________________________________________________\n")

    # laço while para caso o cliente erre na digitação do cpf

    while True:
        cpf = int(input("digite o cpf da conta que você quer apagar ou digite 0 para voltar: "))    # solicita o cpf da conta

        if cpf == 0:  # se  o for igual a 0 interrompe a operação retornando para o menu
            break
        
        for i in range(len(clientes)):  # laço for percorre a lista com todos os clientes e procura aquele que tenha o cpf igual ao digitado

            if  cpf == clientes[i][1]:  # cria a condição para deletar toda a lista com as informações do cliente com o cpf digitado
                clientes.pop(i)
                print()
                print("Cliente deletado com sucesso")
                return
        print()
        print("Cliente não encontrado\n")
        print("Tente novamente\n")


#lista todos os clientes
def ListarClientes():
    print(clientes)

# funcao para depositas na conta
def Debito():
    print("Dados solicitados")

    while True:
        cpf = int(input("Digite seu cpf: "))
        senha = input("Digite sua senha: ")
        valor = int(input("Digite o valor a ser debitado: "))

        print(BuscaClienteSenha(cpf, senha))

        if BuscaClienteSenha(cpf, senha) == False:
            print("Dados invalidos!")
        else:
            break
        
    if BuscaClienteSenha(cpf, senha) != False:
        if BuscaCliente(cpf)[2] == 1:   # comum
            BuscaCliente(cpf)[3] += (valor - 0.05 * valor) 
        elif BuscaCliente(cpf)[2] == 2:   # plus
            BuscaCliente(cpf)[3] += (valor - 0.03 * valor)
    

def Deposito():
    print("Dados solicitados")
    cpf = input("Insira seu cpf: ")
    valor = int(input("Digite o valor do deposito: "))
    print(cpf, valor)

def Extrato():
    print("Dados solicitados")
    cpf = input("Insira seu cpf: ")
    senha = input("Digite sua senha: ")
    print(cpf, senha)

def Trans_contas():
    print("Dados solicitados")
    cpf = input("Insira seu cpf: ")
    senha = input("Digite sua senha: ")
    cpfdestino = input("Insira seu cpf da conta que você deseja transferir: ")
    valor = int(input("Digite o valor da transferência: "))
    print(cpf, senha, valor, cpfdestino)

def Investimento():
    cpf = input("Insira seu cpf: ")
    senha = input("Digite sua senha: ")
    valor = int(input("Digite o valor a ser investido: "))
    print(cpf, senha, valor)


def menu(menu):
    if menu == 1:
        NovoCliente()
    elif menu == 2:
        ApagaCliente()
    elif menu == 3:
        ListarClientes()
    elif menu == 4:
        Debito()
    elif menu == 5:
        Deposito()
    elif menu == 6:
        Extrato()
    elif menu == 7:
        Trans_contas()
    elif menu == 8:
        Investimento()
    

while True:
    print("_______________________________________________________________________\n")
    print("1 - Novo cliente")
    print("2 - Apaga cliente")
    print("3 - Listar clientes")
    print("4 - Débito")
    print("5 - Depósito")
    print("6 - Extrato")
    print("7 - Transferência entre contas")
    print("8 - Operação livre")
    print("9 - Sair")

    op = int(input("insira qual operação você deseja realizar: "))

    if op == 9:
        break
    
    menu(op)