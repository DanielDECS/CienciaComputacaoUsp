def sao_multiplicaveis(m1, m2):
    num_linhas_A, num_colunas_A = len(m1), len(m1[0])
    num_linhas_B, num_colunas_B = len(m2), len(m2[0])
    if num_colunas_A == num_linhas_B:
        return True
    else:
        return False

    
    