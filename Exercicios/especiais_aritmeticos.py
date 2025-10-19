'''
Métodos especiais
__add__: para adição (+)
__sub__: para subtração (-)
__mul__: para multiplicação (*)
__truediv__: para divisão (/)
'''


def mdc(a, b):
    ''' (int, int) -> int
    recebe dois inteiros diferentes de zero e retorna o maximo
    divisor comum entre a e b'''
    if b == 0: return a
    if a == 0: return b
    while a%b != 0:
        a, b = b, a%b
    return b

class Racional:
    def __init__(self, n=0, d=1):
        div = mdc(n, d)
        self.put(n/div, d/div)

    def __str__(self):
        return "%d/%d"%(self.num, self.den)

    def get(self):
        return self.num, self.den

    def put(self, n=0, d=1):
        self.num, self.den = n, d

    def __add__(self, other):
        n = self.num * other.den + self.den * other.num
        d = self.den * other.den
        return Racional(n, d)

    # escreva aqui o seu codigo para os metodos
    # __truediv__
    # __mul__
    # __sub__
    # e ao menos um teste para cada metodo


# testes
r1 = Racional(2)
r2 = Racional(1,5)
print(r1, '+', r2, '=>', r1 + r2)
# teste do div:
# print(r1, '/', r2, '=>', r1 / r2)
#
# outros testes