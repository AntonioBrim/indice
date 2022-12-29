salario = float(input("Digite o valor do salário: "))
ajuste_de_salario = 0
percentual_de_ajuste = 0
valor_do_aumento = 0

if(salario <= 280):
    percentual_de_ajuste = 1.2
    ajuste_de_salario = salario * percentual_de_ajuste

elif(salario > 280 and salario <= 700):
    percentual_de_ajuste = 1.15
    ajuste_de_salario = salario * percentual_de_ajuste

elif(salario > 700 and salario <= 1500):
    percentual_de_ajuste = 1.1
    ajuste_de_salario = salario * percentual_de_ajuste

else:
    percentual_de_ajuste = 1.05
    ajuste_de_salario = salario * percentual_de_ajuste

valor_do_aumento = ajuste_de_salario - salario
print(f"{salario}\n{percentual_de_ajuste}\n{valor_do_aumento}\n{ajuste_de_salario}")

