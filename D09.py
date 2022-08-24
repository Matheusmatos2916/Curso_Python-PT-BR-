## Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

num = input("Insira um número:")
op = int(num)



for i in range(11):
    
   mult = i*op 
   print("{} * {} = {}".format(i, op, mult))