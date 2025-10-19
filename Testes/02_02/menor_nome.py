def menor_nome(nomes):
    valor = int(len(nomes[0]))
    resultado = ""
    for item in range(len(nomes)):
        item_atual = int(len(nomes[item].strip()))
        if valor > item_atual:
            resultado = nomes[item]
            valor = item_atual
        if resultado == "":
            resultado = nomes[0]
    return resultado.strip().capitalize()
