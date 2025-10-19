num = int(input("Digite um número inteiro:"))
pNum = 0
sNum = 0
adjacentes = False
while num > 0 and adjacentes != True:
    pNum = num % 10
    num = num // 10
    sNum = num % 10
    if pNum == sNum:
        adjacentes = True
        num = num // 10
if adjacentes:
    print("sim")
else:
    print("não")
