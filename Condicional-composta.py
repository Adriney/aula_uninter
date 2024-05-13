#Traduza as afirmações a seguir para condicionais em Python
#a)Se ano é divisivel por 4, escreva: "pode ser um ano bissexto".
# Caso contrário, escreva:"Definitivamente não é um ano bissexto"
ano = 1993
if (ano % 4 ==0):
    print("Ano pode ser bissexto!")
else:
    print("Ano definitivamente não é bissexto!")

#b)Se ambas as variáveis booleanas cima e baixo forem True, escreva:
# "Decida-se!", caso contrário, escreva: "Você escolheu um caminho!"
cima = True
baixo = False
if (cima == True and baixo == True):
    print("Decida-se!")
else:
    print("Você escolheu um caminho")