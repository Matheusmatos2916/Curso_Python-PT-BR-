'''Escreva um programa que leia dois números inteiro e compare-os, mostrando na tela uma mensagem:

*O primeiro valor é maior
*O segunda valor é maior
*Não existe valor maior, os dois são iguais'''

N1 = int(input("Insira primeiro número:"))
N2 = int(input("Insira segundo número:"))

if (N1 > N2):
    print(f"O primeiro valor é maior")
elif(N2 > N1):
    print(f"O segunda valor é maior")
else:
    print(f"Não existe valor maior, os dois são iguais")