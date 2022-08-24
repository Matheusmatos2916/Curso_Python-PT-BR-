'''crie um programa que façã o computador jogar jokenpo com voce'''


import random


print("--- Selecionar opção ---")
print("(1-)Papel\n(2-)Pedra\n(3-)Tesoura")
op = int(input("Opção:"))

lista = ['Pedra','Tesoura'] ##Papel
lista2 = ['Tesoura', 'Papel'] ##Pedra
lista3 = ['Papel', 'Pedra'] ##Tesoura

escolhido = random.choice(lista)
escolhido2 = random.choice(lista2)
escolhido3 = random.choice(lista3)

if op == 1:
     if escolhido == 'Tesoura':
         print("Você perdeu, você escolheu: Papel\nmaquina:{}".format(escolhido))
     elif escolhido == 'Pedra':
         print("Você ganhou, você escolheu: Papel\nmaquina:{}".format(escolhido))
     else:
         print("Empate, você escolheu: Papel\nmaquina:{}".format(escolhido))
if op == 2:
     if escolhido2 == 'Papel':
         print("Você perdeu, você escolheu: Pedra\nmaquina:{}".format(escolhido2))
     elif escolhido2 == 'Tesoura':
         print("Você ganhou, você escolheu: Pedra\nmaquina:{}".format(escolhido2))
     else:
         print("Empate, você escolheu: Papel\nmaquina:{}".format(escolhido2))
if op == 3:
     if escolhido3 == 'Pedra':
         print("Você perdeu, você escolheu: Tesoura\nmaquina:{}".format(escolhido3))
     elif escolhido3 == 'Papel':
         print("Você ganhou, você escolheu: Tesoura\nmaquina:{}".format(escolhido3))
     else:
        print("Empate, você escolheu: Papel\nmaquina:{}".format(escolhido3))