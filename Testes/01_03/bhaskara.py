import math

a = float(input("digite o valor de a"))
b = float(input("digite o valor de b"))
c = float(input("digite o valor de c"))

delta = b **2 - 4 * a * c

if delta == 0:
    x = (- b + math.sqrt(delta)) / (2 * a)
    print("a raiz desta equação é", x)
else:
    if delta < 0:
        print("esta equação não possui raízes reais")
    else:
        x = (- b + math.sqrt(delta)) / (2 * a)
        y = (- b - math.sqrt(delta)) / (2 * a)
        if x < y:
            print("as raízes da equação são", x, "e", y)
        else:
            print("as raízes da equação são", y, "e", x)