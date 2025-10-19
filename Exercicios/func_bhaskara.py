import math
def delta(a, b, c):
    return b ** 2 - 4 * a * c


def imprime_raizes(a, b, c):
    d = delta(a, b, c)
    if d == 0:
        x = (- b + math.sqrt(d)) / (2 * a)
        print("A raiz desta equação é", x)
    else:
        if d < 0:
            print("Esta equação não possui raízes reais")
        else:
            x = (- b + math.sqrt(d)) / (2 * a)
            y = (- b - math.sqrt(d)) / (2 * a)
            if x < y:
                print("As raízes da equação são", x, "e", y)
            else:
                print("As raízes da equação são", y, "e", x)

def main():
    a_digitado = float(input("Digite o valor de a: "))
    b_digitado = float(input("Digite o valor de b: "))
    c_digitado = float(input("Digite o valor de c: "))
    imprime_raizes(a_digitado, b_digitado, c_digitado)
