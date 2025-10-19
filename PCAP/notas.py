total_notas = int(input("Digite o numero de notas entre dez e zero que deseja somar para saber a média : "))
contador = 0
soma = 0
while contador < total_notas:
    nota_atual = float(input("Digite a nota atual : "))
    if nota_atual > 10:
        print("O valor digitado é maior que 10 e será descartado")
        contador -= 1
    elif nota_atual < 0:
        print("O valor digitado é menor que 0 e será descartado")
        contador -= 1
    else:
        soma += nota_atual
    contador += 1
media = soma / contador
print("A média das notas do aluno é : ", media)
