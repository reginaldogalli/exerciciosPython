import random  # importa biblioteca random


def cadastra(nome, vezes):  # define função cadastra
    global listaSorteio  # define a variavel como global
    for i in range(0, vezes):  # insere o nome na lista de acordo com o valor doado
        listaSorteio.append(nome)


print('LISTA SORTEIO v0.01\n')  # mensagem inicial
listaSorteio = []  # cria a lista para o sorteio
opcao = 1
doacao = 0
print('Insira uma doação para começar. ')
while True:  # inicia o laço principal
    while opcao == 1:  # inicia o laço secundário
        try:  # verifica se os dados inseridos sao do tipo float
            doacao = float(input('\nDigite o valor da doação (Mínimo R$ 10,00 para entrar no sorteio): R$'))  # Valor
            break
        except ValueError:
            print('\nOops! valor inválido. Tente novamente.')  # Mensagem exibida caso dado incompátivel
    doador = input('Digite o nome do doador: ')  # Recebe o nome do doador
    x = doacao//10  # divide o valor doado por dez e verifica apenas a parte inteira
    cadastra(doador, int(x))  # executa a funcao cadastra
    print('\nDoação cadastrada com sucesso!')
    print('\nLista do sorteio atualizada:')
    print(listaSorteio)  # imprime a lista do sorteio
    print('\nOPÇÕES:')
    print('1 - Inserir nova doação')
    print('2 - Realizar sorteio')
    while True:
        try:  # verifica se os dados inseridos sao válidos
            opcao = int(input('Selecione a opção desejada:'))
            break
        except ValueError:
            print('\nOops! Opção Inválida. Selecione 1 ou 2.')
            print('\nOPÇÕES:')
            print('1 - Inserir nova doação')
            print('2 - Realizar sorteio')
    if opcao == 1:  # se digitar 1, retorna para o inicio do laço primário
        continue
    elif opcao == 2:  # se digitar 2, finaliza o laço primário
        break
    else:  # se digitar algo diferente, inicia outro laço até que digite um valor válido
        while opcao != 1 and opcao != 2:
            while True:
                try:
                    print('\nOops! Opção inválida. Selecione 1 ou 2.')
                    print('\nOPÇÕES:')
                    print('1 - Inserir nova doação')
                    print('2 - Realizar sorteio')
                    opcao = int(input('Selecione 1 ou 2: '))
                    break
                except ValueError:
                    continue
    if opcao == 2:
        break
print('\nEmbaralhando lista...')
random.shuffle(listaSorteio)  # embaralha lista
print(listaSorteio)  # imprime lista embaralhada
sorteado = random.choice(listaSorteio)  # realiza o sorteio
print('\nO ganhador do sorteio foi: {}'.format(sorteado).upper())  # imprime o sorteado na tela
print('\n Fim do Programa.')  # imprime mensagem de encerramento
