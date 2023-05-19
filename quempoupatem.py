from datetime import datetime # importa a função necessaria para registrar datas e horas

# arquivos
def salvarcliente():
    arquivo = open('clientes.txt', 'w', encoding='utf-8')
    for i in clientes:
        arquivo.write(str(i) + "\n")
    arquivo.close()

def salvarextrato():
    arquivo = open('clientes.txt', 'w', encoding='utf-8')
    for i in clientes:
        arquivo.write(str(i) + "\n")
    arquivo.close()

def lerCliente():
    arquivo = open('clientes.txt', 'r', encoding='utf-8')
    dados = arquivo.read()
    dados = dados.replace('[', '')
    dados = dados.replace(']', '')
    dados = dados.split('\n')

    for x in dados:
        cliente = x.split(',')
        print(cliente[0])
    arquivo.close()

def lerExtrato():
    arquivo = open('historico_extrato.txt', 'r', encoding='utf-8')
    dados = arquivo.read()
    dados = dados.replace('[', '')
    dados = dados.replace(']', '')
    dados = dados.split('\n')

    for x in dados:
        if len(x) <= 1:
            continue
        cliente = x.split(',')
        print(cliente[0])
    arquivo.close()
# cria a lista com todos os clientes cadastrados
clientes = []

# cria uma lista que contem todo o histórico de transaçoes de todos os clientes
historico_extrato = []

# função para buscar clientes
def BuscaCliente(cpf):
    for i in range(len(clientes)):
        if cpf == clientes[i][1]:
            return clientes[i]
    return False

# função para buscar clientes e validar a senha
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
    cliente.append(int(input("Insira seu cpf (somente números): "))) #cadastra o cpf no formato de um inteiro
    print('Qual conta você quer criar? ')
    print('Digite 1 para comum ou 2 para a conta plus, caso vc queira saber mais sobre os nossos planos, digite 0') 
    TipoDeConta = int(input())                                       #cadastra o tipo de conta

    # ao digitar 0 cliente o recebe mais imformacoes sobre os tipos de contas disponiveis, se não, o codigo pula a condição e adiciona diretamente a lista do cliente
    if TipoDeConta == 0:        
        print(
            """            - COMUM:
                - Cobra taxa de 5% a cada débito realizado
                - Permite um saldo negativo de até (R$ 1.000,00)
            
            - PLUS
                - cobra taxa de 3% a cada débito realizado
                - Permite um saldo negativo de até (R$ 5.000,00)""")
        TipoDeConta = int(input('Digite 1 para comum ou 2 para a conta plus'))      # pergunta novamente qual o tipo de conta vai ser criada
    cliente.append(TipoDeConta)                                                     # adiciona o valor referente aos tipos de conta à lista do cliente
    cliente.append(int(input("Insira o valor inicial da conta: ")))                 # cadastra o valor inicial da conta
    cliente.append(input("Crie sua senha: "))                                       # cadastra a senha do cliente

    clientes.append(cliente)  # a lista com esse cliente é inserida dentro da lista geral
    
    # cria uma lista dentro da lista de extratos com as movimentaçoes relacionadas a 1 cpf
    extrato_cpf = []

    extrato_cpf.append(cliente[1])                                                  # adiciona o cpf da pessoa à lista de extratos vinculado ao cpf dela
    historico_extrato.append(extrato_cpf)                                           # adiciona a lista vinculado ao cpf dentro da lista de extratos gerais

    # incluir a operacao à lista de extratos
    data = datetime.now().strftime(("%d / %m / %Y %H:%M:%S"))                       # cria a variavel que armazena data e hora
    saldo = cliente[3]
    cpf = cliente[1]
    valor = cliente[3]
    for i in range(len(historico_extrato)):                 # o laço percorre a lista com os extratos de todos os clientes e busca o cpf correto
        if cpf == historico_extrato[i][0]:
            historico_extrato[i].append(data)               # insere a data da operaçao à lista de registros do cliente
            historico_extrato[i].append("Criou a conta")    # insere o nome da operaçao à lista de registros do cliente
            historico_extrato[i].append(valor)              # insere o valor do débito à lista de registros do cliente
            historico_extrato[i].append(0)                  # insere o valor da taxa à lista de registros do cliente
            historico_extrato[i].append(saldo)              # insere o saldo à lista de registros do cliente

    salvarcliente()

# função que apaga clientes
def ApagaCliente():
    print()
    print("_______________________________________________________________________\n")

    # laço while para caso o cliente erre na digitação do cpf

    while True:
        cpf = int(input("Digite o cpf (somente números) da conta que você quer apagar ou digite 0 para voltar: "))  # solicita o cpf da conta

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

