// Jogo do FizzBuzz

for (var i = 1; i <= 100; i++){

    var saida = ""

    if (i % 3 == 0) {saida += 'Fizz'}
    if (i % 5 == 0) {saida += 'Buzz'}

    if(saida == "") {saida = i}

    console.log(saida)

}