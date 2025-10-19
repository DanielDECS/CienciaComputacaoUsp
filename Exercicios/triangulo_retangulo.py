class Triangulo:

    def __init__(self, l_a, l_b, l_c):
        self.a = l_a
        self.b = l_b
        self.c = l_c

    def retangulo(self):
        if(self.b > self.a):
            aux = self.a
            self.a = self.b
            self.b = aux

        if(self.c > self.a):
            aux = self.a
            self.a = self.c
            self.c = aux

        if(self.a * self.a == self.b * self.b + self.c * self.c):
            return True
        else :
            return False