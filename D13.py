##Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = input("Insira o salário:")
total_salario = float(salario)

aumento = total_salario * 0.15

final_salario = total_salario + aumento

print("O valor do produto: {:.2f}".format(total_salario))
print("O valor do produto após o aumento: {:.2f}".format(final_salario))
