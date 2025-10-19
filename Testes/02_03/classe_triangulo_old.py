class Triangulo:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self):
        return (self.a + self.b + self.c)


    def tipo_lado(self):
        if (self.a == self.b) and (self.b == self.c):
            return "equilátero"
        elif (self.a == self.b) or (self.b == self.c) or (self.a == self.c):
            return "isósceles"
        else :
            return "escaleno"
            
from Triangulo import *

t = Triangulo(1, 2, 3)
print(t.a)
print(t.b)
print(t.c)
print(t.perimetro())
print(t.tipo_lado())