Open In Colab
from operator import itemgetter  # importa a funcao itemgetter da biblioteca operator
 
 
print('TABELA DE PRODUTOS ARMAZANADOS v0.01\n')  # mensagem inicial
print('Iniciando o sistema para cadastro de estoque...')
lista = []  # cria a lsita
dicionario = {}  # cria o dicionario
while True:  # laço principal
    while True:  # laço secundário (try)
        try:  # verifica se os dados inseridos sao do tipo int
            dicionario['Codigo'] = int(input('\nDigite o código do produto ou 0 para encerrar o cadastro: '))  # solicita ao usuario para inserir um valor a ser gravado na chave Codigo
            break  # caso o valor seja int finaliza o laço secundário
        except ValueError:  # caso valor nao seja int exibe mensagem3
            print('\nValor inválido. Insira um valor numérico.')
    if dicionario['Codigo'] == 0:  # Verifica de o valor digitado é igual 0
        break  # caso for 0, encerra o laço principal
    else:  # caso não for continua o laço
        while True:  # laço secundário (try)
            try:  # verifica se os dados inseridos sao do tipo int
                dicionario['Estoque'] = int(input('\nDigite a quantidade em estoque do produto: '))  # solicita ao usuario para inserir um valor a ser gravado na chave Estoque
                break  # caso o valor seja int finaliza o laço secundário
            except ValueError:  # caso valor nao seja int exibe mensagem
                print('\nValor inválido. Insira um valor numérico.')
        while True:  # laço secundário (try)
            try:  # verifica se os dados inseridos sao do tipo int
                dicionario['Minimo'] = int(input('\nDigite o estoque minimo do produto: '))  ## solicita ao usuario para inserir um valor a ser gravado na chave Minimo
                break  # caso o valor seja int finaliza o laço secundário
            except ValueError:  # caso valor nao seja int exibe mensagem
                print('\nValor inválido. Insira um valor numérico.')
        lista.append(dicionario.copy())  # Grava dicionário no final da lista
print('\nEsta é a Lista de Produtos Armazenados:')
print(lista)  # imprime a lista gravada
t = len(lista)  # verifica quantos índices tem na lista
print('\n|   TABELA DE ESTOQUE     |')  # imprime a lsita formatada como uma tabela
print('--------------------------')
print('|Código | Estoque | Mínimo|')
print('--------------------------')
for i in range(t):  # imprime linha a linha da tabela utilizando um laço for
    print('|  ' + str(lista[i]['Codigo']).zfill(2) + '   |   ' + str(lista[i]['Estoque']).zfill(2) + '    |   ' + str(lista[i]['Minimo']).zfill(2) + '  |')
    print('--------------------------')  # converte os values do dicionario para str. Utiliza o método zfill para adicionar um zero à esquerda.
listaOrdenada = sorted(lista, key=itemgetter('Codigo'))  # atribui a lista ordenada utilizando o itemgetter
print('\n')
print(listaOrdenada)  # imprime a lista ordenada
print('\n|   TABELA DE ESTOQUE     |')
print('--------------------------')
print('|Código | Estoque | Mínimo|')
print('--------------------------')
for i in range(t):  # imprime linha a linha da tabela utilizando um laço for
    print('|  ' + str(listaOrdenada[i]['Codigo']).zfill(2) + '   |   ' + str(listaOrdenada[i]['Estoque']).zfill(2) + '    |   ' + str(listaOrdenada[i]['Minimo']).zfill(2) + '  |')
    print('--------------------------')   # converte os values do dicionario para str. Utiliza o método zfill para adicionar um zero à esquerda.
