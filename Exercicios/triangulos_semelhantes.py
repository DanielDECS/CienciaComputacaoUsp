class Triangulo:
    def __init__(self, l_a, l_b, l_c):
        self.a = l_a
        self.b = l_b
        self.c = l_c


    def dev_lista(self):
        lista = [self.a, self.b, self.c]
        lista = sorted(lista)
        return lista


    def semelhantes(self, triangulo):
        t3 = []
        for x in range(0, 3):
            t3.append(self.dev_lista()[x] / triangulo.dev_lista()[x])
        if t3[0] == t3[1] and t3[0] == t3[2]:
            return True
        else:
            return False