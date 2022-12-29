#1.Faça um Programa que peça dois números e imprima o maior deles.


#Armazena as variaveis/ int = inteiro , faz com quem a saida seja do type int
number1 = int(input("digite o 1 valor: "))
number2 = int(input("digite o 2 valor: "))

#SE o primeiro for maior que o segundo imprimi o "number1" se nao imprimi "number2"
if(number1 > number2):
    print(number1)

else:
    print(number2)