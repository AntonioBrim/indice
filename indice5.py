nome = input("digite o nome que será invertido :")
nome_lista = []
nome_reverse = ""
for letras in nome:
    nome_lista.append(letras)

for numero in range(len(nome) -1, 0, -1):
    nome_reverse = nome_reverse + nome_lista.pop(numero)

nome_reverse += max(nome_lista)

print(nome_reverse)

