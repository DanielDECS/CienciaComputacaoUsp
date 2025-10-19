
#Mostre os números pares no intervalo entre mínimo e máximo 

minimo = int(input("Digite o valor mínimo: "))
maximo = int(input("Digite o valor máximo: "))

numero = minimo

while numero <= maximo:
    if numero % 2 == 0:
        print(numero)
    numero += 1
    