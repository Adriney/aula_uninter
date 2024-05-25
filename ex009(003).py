#Escreva um programa que calcule o preço a pagar pelo fornecimento
# de energia elétrica. Pergunte a quantidade de Kwhconsumida e
# o tipo de instalção:R para residências, I para indústrias e C
# para comércios.
kwh = float(input('Quantos kWh? '))
tipo = input('Qual o tipo da instalação? '
             '\nR = Residencial'
             '\nC = Comercio'
             '\nI = Industrial '
             '\n    ').upper()

if tipo == 'R':
    if kwh >= 500:
        preco = 0.65
    else:
        preco = 0.4
    print(f'Total a pagar: {kwh * preco:.2f}')
elif tipo == 'C':
    if kwh >= 1000:
        preco = 0.6
    else:
        preco = 0.55
    print(f'Total a pagar: {kwh * preco:.2f}')
elif tipo == 'I':
    if kwh >= 5000:
        preco = 0.6
    else:
        preco = 0.55
    print(f'Total a pagar: {kwh * preco:.2f}')
else:
    print('Instalação Inválida. Encerrando...')
