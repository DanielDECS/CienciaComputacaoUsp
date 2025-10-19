minhaLista = []
trocado = True
num = int(input("Quantos elementos você deseja ordenar: "))

for i in range(num):
    valor = float(input("Informe o elemento da lista: "))
    minhaLista.append(valor)

while trocado:
    trocado = False
    for i in range(len(minhaLista) - 1):
        if minhaLista[i] > minhaLista[i + 1]:
            trocado = True
            minhaLista[i], minhaLista[i + 1] = minhaLista[i + 1], minhaLista[i]

print("\nOrdenado:")
print(minhaLista)