# função para listar todos os clientes
def ListarClientes():
    print()
    print("_______________________________________________________________________\n")
    print(clientes)

# funcao para debitos da conta
def Debito():
    print()
    print("_______________________________________________________________________\n")
    print("Para debitar da sua conta insira os dados solicitados")

    while True:                                                 # laço while para caso o cliente erre os dados
        cpf = int(input("Digite seu cpf (somente números): "))  # solicita o cpf
        senha = input("Digite sua senha: ")                     # solicita a senha
        valor = int(input("Digite o valor a ser debitado: "))   # solicita o valor a ser debitado

        cliente = BuscaClienteSenha(cpf, senha)                 # atribui a lista com os dados do cliente à variavel cliente

        if BuscaClienteSenha(cpf, senha) == False:              # caso os dados fornecido não sejam encontrados o programa retorna uma menssagem de erro
            print("Dados invalidos!")
        else:
            break
        
    temp = cliente[3]                             # variavel temporaria para armazenar a valor da conta antes de ser efetuado o débito para caso do débito não poder ser realizado
        
    if cliente[2] == 1:                           # contas comuns
        cliente[3] += (-1.05 * valor)             # debita o valor mais 5% de taxa
        taxa = 0.05 * valor
        if cliente[3] < -1000:                    # restrição do valor minimo na conta
            print('esta opereção não pode ser concluida, pois você não tem saldo suficiente')
            cliente[3] = temp                     # retorna o valor original da conta
    
    elif cliente[2] == 2:                         # contas plus
        cliente[3] += (-1.03 * valor)             # debita o valor mais 3% de taxa
        taxa = 0.03 * valor
        if cliente[3] < -5000:                    # restrição do valor minimo na conta
            print('esta opereção não pode ser concluida, pois você não tem saldo suficiente')
            cliente[3] = temp                     # retorna o valor original da conta

    # incluir a operacao à lista de extratos
    data = datetime.now().strftime(("%d / %m / %Y %H:%M:%S"))   # cria a variavel que armazena data e hora
    saldo = cliente[3]
    for i in range(len(historico_extrato)):                     # o laço percorre a lista com os extratos de todos os clientes e busca o cpf correto
        if cpf == historico_extrato[i][0]:
            historico_extrato[i].append(data)                   # insere a data da operaçao à lista de registros do cliente
            historico_extrato[i].append("Debito       ")        # insere o nome da operaçao à lista de registros do cliente
            historico_extrato[i].append(-valor)                 # insere o valor do débito à lista de registros do cliente
            historico_extrato[i].append(taxa)                   # insere o valor da taxa à lista de registros do cliente
            historico_extrato[i].append(saldo)                  # insere o saldo à lista de registros do cliente

# função para depositos
def Deposito():
    print()
    print("_______________________________________________________________________\n")
    print('Para depositar dinheiro na sua conta insira os dados solicitados')

    while True:                                                   # laço while para caso o cliente erre os dados
        cpf = int(input("Digite seu cpf (somente números): "))                      # solicita o cpf da conta
        valor = int(input("Digite o valor a ser depositado: "))   # solicita o valor a ser depositado

        cliente = BuscaCliente(cpf)                 # atribui a lista com os dados do cliente à variavel cliente

        if BuscaCliente(cpf) == False:              # caso os dados fornecido não sejam encontrados o programa retorna uma menssagem de erro
            print("Dados invalidos!")
        else:
            break

    cliente[3] += valor                             # adiciona o valor do depósito à conta
    print('Deposito realizado com sucesso')

    # incluir a operacao à lista de extratos
    data = datetime.now().strftime(("%d / %m / %Y %H:%M:%S"))   # cria a variavel que armazena data e hora
    saldo = cliente[3]
    for i in range(len(historico_extrato)):                     # o laço percorre a lista com os extratos de todos os clientes e busca o cpf correto
        if cpf == historico_extrato[i][0]:
            historico_extrato[i].append(data)                   # insere a data da operaçao à lista de registros do cliente
            historico_extrato[i].append("Deposito     ")        # insere o nome da operaçao à lista de registros do cliente
            historico_extrato[i].append(valor)                  # insere o valor do deposito à lista de registros do cliente
            historico_extrato[i].append(0)                      # insere o valor da taxa à lista de registros do cliente
            historico_extrato[i].append(saldo)                  # insere o saldo à lista de registros do cliente

