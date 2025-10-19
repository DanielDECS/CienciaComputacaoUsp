idade = int(input("Digite a sua idade: "))
'''
Crianca 0 até 12
Adolecente 13 até 17
Adulto 18 em diante
'''
if idade <= 0:
    print("idade invalida")
else:
    if idade <= 12:
        print("Criança")
    elif idade >= 13 and idade <= 17:
        print("Adolecente")
    else:
        print("Adulto")
