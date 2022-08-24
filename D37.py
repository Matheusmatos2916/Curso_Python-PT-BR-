##Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input("Digite um número inteiro:"))
print("Opção:")
print("(1-)Binário (2-)Octal (3-)Hexadecimal")
op = int(input("Digite a opção:"))

if(op == 1):
    bin = format(num, "b")
    print(f"{num} em binário: {bin}")
elif(op == 2):
    oct = format(num, "o")
    print(f"{num} em octal: {oct}") 
elif(op == 3):
    hex = format(num, "x")
    print(f"{num} em hexadecimal: {hex}")