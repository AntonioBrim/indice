import json

with open("dados.json") as file:
   data = json.load(file)

soma = 0
dias_de_faturamento = 0
list_de_valores = []
for dia in range(1, len(data)):

   valor = data[dia]["valor"]

   if(valor > 0):

      list_de_valores.append(valor)
      soma += valor
      dias_de_faturamento += 1

media_de_faturamento = (soma / dias_de_faturamento)
dias_superior = 0

for dias_da_media in range(1, len(data)):

   if(data[dias_da_media]["valor"] > media_de_faturamento):
      dias_superior += 1

print("O menor valor de faturamento ocorrido em um dia do mês é : R$ {:.2f}".format(min(list_de_valores)))
print("O maior valor de faturamento ocorrido em um dia do mês é : R$ {:.2f}".format(max(list_de_valores)))
print(f"O Número de dias no mês em que o valor diário foi superior à média mensal é : {dias_superior} dias")
