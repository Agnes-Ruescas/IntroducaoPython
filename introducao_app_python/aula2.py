a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
print('Soma: {soma}. '
      '\nSubtração {sub}.'
      '\nMultiplicação: {multiplicacao}'.format(soma = soma,
                                                multiplicacao = multiplicacao,
                                                sub = subtracao))
print('Divisão: ' + str(divisao))
print('Resto: ' + str(resto))
