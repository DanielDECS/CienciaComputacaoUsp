def maior_elemento(lista):
  maior = lista[0];
  for val in lista:
    if maior < val :
      maior = int(val)
  return maior