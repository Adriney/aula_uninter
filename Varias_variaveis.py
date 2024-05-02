#Várias_variáveis
nota = 8.5
discplina  = 'Algaritmos'
s1 = 'Você tirou %.2f na disciplina de %s' % (nota, discplina)
print(s1)

print('--'*20)
#Composição moderna
s2 = 'Você tirou {} na disciplina de {}'.format(nota, discplina)
print(s2)

print('--'*20)
#Composição com f-string
s3 = f'Você tirou {nota} na disciplina de {discplina}'
print(s3)