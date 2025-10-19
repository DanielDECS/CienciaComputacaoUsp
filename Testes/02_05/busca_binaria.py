def busca(lista, elemento):

    primeiro = 0
    ultimo = len(lista) - 1

    while primeiro <= ultimo:
        i = int((primeiro + ultimo) / 2)
        print(i)
        if lista[i] == elemento:
            return i
        elif lista[i] > elemento:
            ultimo = i - 1
        elif lista[i] < elemento:
            primeiro = i + 1
        else:
            return False
        
    return False