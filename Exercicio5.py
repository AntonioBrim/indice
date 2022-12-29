#5.0Faça um programa para a leitura de duas notas parciais de um aluno.
#O programa deve calcular a média alcançada por aluno e apresentar:
#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#A mensagem "Reprovado", se a média for menor do que sete;
#A mensagem "Aprovado com Distinção", se a média for igual a dez.


# Armazena as variáveis/ int = inteiro , faz com quem a saida seja do type int
note1 = int(input("digite a primeira nota: "))
note2 = int(input("digite a segunda nota: "))

#calcula a média das notas
average = (note1 + note2) / 2

if(average >= 7 and average != 10):
    print("Aprovado")

elif(average < 7):
    print("Reprovado")

else:
    print("Aprovado com Distição")
