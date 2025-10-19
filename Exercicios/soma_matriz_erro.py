def soma_matrizes(m1, m2):
    soma = []
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
        linha = []
        for i in range(len(m1)):
            for j in range(len(m1[0])):
                valor = m1[i][j] + m2[i][j]
                linha.append(valor)
        soma.append(linha)
        return soma
    else:
        return False

