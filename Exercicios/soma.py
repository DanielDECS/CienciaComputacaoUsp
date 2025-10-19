quantidade = int(input("Digite quantos numeros deseja somar: "))
soma = 0
i = 1
while i <= quantidade:
	valor = int(input("Digite um valor a ser somado: "))
	soma = soma + valor
	i = i + 1
print("A soma dos valores digitados é: ", soma)
