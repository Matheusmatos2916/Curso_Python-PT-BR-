'''Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de um sequência de fibonacci.'''

print("Sequência de Fibonacci")

num = int(input("Quantos termos você quer mostrar?"))
T1 = 0
T2 = 1
print("{}->{}".format(T1, T2), end='')
cont = 3
while cont <= num:
        T3 = T1 + T2
        print(" -> {}".format(T3), end='')
        T1 = T2
        T2 = T3
        cont += 1
print("\nFim")