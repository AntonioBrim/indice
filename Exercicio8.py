x = int(input("digite o valor do primeiro: "))
y = int(input("digite o valor do segundo: "))
z = int(input("digite o valor do terceiro: "))

if(x < y and x < z):
    print("comprar o primeiro produto")
elif(y < x and y < z):
    print("comprar o segundo produto")
else:
    print("comprar o terceiro produto")