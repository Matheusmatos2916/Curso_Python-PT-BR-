
'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

Se ele ainda vai se alistar ao serviço militar.
Se é a hora de se alistar.
Se já passou do tempo do alistamento.

Sei programa também deveria mostrar o tempo que falta ou que passou do prazo.'''

ano=int(input("Insira o ano do seu nascimento:"))

alistamento = 2022-ano

total_ano = alistamento - 18

if alistamento > 18:
    print("já passou do tempo do alistamento")
    print("passou {} anos".format(total_ano))
elif alistamento == 18:
    print("é a hora de se alistar")
  
else:
    print("ele ainda vai se alistar ao serviço militar")
    print("Faltam {} anos".format(total_ano * -1))