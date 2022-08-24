##Crie um programa que leia quanto dinheiro uma pessoa tem na arteira e mostre quantos Dólares ela pode comprar. Considere $1 = R$3,27

Total = input("Insira quantos reais no total:")
reais = float(Total)

dinheiro = float(reais)/3.27

print("R${} = ${:.2f}".format(reais, dinheiro))