w = []
for i in range(1,4):
    x = int(input(f"digite o {i}º numero"))
    w.append(x)

w.sort(reverse=True) #ordena os numeros , reverse true decrescente
print(w)