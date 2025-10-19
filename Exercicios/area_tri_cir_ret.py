#!/usr/bin/env python3
# Programa que calcula a área de um retângulo, círculo ou triângulo

def retangulo(lado_a, lado_b):
    """Calcula a área de um retângulo"""
    area = lado_a * lado_b
    return area

def triangulo(base, altura):
    """Calcula a área de um triângulo"""
    area = (base * altura) / 2
    return area

def circulo(raio):
    """Calcula a área de um círculo"""
    area = 3.14 * (raio ** 2)
    return area

opcao = -1
while opcao != 0:
    print('Escolha o objeto que deseja calcular a área')
    print()
    print('1 - Retângulo')
    print('2 - Triângulo')
    print('3 - Círculo')
    print('0 - Sair')
    print()
    opcao = int(input('Entre com o número da opção desejada: '))
    if (opcao == 1):
        lado_a = float(input('Entre com um lado do retângulo: '))
        lado_b = float(input('Entre com o outro lado do retângulo: '))
        area = retangulo(lado_a, lado_b)
        print('\nA área do retâgulo é: {0:.2f}'.format(area))
    elif (opcao == 2):
        lado = float(input('Entre com a base do triângulo: '))
        altura = float(input('Entre com a altura do triângulo: '))
        area = triangulo(base, altura)
        print('\nA área do triângulo é: {0:.2f}'.format(area))
    elif (opcao == 3):
        raio = float(input('Entre com o raio do cículo: '))
        area = circulo(raio)
        print('\nA área do círculo é: {0:.2f}'.format(area))
    elif (opcao != 0):
        print('\n{0} não é uma opção valida'.format(opcao))

    print()
print('Volte a qualquer hora')