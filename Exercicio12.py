valor_da_hora = float(input("Digite o valor da hora de trabalho: "))
quantidade_de_hora = int(input("Digite quantas horas de trabalho por mes: "))

inss = 0.1
imposto_de_renda = 0
salario_bruto = quantidade_de_hora * valor_da_hora

if(salario_bruto <= 900):
    pass

elif(salario_bruto > 900 and salario_bruto <= 1500 ):

    imposto_de_renda = 0.05

elif(salario_bruto > 1500 and salario_bruto <= 2500):

    imposto_de_renda = 0.1

else:

    imposto_de_renda = 0.2

descontos = (imposto_de_renda * salario_bruto) + (salario_bruto * inss)

print(f"Salário Bruto:({quantidade_de_hora} * {valor_da_hora})      : R$ {salario_bruto}")
print(f"(-) IR ({int(imposto_de_renda * 100)}%)                    : R$ {imposto_de_renda * salario_bruto}")
print(f"(-) INSS ({int(inss * 100)}%)                  : R$ {inss * salario_bruto}")
print(f"FGTS (11%)                      : R$ {salario_bruto * 0.11}")
print(f"Total de descontos              : R$ {descontos}")
print(f"Salário Liquido                 : R$ {salario_bruto - descontos}")