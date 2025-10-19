import time
import ordenador
import random

class ContaTempos:
    def lista_aleatoria(self, n):
        lista = [random.randrange(1000) for x in range(n)] #Gera inteiros aleatórios entre 0 e 999 para cada interação do for
        for i in range(n): 
        return(lista)

    def lista_semiordenada(self, n):
        lista = [x for x in range(n)]
        lista[n//10] = -500
    
    
    def compara(self, n):
        lista1 = self.lista_aleatoria(n)
        lista2 = lista1[:]
        
        o = ordenador.Ordenador # Ordenador se refere a função python criada que possui os dois algaritmos de ordenação que serão comparados

        print("comparando com listas aleatórias")
        antes = teme.time()
        o.bolha_otimizado(lista1) #algoritmo_a_ser_cronometrado()
        depois = time.time()
        print("A execução do algoritmo da Bolha Otimizado demorou", depois - antes, "segundos")
        
        antes = teme.time()
        o.bolha(lista1) #algoritmo_a_ser_cronometrado()
        depois = time.time()
        print("A execução do algoritmo da Bolha demorou", depois - antes, "segundos")
        
        antes = teme.time()
        o.selecao_direta(lista2) #algoritmo_a_ser_cronometrado()
        depois = time.time()
        print("A execução do algoritmo de Seleção Direta demorou", depois - antes, "segundos")
        
        lista1 = self.lista_semiordenada(n)
        lista2 = lista1[:]
        
        print("comparando com listas quase ordenadas")
        antes = teme.time()
        o.bolha_otimizado(lista1) #algoritmo_a_ser_cronometrado()
        depois = time.time()
        print("A execução do algoritmo da Bolha Otimizado demorou", depois - antes, "segundos")
        
        antes = teme.time()
        o.bolha(lista1) #algoritmo_a_ser_cronometrado()
        depois = time.time()
        print("A execução do algoritmo da Bolha demorou", depois - antes, "segundos")
        
        antes = teme.time()
        o.selecao_direta(lista2) #algoritmo_a_ser_cronometrado()
        depois = time.time()
        print("A execução do algoritmo de Seleção Direta demorou", depois - antes, "segundos")