'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

Média abaixo de 5.0: Reprovado
Média entre 5.0 e 6.9: Recuperação
Média 7.0 ou superior: Aprovação '''

n1 = float(input("Insira a primeira nota:"))
n2 = float(input("Insira a segunda nota:"))

media = (n1 + n2)/2

print("Sua média foi: {:.2f}".format(media))

if media < 5.0:
    print("Reprovado")
elif media >=5.0 and media < 6.9:
    print("Recuperação")
elif media >= 7.0 and media <= 10:
    print("Aprovação")