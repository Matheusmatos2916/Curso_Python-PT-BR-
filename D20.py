##O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.##O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random



num1 = str(input('Primeiro aluno:'))
num2 = str(input('Segundo aluno:'))
num3 = str(input('Terceiro aluno:'))
num4 = str(input('Quarto aluno:'))

def funcao():
  return 0.1
  


lista = [num1, num2, num3, num4]


ordem = random.shuffle(lista, funcao)

print("Ordem escolhido:", lista)