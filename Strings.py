#Agora, utilizando operadores + e *, crie as saídas a seguir:
#a)'ant bat cod'
#b)'ant ant ant ant ant ant ant ant'
#c)'ant bat bat cod cod cod'
#d)'ant bat ant bat ant bat ant bat ant bat ant bat ant bat'
#e)'batbatcod batbatcod batbatcod batbatcod batbatcod '
s1 = 'ant'
s2 = 'bat'
s3 = 'cod'

res1 = s1 + ' ' + s2 + ' ' + s3
print(res1)

res2 = 10 * (s1 + ' ')
print(res2)

res3 = (s1 + ' ') + 2 * (s2 + ' ') + 3 *(s3 + ' ')
print(res3)

res4 = 7 * (s1 + ' '+ s2 + ' ')
print(res4)

res5 = 5 * (s2 +  s2  + s3 + ' ')
print(res5)