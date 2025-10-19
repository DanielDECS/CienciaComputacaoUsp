def primeiro_lex(lista):
    valor = lista[0].lower()
    resultado = ""
    for item in range(len(lista)):
        item_atual = lista[item].lower()
        if valor > item_atual:
            valor = item_atual
            resultado = lista[item]
        if resultado == "":
            resultado = lista[0]
    return resultado
