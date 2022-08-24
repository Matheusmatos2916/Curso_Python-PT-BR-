'''Crie um programa que leia o ano de nascimento de sete. No final mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''

from datetime import date

Data_atual = date.today().year
for  i in range(1, 8):
    nasc = int(input("Em que ano a {}°pessoa nasceu?".format(i)))
    idade = Data_atual - nasc
    print("Essa {}°pessoa tem {} anos".format(i, idade))
    if idade >= 18:
        print("Essa {}°pessoa tem maioridade".format(i))
    else:
        print("Essa {}°pessoa  não maioridade".format(i))


