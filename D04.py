##Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

a = input('Digite algo: ')
print('O tipo primitivo desse valor é:', type(a))
print("Só tem espaço? ", a.isspace())
print("E um número?", a.isnumeric())
print("É alfabético?", a.isalpha())
print("É alfanumérico?", a.isalnum())
print("Está em maiscula?", a.isupper())
print("Está em misnúscula?", a.islower())
print("Está capitalizada?", a.istitle())