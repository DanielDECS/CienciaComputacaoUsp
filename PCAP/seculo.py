def seculo(ano):
    resto = ano % 100
    if resto < 0:
        sec = ano // 100
    else:
        sec = (ano // 100)+1
    return sec