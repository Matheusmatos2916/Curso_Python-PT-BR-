## Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

import math

n1 = input("Insira um número:")
op = int(n1)

d = op*2
t = op*3
sqrt = math.sqrt(op)

print("O dobro de {}: {}".format(op, d))
print("O triplo de {}: {}".format(op, t))
print("a raiz quadrada de {}: {:.2f}".format(op, sqrt))