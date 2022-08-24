##faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno. cosseno e tangente desse ângulo.

import math as mt

x = float(input("Insira o ângulo:"))



cos = mt.cos(mt.radians(x))
sin = mt.sin(mt.radians(x))
tg = mt.tan(mt.radians(x))

print("Cos°{}: {:.2f}".format(x,cos))
print("Sin°{}: {:.2f}".format(x,sin))
print("tg°{}: {:.2f}".format(x,tg))
