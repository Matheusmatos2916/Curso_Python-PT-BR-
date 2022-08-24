'''Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''

num = int(input("Insira um número:"))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("{} não é um número primo".format(num))
        else:
            print("{} é um número primo".format(num))
    
  
  
    
