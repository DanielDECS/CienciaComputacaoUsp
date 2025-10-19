import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    x = 0
    for i in range (0, 6):
        x = x + (abs(as_a[i] - as_b[i]))
    grau_sim = x / 6
    if grau_sim < 0:
        grau_sim = grau_sim * (-1)
    return grau_sim
    pass

def calcula_assinatura(texto):    
    lista_de_palavras = separa_sentencas(texto)
    total_sentencas = 0
    tamanho_sentencas = 0

    frases = []
    for i in range(len(lista_de_palavras)):
        frase_aux = separa_frases(lista_de_palavras[i])
        frases.append(frase_aux)
        total_sentencas += 1
        tamanho_sentencas = tamanho_sentencas + len(lista_de_palavras[i])

    palavras = []
    total_frases = 0
    tamanho_frases = 0
    for linha in range(len(frases)):
        for coluna in range(len(frases[linha])):
            palavras_aux = separa_palavras(frases[linha][coluna])
            palavras.append(palavras_aux)
            total_frases += 1
            tamanho_frases += len(frases[linha][coluna])

    matriz_lista = []
    for linha in range(len(palavras)):
        for coluna in range(len(palavras[linha])):
            matriz_lista.append(palavras[linha][coluna])
    palavras = matriz_lista[:]

    total_letras = 0
    total_palavras = len(palavras)
    for lin in range(len(palavras)):
        for col in range(len(palavras[lin])):
            total_letras = total_letras + len(str(palavras[lin][col]))
    
    tamanho_medio_palavra = total_letras / total_palavras
    type_token = n_palavras_diferentes(palavras) / total_palavras
    hapax_legomana = n_palavras_unicas(palavras) / total_palavras
    tamanho_medio_sentenca = tamanho_sentencas / total_sentencas
    complexidade_sentenca = total_frases / total_sentencas
    tamanho_medio_frase = tamanho_frases / total_frases
    
    return [tamanho_medio_palavra, type_token, hapax_legomana, tamanho_medio_sentenca, complexidade_sentenca, tamanho_medio_frase]
    pass
def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    i = 1
    assinatura_texto = calcula_assinatura(textos[i])
    grau_similaridade = compara_assinatura(assinatura_texto, ass_cp) 
    
    menor_grau = grau_similaridade
    texto_infectado = i
    i = i + 1
    while i <(len (textos)):
        assinatura_texto = calcula_assinatura(textos[i])
        grau_similaridade = compara_assinatura(assinatura_texto, ass_cp)
        if grau_similaridade < menor_grau: 
            menor_grau = grau_similaridade
            texto_infectado = i
        i = i + 1                 
    print("O autor do texto ", texto_infectado," está infectado com COH-PIAH")
    return texto_infectado
    pass
