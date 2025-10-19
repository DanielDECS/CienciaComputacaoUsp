def maior_lexico(lista_nomes):
    valor = lista_nomes[0].lower()
    for item in range(len(lista_nomes)):
        item_atual = lista_nomes[item].lower()
        if valor > item_atual:
            valor = item_atual
            resultado = lista_nomes[item]
    print(resultado)