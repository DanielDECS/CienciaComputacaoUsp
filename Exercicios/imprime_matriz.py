def imprime_matriz(minha_matriz):
    for lin in range(len(minha_matriz)):
        contador = 0
        for col in range(len(minha_matriz[lin])):
            a = int(minha_matriz[lin] [col])
            contador = contador + 1
            if len(minha_matriz[lin]) == contador:
                print(a,end='')
            else:
                print(a,end=' ')
        print(end='\n')
