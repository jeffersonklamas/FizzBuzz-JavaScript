# FizzBuss
# Divisivel por 3 => 'Fizz',
# Divisivel por 5 => 'Buzz',
# Divisivel por 3 e 5 => 'FizzBuzz',
# Se não for um número => 'Não é um Número',
# Se não for divisivel nem por 3 e nem por 5 => Entrada

valor = 40

#if type(valor) != 'int':
#    print('Não é um número')
if valor % 3 == 0 and valor % 5 == 0:
    print('FizzBuzz')
elif valor % 3 == 0:
    print('Fizz')
elif valor % 5 == 0:
    print('Buzz')
print (valor)

