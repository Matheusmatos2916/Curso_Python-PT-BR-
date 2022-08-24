'''Refaça o Desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.'''
a1 = int(input("O valor primeiro termo:"))
r = int(input("O valor da razão de um PA:"))
i = 1

while i <= 11:
      an = a1 + ((i - 1)*r)
      print("{}°) = {}".format(i, an))
      i += 1