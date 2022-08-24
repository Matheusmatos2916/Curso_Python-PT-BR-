##Faça um algoritmo que leia o preço de um produto e mostre seu novo preço. com 5% de desconto.

preco = input("Insira o valor do produto:")
op_preco = float(preco)
desconto = op_preco * 0.05
total_preco = op_preco - desconto

print("O valor do produto: {:.2f}".format(op_preco))
print("O valor do produto após o desconto: {:.2f}".format(total_preco))