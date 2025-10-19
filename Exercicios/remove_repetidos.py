def remove_repetidos(l):
    lista = l
    i = 0
    while i < len(lista):
        j = i + 1
        while j < len(lista):
            if lista[j] == lista[i]:
                del(lista[j])
            else:
                j = j + 1
        i = i + 1

    return sorted(lista)
