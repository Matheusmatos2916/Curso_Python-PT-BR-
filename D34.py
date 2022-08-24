##Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
## para salários superiores a R$1.250,00, calcule um aumento de 10%
## para os inferiores ou iguais e aumento é de 15%. 

salário = float(input("Insira seu salário:"))

if salário > 1250.00:
    aumento = salário * 1.10
    print("Seu salário: R$ {:.2f}".format(aumento))
else: 
    aumento = salário * 1.15
    print("Seu salário: R$ {:.2f}".format(aumento))