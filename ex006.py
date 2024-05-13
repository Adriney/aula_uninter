#Escreva um algoritmo que leia um nome e uma idade.
# Caso o nome digitado seja Vinicios, escreva isso na tela.
# Caso o usuário digite qualquer outro nome, verifique sua idade.
# Se for menor que 18 anos, informe que é de menor.
# Se for maior que 100 anos, informe que esta pessoa
# possivelmente não existe.

nome = input('Qual seu nome?')
idade = int(input('Qual sua idade?'))

if nome == 'Jose':
    print('Olá, Jose!')
elif idade < 18:
    print('Você não é o Jose! e é menor de idade!')
elif idade > 100:
    print('')
    print('Diferente de você, o Jose não é imortal!')