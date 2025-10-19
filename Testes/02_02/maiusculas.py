def maiusculas(frase):
    nmai = ""
    for c in frase:
        if c >= 'A' and c <= 'Z':
            nmai += c
    return nmai    
        