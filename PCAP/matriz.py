"""
Natureza multidimensional das listas: aplicativos avançados
Vamos nos aprofundar na natureza multidimensional das listas. 
Para encontrar qualquer elemento de uma lista bidimensional, 
você deve usar duas coordenadas :

um vertical (número da linha)
e um horizontal (número da coluna).
Imagine que você desenvolva um software para uma estação meteorológica automática. 
O aparelho registra a temperatura do ar de hora em hora e faz isso ao longo do mês. 
Isso dá a você um total de 24 × 31 = 744 valores. 
Vamos tentar criar uma lista capaz de armazenar todos esses resultados.

Primeiro, você deve decidir qual tipo de dados seria adequado para este aplicativo. 
Nesse caso, floatseria melhor, uma vez que este termômetro é capaz de medir a 
temperatura com uma precisão de 0,1 ℃.

Então você toma uma decisão arbitrária de que as linhas irão registrar as leituras 
a cada hora na hora (então a linha terá 24 elementos) e cada uma das linhas será 
atribuída a um dia do mês (vamos supor que cada mês tenha 31 dias , então você precisa 
de 31 linhas). Aqui está o par apropriado de compreensões ( hé para hora, dpara dia):
"""
# A matriz inteira está preenchida com zeros agora

temps = [[0.0 for h in range(24)] for d in range(31)]
#
# the matrix is magically updated here
#

"""
Agora é hora de determinar a temperatura média mensal do meio-dia. 
Some todas as 31 leituras registradas ao meio-dia e divida a soma por 31. 
Você pode presumir que a temperatura da meia-noite é armazenada primeiro.
Nota: a dayvariável usada pelo forloop não é um escalar - cada passagem pela 
tempsmatriz a atribui às linhas subsequentes da matriz; portanto, é uma lista. 
Deve ser indexado com 11para acessar o valor de temperatura medido ao meio-dia.
"""
total = 0.0

for day in temps:
    total += day[11]

average = total / 31

print("Average temperature at noon:", average)

#Agora encontre a temperatura mais alta durante todo o mês
#a day variável percorre todas as linhas da tempsmatriz;
# a temp variável itera por meio de todas as medições feitas em um dia.

highest = -100.0

for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp

print("The highest temperature was:", highest)

#Agora conte os dias em que a temperatura ao meio-dia foi de pelo menos 20 ℃:
hotDays = 0

for day in temps:
    if day[11] > 20.0:
        hotDays += 1

print(hotDays, "days were hot.")