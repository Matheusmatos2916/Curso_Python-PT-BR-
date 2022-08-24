'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo. '''
while True:
    num = int(input("Insira um número:"))
    for c in range(1,11):
        t = num * c
        print("{} x {} = {}".format(num, c, t))