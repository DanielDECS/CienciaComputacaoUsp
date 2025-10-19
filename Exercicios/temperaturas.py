def MinMax(temperatura):
    print("A menor temperatura do mês foi: ", minima(temperatura), "C.")
    print("A maior temperatura do mês foi: ", maxima(temperatura), "C.")

def maxima(temps):
    max = temps[0]
    i = 0
    while i < len(temps):
        if temps[i] > max:
            max = temps[i]
        i = i + 1
    return max
	
def minima(temps):
    min = temps[0]
    i = 0
    while i < len(temps):
        if temps[i] < min:
            min = temps[i]
        i = i + 1
    return min
    
def testa_pontual(temp, valor_esperado):
    valor_calculado = minima(temp)
    if valor_calculado != valor_esperado:
        print("Valor errado para array ", temp)
        print("Valor esperado: ", valor_esperado,
              ". Valor calculado: ", valor_calculado)

def testa_minima():
    print("Iniciando os testes")
    testa_pontual([0], 0)
    testa_pontual([4,6,22,9,4,3], 3)
    testa_pontual([0,1,2,3,4,5], 0)
    testa_pontual([0,-1,2,-3,4,-5], -5)
    print("Teste concluido com sucesso")
