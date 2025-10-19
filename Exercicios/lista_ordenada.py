def ordenada(lista):
    proximo = 0
    for i in range(len(lista)):
        proximo = i + 1
        if proximo < len(lista):
            if lista[i] > lista[proximo]:
                return False
    return True
