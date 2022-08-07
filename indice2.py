numero = int(input("Digite o numero desejado :"))

fibonacci = 0
fibonacci_auxiliar = 0

if(numero == 0):
    print("o número informado pertence a sequência")

while(numero > fibonacci):

    if(fibonacci == 0):
        fibonacci += 1
   
    fibonacci = fibonacci + fibonacci_auxiliar
    fibonacci_auxiliar = fibonacci - fibonacci_auxiliar

    if(fibonacci == numero):
        print("o número informado pertence a sequência")
        break
    
if(numero < fibonacci):
    print("o número informado nao pertence a sequência")
