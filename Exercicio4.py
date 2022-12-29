#4.Faça um Programa que verifique se uma letra digitada é vogal ou consoante.


letra = input("digite uma letra: ")
letra = letra.lower()

#isalpha = type booleano,true se todos os caracteres na string forem alfabetos podem-
# ser minúsculas e maiúsculas; false se pelo menos um caractere não for do alfabeto


#Se a letra nao for vogal e nao for consoante , nao é uma letra 
# or = ou 

if(letra.isalpha()): 
    if(letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u"):
        print("Vogal")

    else:
        print("consoante")

else:
    print("nao é uma letra")


