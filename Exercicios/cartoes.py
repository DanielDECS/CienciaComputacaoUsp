meuCartao = int(input("Digite o número do seu cartão de crédito: "))

cartaoLido = 1
encontreiCartao = False

while cartaoLido != 0 and not encontreiCartao:
    cartaoLido = int(input("Digite o número do próximo cartão de crédito: "))
    if cartaoLido == meuCartao:
        encontreiCartao = True
if encontreiCartao:
    print("Encontrei o cartão")
else:
    print("Não encontrei o cartão")
