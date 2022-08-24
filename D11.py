##Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la.sabendo que cada litro de tinta, pinta uma área de 2m^2.

larg = input("Insira a largura da parede (em m):")
comp = input("Insira a comprimento da parede(em m):")

op_larg = float(larg)
op_comp = float(comp)

mq = op_larg*op_comp

litros = mq/2

print("Área: {} m²".format(mq))
print("Total de litros: {} L".format(litros))



