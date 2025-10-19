  
import math

def determinant(matrix, mul):
    width = len(matrix)
    if width == 1:
        return mul * matrix[0][0]
    else:
        sign = -1
        total = 0
        for i in range(width):
            m = []
            for j in range(1, width):
                buff = []
                for k in range(width):
                    if k != i:
                        buff.append(matrix[j][k])
                m.append(buff)
            sign *= -1
            total += mul * determinant(m, sign * matrix[0][i])
        return total

def dist((x1, y1), (x2, y2), (x3, y3)):
    matrix = [[x1,y1,1],[x2,y2,1],[x3,y3,1]]
    determinat = determinant(matrix, 1)
    if determinat == 0:
        a = (x2 - x1)**2 + (y2 - y1)**2
        b = (x3 - x2)**2 + (y3 - y2)**2
        c = (x3 - x1)**2 + (y3 - y1)**2
        d = max(a, b, c)
        e = math.sqrt(d)
        return b
    else:
        print("This is a triangle!!")

#(2, 5), B (3, 7) e C (5, 11) example coordinte of allign points

print(dist((2,5),(3,7),(5,1)))

#dist((10,5), (5,10))