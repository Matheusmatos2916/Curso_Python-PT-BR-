'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:

A média de idade do grupo.'''
soma_idade = 0
media = 0
maior_homem = 0
nome_homem = ''
total_mulheres = 0
for p in range(1,5):
    print("--- {}°Pessoa ---".format(p))
    nome = str(input("Nome:")).strip()
    idade = int(input("Idade:"))
    sexo = str(input("Sexo [M/F]:")).strip()
    soma_idade += idade
    if p == 1 and sexo in 'Mm':
        maior_homem = idade
        nome_homem = nome
    if sexo in 'Mm' and idade > maior_homem:
        maior_homem = idade
        nome_homem = nome
    if sexo in 'Ff' and idade < 20:
        total_mulheres +=1
media = soma_idade / 4
print("A média de idade do grupo é de {} anos".format(media))
print("O homem mais velho tem {} anos e se chama {}.".format(maior_homem, nome))
print("Ao todo são {} mulheres com menos de 20 anos.".format(total_mulheres))

