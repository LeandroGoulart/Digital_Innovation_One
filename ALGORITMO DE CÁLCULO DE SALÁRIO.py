'''Essa função recalcula aumento de salário.
Caso o funcionário receba até R$ 3000 reais, recebe 20% de reajuste
Acima de R$3000 reajusta 10% de reajuste '''


print ("Calcule o Salário")
print("se salario for menor que 3000 recebe reajuste 20%, senão recebe reajuste de apenas 10%.")
Valor = int (input ("Digite um valor: R$ "))
if Valor<=3000:
  print("Valor com juros: R$ ", Valor+ (Valor * 20 / 100))
else:print("Valor com juros: R$", Valor + (Valor * 10 / 100))