x = int(input("digite o primeiro numero: "))
y = int(input("digite o segundo numero: "))
z = int(input("digite o terceiro numero: "))
maior = x


if(y > x and y > z):
    maior = y

if(z > y and z > x):
    maior = z

menor = x

if(y < x and y < z):
    menor = y

if(z < y and z < x):
        menor = z

print(f"o maior valor é :{maior} e o menor valor é: {menor}")