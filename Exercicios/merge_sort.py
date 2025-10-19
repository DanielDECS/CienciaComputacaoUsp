def merge_sort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)
        
    if (fim - inicio > 1):
        meio = (fim + inicio)//2
        merge_sort(lista, inicio, meio)
        merge_sort(lista, meio, fim)
        merge(lista, inicio, meio, fim)
    
    return lista
        
def merge(lista, inicio, meio, fim):
    lista_esquerda = lista[inicio:meio]
    lista_direita = lista[meio:fim]
    maior_esquerda, maior_direita = 0, 0
    for i in range(inicio, fim):
    
        if maior_esquerda >= len(lista_esquerda):
            lista[i] = lista_direita[maior_direita]
            maior_direita = maior_direita + 1
            
        elif maior_direita >= len(lista_direita):
            lista[i] = lista_esquerda[maior_esquerda]
            maior_esquerda = maior_esquerda + 1
        
        elif lista_esquerda[maior_esquerda] < lista_direita[maior_direita]:
            lista[i] = lista_esquerda[maior_esquerda]
            maior_esquerda = maior_esquerda + 1
            
        else:
            lista[i] = lista_direita[maior_direita]
            maior_direita = maior_direita + 1