# função para os extratos
def Extrato():
    print()
    print("_______________________________________________________________________\n")
    print("Prencha os dados solicitados")

    while True:                                                 # laço while para caso o cliente erre os dados
        cpf = int(input("Digite seu cpf (somente números): "))                    # solicita o cpf
        senha = input("Digite sua senha: ")                     # solicita a senha

        cliente = BuscaClienteSenha(cpf, senha)                 # atribui a lista com os dados do cliente à variavel cliente

        if BuscaClienteSenha(cpf, senha) == False:              # caso os dados fornecido não sejam encontrados o programa retorna uma menssagem de erro
            print("Dados invalidos!")
        else:
            break
    
    
    
    print("_______________________________________________________________________\n")
    print('Seu extrato')
    print('')
    print(f'Nome: {cliente[0]}')                                            # imprime o nome do cliente
    print(f'CPF: {cliente[1]}')                                             # imprime o cpf do cliente
    if cliente[2] == 1:                                                     # condição para verificar o tipo de conta
        print('Conta: Comum')                                               # imprime o tipo de conta do cliente
    else:
        print('Conta: Plus')                                                # imprime o tipo de conta do cliente
    for i in range(len(historico_extrato)):                                 # laço para percorrer a liste geral de extratos
        if cliente[1] == historico_extrato[i][0]:                           # condição para que o programa encontre a lista correte de acordo com o cpf
            for x in range(0, len(historico_extrato[i]) - 1, 5):            # laço para a impressão dos valores seguindo um padrão de repetição de 5 em 5
                # imprime os dados
                print(f'Data: {historico_extrato[i][1 + x]} | Operação: {historico_extrato[i][2 + x]} | Valor: {historico_extrato[i][3 + x]} | Tarifa: {historico_extrato[i][4 + x]} | Saldo: {historico_extrato[i][5 + x]}')
                    
# função para realizar as transaçoes entre as contas
def Trans_contas():
    print()
    print("_______________________________________________________________________\n")
    print('Para transferir seu dinheiro para outra conta insira os dados solicitados')
    while True:                                                     # laço while para caso o cliente erre os dados
        cpf = int(input("Digite seu cpf (somente números): "))                        # solicita o cpf da conta de origem
        senha = input("Digite sua senha: ")                         # solicita a senha da conta de origem
        valor = int(input("Digite o valor a ser transferido: "))    # solicita o valor a ser transferido
    
        cliente1 = BuscaClienteSenha(cpf, senha)                    # atribui a lista com os dados do cliente original à variavel cliente1

        if BuscaClienteSenha(cpf, senha) == False:                  # caso os dados fornecido não sejam encontrados o programa retorna uma menssagem de erro
            print("Dados invalidos!")
        else:
            break
    
    while True:                                       # laço while para caso o cliente erre os dados
        cpf_destino = int(input("Agora digite o cpf (somente números) da conta para a qual deseja realizar a transferencia: "))   # solicita o cpf da conta que receberá o dinheiro

        cliente2 = BuscaCliente(cpf_destino)          # atribui a lista com os dados do cliente que receberá o dinheiro  à variavel cliente2

        if BuscaCliente(cpf_destino) == False:        # caso os dados fornecido não sejam encontrados o programa retorna uma menssagem de erro
            print("Dados invalidos!")
        else:
            break

    temp1 = cliente1[3]       # variavel temporaria para armazenar o valor da conta 1 antes de ser efetuada a transferencia para caso a operação não possa ser realizada
    temp2 = cliente2[3]       # variavel temporaria para armazenar o valor da conta 2 antes de ser efetuada a transferencia para caso a operação não possa ser realizada

    if cliente1[2] == 1:                    # conta 1 comum
        cliente1[3] += (-valor)             # debita o valor da tranferencia da conta 1
        cliente2[3] += valor                # adiciona o valor da tranferencia à conta 2
        if cliente1[3] < -1000:             # restrição do valor minimo na conta
            print('Esta opereção não pode ser concluida pois você não tem saldo suficiente')
            cliente1[3] = temp1             # retorna o valor original da conta 1
            cliente2[3] = temp2             # retorna o valor original da conta 2

    elif cliente1[2] == 2:                  # conta 1 plus
        cliente1[3] += (-valor)             # debita o valor da tranferencia da conta 1
        cliente2[3] += valor                # adiciona o valor da tranferencia à conta 2
        if cliente1[3] < -5000:             # restrição do valor minimo na conta
            print('Esta opereção não pode ser concluida pois você não tem saldo suficiente')
            cliente1[3] = temp1             # retorna o valor original da conta 1
            cliente2[3] = temp2             # retorna o valor original da conta 2

    # incluir a operacao à lista de extratos
    data = datetime.now().strftime(("%d / %m / %Y %H:%M:%S"))   # cria a variavel que armazena data e hora
    saldo1 = cliente1[3]
    saldo2 = cliente2[3]

    for i in range(len(historico_extrato)):                     # o laço percorre a lista com os extratos de todos os clientes e busca o cpf correto
        if cpf == historico_extrato[i][0]:
            historico_extrato[i].append(data)                   # insere a data da operaçao à lista de registros do cliente
            historico_extrato[i].append("Tranferência ")         # insere o nome da operaçao à lista de registros do cliente
            historico_extrato[i].append(-valor)                 # insere o valor tranferido à lista de registros do cliente
            historico_extrato[i].append(0)                      # insere o valor da tarifa à lista de registros do cliente
            historico_extrato[i].append(saldo1)                 # insere o saldo à lista de registros do cliente

    for i in range(len(historico_extrato)):                     # o laço percorre a lista com os extratos de todos os clientes e busca o cpf correto
        if cpf_destino == historico_extrato[i][0]:
            historico_extrato[i].append(data)                   # insere a data da operaçao à lista de registros do cliente
            historico_extrato[i].append("Tranferência ")        # insere o nome da operaçao à lista de registros do cliente
            historico_extrato[i].append(+valor)                 # insere o valor recebido à lista de registros do cliente
            historico_extrato[i].append(0)                      # insere o valor da tarifa à lista de registros do cliente
            historico_extrato[i].append(saldo2)                 # insere o saldo à lista de registros do cliente

