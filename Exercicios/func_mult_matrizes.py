def mult_matrizes(a, b):
    num_lin_a, num_col_a = len(a), len(a[0])
    num_lin_b, num_col_b = len(b), len(b[0])
    assert num_col_a == num_lin_b
    c = []
    for linha in range(num_lin_a): # percorre as linhas da matriz
        # começando nova linha
        c.append([])
        for coluna in range(num_col_b): # percorre as colunas da matriz
            c[linha].append(0)
            for k in range(num_col_a):
                c[linha][coluna] += a[linha][k] * b[k][coluna]
    return c

# teste das funções
a = [[1,2,3], [4,5,6]]
b = [[1,2], [3,4], [5,6]]
print(mult_matrizes(a,b))