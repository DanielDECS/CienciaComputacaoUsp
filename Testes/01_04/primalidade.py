num = int(input("Digite um número inteiro: "))
ePrimo = True
fator = 2

while fator < num and ePrimo:
    if num % fator == 0:
        ePrimo = False
    fator = fator + 1
        
if ePrimo and num != 1:
    print("primo")
else:
    print("não primo")