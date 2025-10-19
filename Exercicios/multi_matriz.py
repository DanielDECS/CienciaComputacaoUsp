def mat_mul (A, B):
    num_linhas_A, num_colunas_A = len(A), len(A[0])
    num_linhas_B, num_colunas_B = len(B), len(B[0])
    assert num_colunas_A == num_linhas_B
    
    C = []
    for linha in range(num_linhas_A):
        C[linha].append(0)
        for coluna in range(num_colunas_B)
            for k in range(num_colunas_A):
                C[linha][coluna] += A[linha][coluna] * B[linha][coluna]
    return C
    
    