## Desevolva um programa que leia as duas notas de um aluno, calcule e mostre a sua media.

nome = input("Insira um nome:")
n1 = input("Insira a primeira nota:")
n2 = input("Insira a segunda nota:")
n3 = input("Insira a terceira nota:")

op1 = float(n1)
op2 = float(n2)
op3 = float(n3)

Media = float(float(op1+op2+op3)/3)

print("A média das notas de {}: {:.2f}".format(nome, Media))