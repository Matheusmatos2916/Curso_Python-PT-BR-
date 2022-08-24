
'''Refaça o Desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

Equilátero: todos os lados iguais
Isósceles: dois lados iguais
Escaleno: todos os lados diferentes
'''

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
    
if(a + b > c and a + c > b and b + c > a):
  print("Os 3 lados foram um triângulo!")
if(a == b and a == c):
  print("Equilatero")
elif(a == b or a == c or b == c):
  print("Isosceles")
else:
  print("Escaleno")
else: 
  print("Os 3 lados não formam um triângulo!")


