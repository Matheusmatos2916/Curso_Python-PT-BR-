##Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

import math as mt

CO = float(input("Insira o comprimento do cateto oposto:"))
CA = float(input("Insira o comprimento do cateto adjcente:"))

hipo = mt.sqrt(pow(CO,2) + pow(CA,2))

print("O comprimento da hipotesa é: {:.2f}".format(hipo))

