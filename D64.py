'''Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles(Desconsiderando o flag)
'''
num = 0
soma = 0
cont = 0
while num != 999:
    
    num = int(input("Insira um número inteiro:"))
    if num != 999:
      soma += num
      cont += 1
    else:
      break

print("Resultado da soma: {} ".format(soma))
print("números digitado: {}".format(cont))
