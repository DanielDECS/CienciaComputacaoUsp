def raiz_quadrada(n):
    raiz = n ** (1/2)
    return raiz

def delta(a, b, c):
    if a + b + c == 0:
        return 0
    else:
        return b ** 2 - 4 * a * c

def equa_seg_grau(a, b, c):
    d = delta(a, b, c)
    if d == 0:
        x = (- b + (raiz_quadrada(d))) / (2 * a)
        print("A raiz desta equação é", x)
    else:
        if d < 0:
            print("Esta equação não possui raízes reais")
        else:
            x1 = (- b + (raiz_quadrada(d))) / (2 * a)
            x2 = (+ b + (raiz_quadrada(d))) / (2 * a)
            if x1 < x2:
                print("As raízes da equação são", x2, "e", x1)
            else:
                print("As raízes da equação são", x1, "e", x2)

def main():
    a_digitado = float(input("Digite o valor de a: "))
    b_digitado = float(input("Digite o valor de b: "))
    c_digitado = float(input("Digite o valor de c: "))
    verifica = a_digitado, b_digitado, c_digitado
    if verifica[:3] == (0,0,0):
        print("Valores inválidos")
    else:
        equa_seg_grau(a_digitado, b_digitado, c_digitado)

    

    
    