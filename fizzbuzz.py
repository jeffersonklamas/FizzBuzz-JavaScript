#-------------------------------------------------------
# FizzBuzz
# Divisivel por 3 => 'Fizz',
# Divisivel por 5 => 'Buzz',
# Divisivel por 3 e 5 => 'FizzBuzz',
# Se não for um número => 'Não é um Número',
# Se não for divisivel nem por 3 e nem por 5 => Entrada
#-------------------------------------------------------

import os

# Limpa tela quando da saída no terminal
os.system('clear') or None

# Desenvolvimento

valor = 40

# Nada Bom no momento, Falta resolver a opção Se não for um número => 'Não é um Número',


#if type(valor) != 'int':
#    print('Não é um número')
if valor % 3 == 0 and valor % 5 == 0:
    print('FizzBuzz')
elif valor % 3 == 0:
    print('Fizz')
elif valor % 5 == 0:
    print('Buzz')
print (valor)

