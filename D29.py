##Escreva um programa que leia a velocidade de um carro.
## se ele ultrapassar 80km/h. mostre uma mensagem dizendo que ele foi multado.
## A multa vai custar R$7,00 por cada Km acima do limite.

Velocidade = float(input("Velocidade do carro(km/h):"))
Total = Velocidade - 80
custo = Total * 7.00

if (Velocidade >= 80):
    print("Você foi multado.")
    print("Custo da multa: R$ {:.2f}".format(custo))
else: 
    print("Você não foi multado.")