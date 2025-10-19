#Mostre a tabuada do numero informado

numero = int(input("De qual numero deseja saber a tabuada? "))
print("A tabuada de ", numero, "é :")
'''
contador = 1
while contador <= 10:
    tabuada = numero * contador
    print(numero," x ", contador, " = ", tabuada)
    contador += 1
'''
for i in range(1, 11):
    tabuada = i * numero
    print(numero," x ", i, " = ", tabuada)
    