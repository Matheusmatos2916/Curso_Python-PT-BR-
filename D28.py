##Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

aleatorio = random.randint(0, 5)

num = int(input("Chute um número de (0 até 5):"))


if num == aleatorio:
   print("você aceitou!".format(aleatorio))
else:
   print("você errou! O número é {}.".format(aleatorio)) 