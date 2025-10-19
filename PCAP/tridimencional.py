"""
Python não limita a profundidade da inclusão list-in-list. Aqui você pode ver
 um exemplo de uma matriz tridimensional:

Imagine um hotel. É um enorme hotel composto por três edifícios de 15 andares cada. 
Existem 20 quartos em cada andar. Para isso, você precisa de um array que possa coletar
 e processar informações sobre os quartos ocupados / livres.

Primeira etapa - o tipo dos elementos da matriz. Nesse caso, caberia um valor booleano
 ( True/ False).

Etapa dois - análise calma da situação. Resuma a informação disponível: três edifícios,
 15 andares, 20 quartos.

O primeiro índice ( 0por meio de 2) seleciona um dos edifícios; o segundo ( 0a 14) 
seleciona o andar, o terceiro ( 0a 19) seleciona o número do quarto. Todos os quartos
 são inicialmente gratuitos.

Agora você pode reservar um quarto para dois noivos: no segundo prédio, no décimo andar, 
quarto 14 e liberar o segundo quarto no quinto andar localizado no primeiro edifício.
Verifique se há vagas no 15º andar do terceiro prédio:

A vacancy variável contém 0 se todos os quartos estão ocupados ou o número de 
quartos disponíveis, caso contrário.
    
    
"""
rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]
rooms[1][9][13] = True
rooms[0][4][1] = False
vacancy = 0

for roomNumber in range(20):
    if not rooms[2][14][roomNumber]:
        vacancy += 1
