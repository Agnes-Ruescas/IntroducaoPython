a = int(input('Primeiro bimestre: '))
while a > 10:
    a = int(input('Você digitou errado. \nPrimeiro bimestre: '))
b = int(input('Segundo bimestre: '))
while b > 10:
    b = int(input('Você digitou errado. \nSegundo bimestre: '))
c = int(input('Terceiro bimestre: '))
while c > 10:
    c = int(input('Você digitou errado. \nTerceiro bimestre:'))
d = int(input('Quarto bimestre: '))
while d > 10:
    d = int(input('Você digitou errado. \nQuarto bimestre: '))
media = (a + b + c + d)/4
print('Média final é {}'.format(media))





# a = 0
# while a <= 10:
#     print(a)
#     a += 1


# a = int(input('Entre com um valor: '))
#
# for num in range(a+1):
#     div = 0
#     for x in range(1, num+1):
#         resto= num % x
#         if resto == 0:
#             div += 1
#
#     if div == 2:
#         print(num)


# a = int(input('Entre com o número: '))
# div = 0
#
# for x in range(1, a+1):
#     resto= a % x
#     if resto == 0:
#         div += 1
#
# if div == 2:
#     print('Número {} é primo'.format(a))
# else:
#     print('Número {} não é primo'.format(a))