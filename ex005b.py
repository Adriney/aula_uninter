#Escreva um algoritmo em Python em que o usuário escolhe se
# quer comprar maçãs, laranjas ou bananas. Deverá ser
# apresentado na tela um menu com as opções: 1 para maçã,
# e para larenja e 3 para banana. Ap´s escolhida a fruta,
# deve-se digitar quantas unidades se quer comprar.
# O algiritmo deve calcular o preço totala pagar do produto
# escolhido e mostrá-lo na tela. Considere que uma maçã custa
# R$2,30, e uma laranja, R$3,60, e uma banana, R$1,85.
# Vamos resolver no Python com uso do elif.
print('Escolha o que deseja comprar: ')
print('1 - Maçã ')
print('2 - Laranja')
print('3 - Banana')
produto = int(input('Qual sua escolha?'))
qtd = int(input('Quantas unidades?'))
if(produto == 1):
     pagar = qtd * 2.3
     print(f'Você comprou {qtd} maçãs. Total à pagar : {pagar}')
elif (produto == 2):
     pagar = qtd * 3.6
     print(f'Você comprou {qtd} laranjas. Total à pagar : {pagar}')
elif(produto == 3):
     pagar = qtd * 1.85
     print(f'Você comprou {qtd} bananas. Total à pagar : {pagar}')
else:
     print('Produto inexistente! ')