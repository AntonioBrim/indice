sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53

soma = sp + rj + mg + es + outros

print("{:.2f}% em São Paulo".format((sp * 100) / soma))
print("{:.2f}% em Rio de Janeiro".format((rj * 100) / soma))
print("{:.2f}% em Minas Gerais".format((mg * 100) / soma))
print("{:.2f}% em Espírito Santos".format((es * 100) / soma))
print("{:.2f}% em outros".format((outros * 100) / soma))

