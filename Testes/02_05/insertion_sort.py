def insertion_sort(lista):
    fim = len(lista)
    for i in range(1, fim):
        elemento_atual = lista[i]
        j = i -1
        while j >= 0 and lista[j] > elemento_atual:
            lista[j+1] = lista[j]
            j = j - 1
        lista[j+1] = elemento_atual
    return lista