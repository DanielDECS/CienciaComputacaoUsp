def inverte_ordem():
    lista = []
    l2 = []
    n = 1
    i = 0
    while n != 0:
        n = int(input('Digite um número: '))
        lista.append(n)
        i = len(lista)
    i = i - 1
    while i >= 0:
        l2.append(lista[i])
        i = i - 1
    for a in l2:
        if a != 0:
            print(a)

x = inverte_ordem()