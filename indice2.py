numero =int(input("digite o numero desejado "))
fibonacci = 0
fibonacci_auxiliar = 0
soma = 0
fibonacci_total = []

if (numero == 0):
    print(" o número informado pertence a sequência")

while(numero > fibonacci):
    fibonacci += fibonacci_auxiliar
    fibonacci_auxiliar = fibonacci - fibonacci_auxiliar

    if(fibonacci == 0):
        fibonacci += 1

    if(numero == fibonacci):
        print(" o número informado pertence a sequência")
        break

    if(numero < fibonacci):
        print(" o número informado nao pertence a sequência")