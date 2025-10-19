class Buscador:

    def busca_sequencial(self, lista, x):
        for i in range(len(lista)):
            if lista[i] == x:
                return True
        return False

    def busca_binaria(self, lista, x):
        primeiro_lista = 0
        ultimo_lista = len(lista)-1
        while primeiro_lista <= ultimo_lista:
            meio = (primeiro_lista + ultimo_lista) // 2
            if lista[meio] == x:
                return meio
            else:
                if x < lista[meio]:
                    ultimo_lista = meio - 1
                else:
                    primeiro_lista = meio + 1
        return -1
            
        