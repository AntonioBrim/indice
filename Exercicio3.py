# 3.Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
#Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

# Armazena a variavel
sexo = input("digite o sexo: ")

# usa o "if" caso o valor da variavel "sexo" seja igual a "F" ou "M" 
if(sexo.upper() == "F"):#upper serve para deixar a string maiuscula ,caso o usuário digite -
    print("Feminino")   #minuscula o codigo ainda aceitará

elif(sexo.upper() == "M"):
    print("Masculino")

#Caso nenhum deles corresponda aos de cima , sera inválido

else:
    print("Sexo Invalido") 
