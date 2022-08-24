##Escreva um programa que converta uma temperatura digitada em C e converta para F.

C = float(input("Insira a temperatura(em °C):"))

F = float((C * 9/5) + 32)

print("{}°C = {}F".format(C, F))
