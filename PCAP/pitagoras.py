"""
Garantir que um determinado triângulo 
seja um triângulo retângulo .

Precisaremos fazer uso do teorema de Pitágoras :

c 2 = a 2 + b 2

Como reconhecemos qual dos três lados é a hipotenusa?

A hipotenusa é o lado mais comprido.
"""


def isItATriangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

def isItRightTriangle(a, b, c):
    if not isItATriangle(a, b, c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2
    13
a = float(input("Enter the first side's length: "))
b = float(input("Enter the second side's length: "))
c = float(input("Enter the third side's length: "))

print(isItRightTriangle(a, b, c))
print(isItRightTriangle(a, b, c))

"""
Veja como testamos a relação entre a hipotenusa e os 
lados restantes - escolhemos o lado mais longo e 
aplicamos o teorema de Pitágoras para verificar se 
tudo está certo. Isso requer três verificações no total.
"""