# função de recarga de celular
def Recarga():
    print()
    print("_______________________________________________________________________\n")
    print('Bem vindo a area de recarga do seu celular!')
    print('Para realizar a operação, complete os campos abaixo')
    print('Lembando que as recargas possuem as mesmas taxas de cobranças que os débitos')
    
    while True:                                                     # laço while para caso o cliente erre os dados
        cpf = int(input("Digite seu cpf (somente números): "))                        # solicita o cpf do cliente
        senha = input("Digite sua senha: ")                         # solicita a senha
        valor = int(input("Digite o valor da recarga: "))           # solicita o valor da recarga
        cliente = BuscaClienteSenha(cpf, senha)                     # atribui a lista com os dados do cliente à variavel cliente

        if BuscaClienteSenha(cpf, senha) == False:                  # caso os dados fornecido não sejam encontrados o programa retorna uma menssagem de erro
            print("Dados invalidos!")
        else:
            break
    
    temp = cliente[3]                             # variavel temporaria para armazenar a valor da conta antes de ser efetuada a operação para caso o cliente não tenha saldo suficiente
        
    if cliente[2] == 1:                           # contas comuns
        cliente[3] += (-1.05 * valor)             # debita o valor mais 5% de taxa
        taxa = 0.05 * valor
        if cliente[3] < -1000:                    # restrição do valor minimo na conta
            print('esta opereção não pode ser concluida, pois você não tem saldo suficiente')
            cliente[3] = temp                     # retorna o valor original da conta

    elif cliente[2] == 2:                         # contas plus
        cliente[3] += (-1.03 * valor)             # debita o valor mais 3% de taxa
        taxa = 0.03 * valor
        if cliente[3] < -5000:                    # restrição do valor minimo na conta
            print('esta opereção não pode ser concluida, pois você não tem saldo suficiente')
            cliente[3] = temp                     # retorna o valor original da conta

    # incluir a operacao à lista de extratos
    data = datetime.now().strftime(("%d / %m / %Y %H:%M:%S"))   # cria a variavel que armazena data e hora
    saldo = cliente[3]
    for i in range(len(historico_extrato)):                     # o laço percorre a lista com os extratos de todos os clientes e busca o cpf correto
        if cpf == historico_extrato[i][0]:
            historico_extrato[i].append(data)                   # insere a data da operaçao à lista de registros do cliente
            historico_extrato[i].append("Recarga      ")
            historico_extrato[i].append(-valor)                 # insere o valor do débito à lista de registros do cliente
            historico_extrato[i].append(taxa)                   # insere o valor da taxa à lista de registros do cliente
            historico_extrato[i].append(saldo)                  # insere o saldo à lista de registros do cliente

# função do menu
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
        Recarga()

# bloco do menu
while True:
    print("_______________________________________________________________________\n")
    print('_____________________Bem vindo ao banco Hugo___________________________')
    print("1 - Novo cliente")
    print("2 - Apaga cliente")
    print("3 - Listar clientes")
    print("4 - Débito")
    print("5 - Depósito")
    print("6 - Extrato")
    print("7 - Transferência entre contas")
    print("8 - Recarga de telefone")
    print("9 - Sair")

    op = int(input("insira qual operação você deseja realizar: ")) # captura o valor digitado pelo usuario e armazena na variavel op

    if op == 9:                                                    # caso op = 9, o codigo é interrompido
        break
    lerCliente()
    menu(op)                                                       # a variavel op chama as outras funções atraves da função menu