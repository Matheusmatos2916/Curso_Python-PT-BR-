## Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

N1 = input("Insira um número inteiro:")
op = int(N1)

print("O antessor de {} : {}".format(op, op-1))
print("O sucessor de {} : {}".format(op, op+1))