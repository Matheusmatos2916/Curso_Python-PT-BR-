'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. '''

from random import randint
venceu = 0
while True:
    num = int(input('Diga um valor: '))
    aleatorio = randint(0, 10)
    total = num + aleatorio
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I]')).strip().upper()[0]
    print(f'Você jogou {num} e o computador {aleatorio}. Total de {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            venceu += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            venceu += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {venceu} vezes.')
