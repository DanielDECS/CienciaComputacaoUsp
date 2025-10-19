# -*- coding: utf-8 -*-
"""
fv = valor futuro.
pv = valor presente.
i = juros mensal
n = prazo para pagamento em parcelas mensais
"""
def calcula_Juros(pv, i, n):
    fv = 0
    fv = pv *((1 + i / 100) **n)
    return(fv)

a = float(input("Entre com o valor atual: "))
b = float(input("Entre com a porcentagem de juros atual: "))
c = float(input("Entre com o prazo desejado: "))

print(calcula_Juros(a, b, c))