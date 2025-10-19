def soma_hipotenusas(n):
    valor = n
    soma = 0
    ant = n + 1
    while n >= 1:
        i = n
        while i >= 1:
            h = (i ** 2 + n ** 2) ** (1/2)
            if h <= valor and (h * 10) % 10 == 0 and h < ant:
                h = int(h)
                ant = h
                soma = soma + h
            i = i - 1
        n = n - 1
    return soma

