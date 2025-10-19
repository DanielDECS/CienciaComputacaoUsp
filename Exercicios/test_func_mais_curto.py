def mais_curto(lista_nomes):
    valor = int(len(lista_nomes[0]))
    for item in range(len(lista_nomes)):
        item_atual = int(len(lista_nomes[item].strip()))
        if valor > item_atual:
            valor = item_atual
            resultado = lista_nomes[item]
    print(resultado.capitalize().strip())
        
def testa_mais_curto():
    mais_curto1 = []
    lista_test1 = ["Daniel", "Ilmara", "Debora", "Ana", "Paulo"]
    mais_curto(lista_test1):
    lista_test2 = ["Daniela", "Mara", "Debora", "Ana      ", "Paulo"]
    mais_curto(lista_test2):
    lista_test3(["Daniela", "Mariana", "Debora", "Ana      ", "Paulo"]
    mais_curto(lista_test3):
