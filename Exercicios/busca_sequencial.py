def busca_sequencial(seq, x):
    for i in range(len(seq)):
        if seq[i] == x:
            return True
    return False