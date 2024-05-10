#not
x = True
y = False
print(not  x)
print(not y)
print('-*'*15)
 #and
x = True
y = False
print(x and y)
print('--'*15)

 #or
x = False
y = True
print(x or y)
print('-='*15)
x = 10
y = 1
z = 5.5
res = (x > y) and (z == y)
#True and False(x é maior que y= verdadeiro/ z é igual a y = False
print(res)
print('-_'*15)
x = 10
y = 1
z = 5.5
res = x > y or not z == y and y != y + z / x #z(10)dividido por x(5.5)=0.55 +y(1)=1.55
# x é maior que y =true / or not /z é igual a y=False/ and /y é diferente de 1.55 = True
#res = True or not False and True
#res = True or True and True
#res = True or True
print(res)
print('--'*15)