clientes = []

def lerCliente():
    global clientes  # Acessa a variável clientes globalmente
    auxiliar = []
    arquivo = open('clientes.txt', 'r', encoding='utf-8')                             # abre o arquivo

    for linha in arquivo.readlines():
        linha = linha.strip()                                                         # remove espaços em branco e \n no início e fim da linha
        linha = linha.replace("'", '')                                                # remove as aspas
        temp = linha[1:-1].split(', ')                                                # remove os [] e divide a linha em listas nos pontos em que há vírgula e espaço

        cliente = [temp[0], int(temp[1]), int(temp[2]), float(temp[3]), temp[4]]      # converte os valores apropriados para cada índice da sublista

        auxiliar.append(cliente)                                                      # adiciona a lista cliente à lista auxiliar

    clientes = auxiliar[:]                                                            # atribui a lista auxiliar à lista clientes

    arquivo.close()                                                                   # encerra a operação com o arquivo

lerCliente()
print(clientes)