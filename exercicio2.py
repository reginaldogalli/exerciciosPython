def juntar(arg1, arg2, arg3):  # define a função juntar
    servidor = '@algoritmos.com.br'  # salva o servidor de email em uma vari[avel
    return arg1[0] + arg2 + arg3 + servidor  # retorna a junção da inicial + sobrenome + RU + servidor
 
 
# Programa Principal
print('GERADOR DE E-MAILS v0.01\n')  # mensagem inicial
nome = input('Digite o seu nome: ')  # recebe a string para a variável nome
sobrenome = input('Digite o seu sobrenome: ')  # recebe a string para a variável sobrenome
ru = input('Digite o seu RU: ')  # recebe a string para a variável ru
email = juntar(nome.lower(), sobrenome.replace(' ', '').lower(), ru[-2:])  # atribui o retorno da função para o email
print('Sr(a). {} {}, seu email é {}'.format(nome, sobrenome, email))  # Exibe a mensagem com o email
print('ENCERRANDO O PROGRAMA...')  # mensagem de encerramento
