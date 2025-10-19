myList = [10, 1, 8, 3, 5]
length = len(myList)

for i in range(length // 2):
    myList[i], myList[length - i - 1] = myList[length - i - 1], myList[i]

print(myList)

"""
Nota:
atribuímos a lengthvariável com o comprimento da lista atual (isso torna nosso código um pouco mais claro e curto)
lançamos o forloop para percorrer seus length // 2tempos de corpo 
(isso funciona bem para listas com comprimentos pares e ímpares,
 porque quando a lista contém um número ímpar de elementos, o do meio permanece intocado)
trocamos o i ésimo elemento (do início da lista) por aquele com índice igual a (length - i - 1)
(do final da lista); No nosso exemplo, para iigual 0a (l - i - 1)dá 4; 
por iigual a 1, dá 3- isso é exatamente o que precisávamos.
"""