"""
O primeiro problema que queremos mostrar a você é chamado de cifra de César - 
mais detalhes aqui: https://en.wikipedia.org/wiki/Caesar_cipher .

Esta cifra foi (provavelmente) inventada e usada por Gaius Julius Caesar e suas 
tropas durante as Guerras Gálicas. A ideia é bastante simples - cada letra da 
mensagem é substituída pelo seu consequente mais próximo ( A torna-se B , B 
torna-se C e assim por diante). A única excepção é Z , que se torna um .

O programa no editor é uma implementação muito simples (mas funcional) do 
algoritmo.

Nós o escrevemos usando as seguintes suposições:

aceita apenas letras latinas (nota: os romanos não usavam espaços em branco 
nem dígitos)
todas as letras da mensagem estão em maiúsculas (nota: os romanos conheciam 
apenas maiúsculas)
Vamos rastrear o código:

linha 02: peça ao usuário para inserir a mensagem aberta (não criptografada) 
de uma linha;
linha 03: prepare uma string para uma mensagem criptografada (vazia por enquanto)
linha 04: inicie a iteração através da mensagem;
linha 05: se o caractere atual não for alfabético ...
linha 06: ... ignore;
linha 07: converta a letra para maiúsculas (é preferível fazer isso às cegas, 
em vez de verificar se é necessário ou não)
linha 08: pegue o código da letra e aumente em um;
linha 09: se o código resultante tiver "deixado" o alfabeto latino (se for 
maior que o código Z ) ...
linha 10: ... mude para o código A ;
linha 11: acrescenta o caractere recebido ao final da mensagem criptografada;
linha 13: imprime a cifra.
O código, alimentado com esta mensagem:

AVE CAESAR

saídas:

BWFDBFTBS

Faça seus próprios testes.

"""
text = input("Enter your message: ")
cipher = ''
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + 1
    if code > ord('Z'):
        code = ord('A')
    cipher += chr(code)

print(cipher)



