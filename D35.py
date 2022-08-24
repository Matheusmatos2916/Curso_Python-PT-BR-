## Desenvolva um programa que oleia o comprimento de trÊs retas e diga ao usuário se elas podem ou não formar um triângulo.


a = float(input("Insira o tamanho da segmento de reta 1:"))
b = float(input("Insira o tamanho da segmento de reta 2:"))
c = float(input("Insira o tamanho da segmento de reta 3:"))




maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
menor = a
if b < c and b < a:
    menor = b
if c < b and c < a:
    menor1 = c
    menor2 = b

soma = b+c

if soma > a: 
  print("Será possível formar um triângulo.")
else:
 print("Não será possível formar um triângulo.")