'''Crie um programa que leia dois valores e mostre um menu na tela:

[1]somar
[2]multiplicar
[3]maior
[4]novos números
[5]sair do programa

seu programa deverá realizar a operação solicitada em cada caso.'''


Valor1 = int(input("Insira um primeiro valor:"))
Valor2 = int(input("Insira um segunda valor:"))
op = 0


while op != 5:
    print("[1]somar\n[2]multiplicar\n[3]maior\n[4]novos números\n[5]sair do programa")
    op = int(input("Insira a opção do menu:"))
    if op == 1:
        OP1 = Valor1 + Valor2
        print("O resultado da operação: {}".format(OP1))
    elif op == 2:
        OP1 = Valor1 * Valor2
        print("O resultado da operação: {}".format(OP1))
    elif op == 3: 
      if Valor1 > Valor2:
          print("O primeiro valor é maior que é o segundo.")
      elif Valor2 > Valor1:
          print("O segundo valor é maior que é o  primeiro.")
      else:
          print("O valores são igual.")
    elif op == 4:
        Valor1 = int(input("Insira um novo primeiro valor:"))
        Valor2 = int(input("Insira um novo segunda valor:"))
    elif op == 5:
        print("Finalizando...")