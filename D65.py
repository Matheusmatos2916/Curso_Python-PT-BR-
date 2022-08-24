'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução.
mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar maiores.'''

num = int(input('Digite um número: '))
historico = [num]
c = True
soma = 0
i = 0

while c is True:

    num = int(input('Digite um número: '))
    historico.append(num)


    string = str(input('Deseja continuar? [S/N] ')).upper()
    if string == 'N':
        c = False
    elif string != 'N' and string != 'S':
        print('Opção inválida. Tente novamente.')

for num in historico:
    soma += num
    print(soma, end=' ')

    if num == historico[0]:
        maior = num
        menor = num
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num

count = len(historico)

print("VocÊ digitou os números {}".format(historico))
print("Maior número {} e menor número {}".format(maior, menor))
print('Soma {}, quantidade de números digitados {} e média {:.2f}'.format(soma, count, soma / count))