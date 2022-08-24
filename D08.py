## Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metro = input("Insira a quantidade de metros:")
op_metro = float(metro)

cm = float(op_metro)*100
mm = float(op_metro)*1000


print("{} m em cm: {} cm".format(metro, cm))
print("{} m em mm: {} mm".format(metro, mm))