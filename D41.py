'''A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

Até 9 anos: Mirim
Até 14 anos: Infantil
Até 19 anos: Junior
Até 20 anos: Sênior
Acima: Master
'''
atleta = int(input("Insira o ano do seu nascimento:"))


anos = 2022 - atleta



if anos <= 9:
    print("Mirim")
elif anos <= 14:
    print("Infantil")
elif anos <= 19:
    print("Junior")
elif anos <= 20:
    print("Sênior")
else:
    print("Master")