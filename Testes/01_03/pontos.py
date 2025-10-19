x1 = float(input("digite a coordenada x do primeiro ponto: "))
y1 = float(input("digite a coordenada y do primeiro ponto: "))
x2 = float(input("digite a coordenada x do segundo ponto: "))
y2 = float(input("digite a coordenada y do segundo ponto: "))

distancia = ((x1 - x2)**2 + (y1 - y2)**2)**0.5

if distancia >= 10:
    print("longe")
else:
    print("perto")
