def soma_matrizes(m1, m2):
    soma = []
    nLinhasA, nLinhasB = len(m1), len(m2)
    nColunasA, nColunasB = len(m1[0]), len(m2[0])
    
    if (nLinhasA == nLinhasB) and (nColunasA == nColunasB):
        for i in range(nLinhasA):
            linha = [0]*nColunasA
            soma.append(linha)
            for j in range(nColunasA):
                soma[i][j] = m1[i][j] + m2[i][j]
        return soma
    else:
        return False

