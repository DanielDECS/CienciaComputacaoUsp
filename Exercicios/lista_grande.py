def lista_grande(n):
   import random
   tamanho = n
   resposta = [2] * tamanho
   for i in range(tamanho):
       resposta[i] = random.randrange(20)
   return resposta
   
#Exemplo de gerador, numeros = random.sample(range(1, 1000), 42)