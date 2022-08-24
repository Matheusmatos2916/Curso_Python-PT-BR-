'''Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.'''

for  i in range(1, 6):
    peso = float(input("Insira o peso a {}°pessoa:".format(i)))
    print("peso da {}°pessoa em kg:{}".format(i, peso))
    
    if i == 1:
        maior = peso
        menor = peso
    else:   
       if peso > maior:
           maior = peso
       if peso < menor:
           menor = peso

print("maior peso: {} kg".format(maior))
print("menor peso: {} kg".format(menor))