
'''crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderado os espaços.'''

string = str(input("Insira a frase:"))
stringSemEspacos = string.replace(' ', '')
stringTodaMinuscula = stringSemEspacos.lower()
stringInvertida = stringTodaMinuscula[::-1]
if stringInvertida == stringTodaMinuscula:
    print ("SIM")
else:
    print ("NAO")


