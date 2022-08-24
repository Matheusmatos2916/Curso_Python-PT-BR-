''' Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal 

– 3x ou mais no cartão: 20% de juros'''


produto = float(input("Insira o valor do produto:"))
print("--- Selecionar opção ---\n")
print("(1-)à vista dinheiro/cheque: 10% de desconto\n(2-)à vista no cartão: 5% de desconto\n(3-)em até 2x no cartão: preço formal\n(4-)3x ou mais no cartão: 20% de juros")
op = int(input("Insira a opção:"))

if op == 1:
    desconto = produto * 0.1
    total = produto - desconto
    print("O valor com desconto: {:.2f}".format(total))
elif op == 2:
    desconto = produto * 0.05
    total = produto - desconto
    print("O valor com desconto: {:.2f}".format(total))
elif op == 3:
    parcela = produto/2
    print("O valor formal: {:.2f}\nParcela 2x: {:.2f}".format(produto, parcela))
elif op == 4 or op > 5:
     aumento = produto * 0.20
     total = produto + aumento
     print("O valor com acréscimo: {:.2f}".format(total))