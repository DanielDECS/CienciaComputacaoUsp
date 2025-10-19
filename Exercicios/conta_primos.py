def ePrimo(x):
    fator = 2
    while fator * fator <= x:
        if x % fator == 0:
            return False
        fator = fator + 1
    return True

def n_primos(n):
    contagem_primos = 0
    for i in range(2, n + 1):
        if ePrimo(i):
            contagem_primos = contagem_primos + 1
    return contagem_primos
