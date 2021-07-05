
// FizzBuss
// Divisivel por 3 => 'Fizz',
// Divisivel por 5 => 'Buzz',
// Divisivel por 3 e 5 => 'FizzBuzz',
// Se não for um número => 'Não é um Número',
// Se não for divisivel nem por 3 e nem por 5 => Entrada

let resultado = fizzBuzz(50);
console.log(resultado)

function fizzBuzz(entrada) {
    // Se não for um número => 'Não é um Número'
    if (typeof entrada !== 'number')
        return 'Não é um número';
    // Divisivel por 3 e 5 => 'FizzBuzz'
    if ((entrada % 3 === 0) && (entrada % 5 === 0))
        return 'FizzBuss';
    // Divisivel por 3 => 'Fizz'
    if (entrada % 3 === 0)
        return 'Fizz';
    // Divisivel por 5 => 'Buzz'
    if (entrada % 5 === 0)
        return 'Buzz';
    // Se não for divisivel nem por 3 e nem por 5 => Retorne o alor da Entrada
    return entrada;  
}