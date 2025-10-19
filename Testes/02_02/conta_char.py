def conta_letras(frase, contar = "vogais"):
    nv = 0
    nc = 0
    vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for letra in frase:
        if letra in vogais:
            nv += 1
        if letra not in vogais and letra != " ":
            nc += 1   
    if contar == "vogais" or contar == "":
        return nv
    if contar == "consoantes":
        return nc
