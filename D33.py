## Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

a = int(input("Insira o primeiro número:"))
b = int(input("Insira o segunda número:"))
c = int(input("Insira o terceiro número:"))

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
menor = a
if b < c and b < a:
    menor = b
if c < b and c < a:
    menor = c
print("O maior número digitado foi {}".format(maior))
print("O menor número digitado foi {}".format(menor))