print('CONCEITO DE AVALIAÇÃO DOS ALUNOS v0.01\n')
while True:  # inicia o laço de repetição
    print('OPÇÕES:')
    print('1 - Iniciar')
    print('2 - Encerrar')
    conceito = '?'
    inicia = input('Digite a opção desejada: ')  # digita '1' para iniciar  ou outra tecla para encerrar
    if inicia == '1':  # Verifica se o usuário digitou '1' para iniciar o programa
        nome = input('Digite o nome do aluno: ')  # solicita ao usuario que digite o nome do aluno
        while True:
            try:
                nota = float(input('Digite a nota do aluno (0 - 10): '))  # solicita ao usuario que digite a nota
                break
            except ValueError:
                print('Valor inválido! Digite um valor numérico entre 0 e 10')
        if nota <= 2.9:  # caso nota menor ou igual 2.9,
            conceito = 'E'  # atribui 'E' para a variavel conceito
        elif 0 > nota <= 4.9:  # caso nota maior que 2.9 e menor ou igual 4.9,
            conceito = 'D'  # atribui 'D' para a variavel conceito
        elif 4.9 < nota <= 6.9:  # caso nota maior que 4.9 e menor ou igual 6.9,
            conceito = 'C'  # atribui 'C' para a variavel conceito
        elif 6.9 < nota <= 8.9:  # caso nota maior que 6.9 e menor ou igual 8.9,
            conceito = 'B'  # atribui 'B' para a variavel conceito
        elif 8.9 < nota <= 10:  # caso nota maior que 8.9 e menor ou igual 10,
            conceito = 'A'  # atribui 'A' para a variavel conceito
        else:  # caso nota não corresponda a nenhuma das condições anteriores,
            print('Nota inválida!\n')
        if 0 <= nota <= 10:
            print('O aluno {} tirou nota {} e se enquadra no conceito {}\n'.format(nome, nota, conceito))  # imprime
    elif inicia == '2':  # caso o ususario digite '2'
        print('ENCERRANDO O PROGRAMA ...')  # imprime a mensagem
        break  # Encerra o laço de repetição
    else:
        continue
