''' D61, perguntando para o usuário se ele  quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar O termos.'''

a1 = int(input("O valor primeiro termo:"))
r = int(input("O valor da razão de um PA:"))
i = 1
f = int(input("O final dos termos:"))

while i <= f:
      an = a1 + ((i - 1)*r)
      print("{}°) = {}".format(i, an))
      i += 1