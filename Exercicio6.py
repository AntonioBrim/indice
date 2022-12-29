x = int(input("digite o primeiro numero: "))
y = int(input("digite o segundo numero: "))
z = int(input("digite o terceiro numero: "))

if(x > y and x > z):
    print(x)
elif(y > x and y > z):
    print(y)
else:
    print(z)