'''Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de trÊs e que se encontram no intervalo de 1 até 500.'''


soma = 0
for i in range(1, 500):
    if(i % 2 == 1 and i % 3 == 0):
        soma += i 

print("Soma entre todos os números ímpares que são múltiplos de três:{}".format(soma))       