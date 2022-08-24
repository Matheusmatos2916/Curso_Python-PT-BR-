##Desenvolva um programa que pergunte a distância de um viagem em km. calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200km e R$0,45 para viagens mais longas.

distância = float(input("Insira a distância (em km):"))

if distância <= 200:
  preço = 0.50*distância
  print("O preço da passagem: R$ {:.2f}".format(preço))
else:
  preço = 0.45*distância
  print("O preço da passagem: R$ {:.2f}".format(preço))
  
