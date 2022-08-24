'''Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.'''

num = input("Insira um número:")
op = int(num)



for i in range(11):
    
   mult = i*op 
   print("{} * {} = {}".format(i, op, mult))