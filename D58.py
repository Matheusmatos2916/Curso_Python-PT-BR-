'''Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. 
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''

import random

aleatorio = random.randint(0, 10)

count = 0
acertou = False

while not acertou:
    num = int(input("Chute um número de (0 até 10):"))
    count += 1
    if (aleatorio == num):
            acertou = True
print("você aceitou, o número é {}".format(aleatorio)) 
print("O total de tentativas: {} ".format(count))