##Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date
ano = int(input("Insira o ano:"))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0:
    print("{} é bissexto".format(ano))
else:
    print("{} não é bissexto".format(ano))