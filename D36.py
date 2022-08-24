##Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input("Preço da casa:"))
salario = float(input("Total do salário:"))
anos = int(input("Total de anos:"))

parcela = casa / (anos*12)
minimo  = salario *30 / 100

print("Para pagar uma casa de R${:.2f} em {:.2f} anos.".format(casa, anos), end ='')
print("a prestação será de R${:.2f}".format(parcela))
if parcela <= minimo:
    print("Empréstimo pode ser CONCEDIDO!")
else:
    print("Empréstimo NEGADO!")