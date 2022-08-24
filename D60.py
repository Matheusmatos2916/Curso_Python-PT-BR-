'''Faça um programa que leia um número qualquer e mostre o seu fatorial.'''

num = int(input("Insira um número inteiro:"))

fat = 1 
i = 1
while i <= num:
    fat *= i
    i += 1
print("fatorial  de {} é {}".format(num,fat))
    
  