'''Desenvolva um programa qu leia o primeiro termo e a razão de um PA. No final, mostre os 10 primeiros termos dessa progressão.'''





a1 = int(input("O valor primeiro termo:"))
r = int(input("O valor da razão de um PA:"))


for i in range(1, 11):
    an = a1 + ((i - 1)*r)
    print("{}°) = {}".format(i, an))



