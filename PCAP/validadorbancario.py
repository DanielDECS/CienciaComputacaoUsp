"""O Validador IBAN
O quarto programa implementa (em uma forma ligeiramente simplificada) um algoritmo usado por bancos europeus para especificar números de contas. O padrão denominado IBAN (Número de Conta Bancária Internacional) fornece um método simples e bastante confiável de validação dos números das contas contra erros de digitação simples que podem ocorrer durante a reconfiguração do número, por exemplo, de documentos em papel, como faturas ou contas, para computadores.

Você pode encontrar mais detalhes aqui: https://en.wikipedia.org/wiki/International_Bank_Account_Number .

Um número de conta compatível com IBAN consiste em:

um código de país de duas letras retirado do padrão ISO 3166-1 (por exemplo, FR para França, GB para Grã-Bretanha, DE para Alemanha e assim por diante)
dois dígitos de verificação usados ​​para realizar as verificações de validade - testes rápidos e simples, mas não totalmente confiáveis, mostrando se um número é inválido (distorcido por um erro de digitação) ou parece ser bom;
o número real da conta (até 30 caracteres alfanuméricos - o comprimento dessa parte depende do país)
O padrão diz que a validação requer as seguintes etapas (de acordo com a Wikipedia):

(etapa 1) Verifique se o comprimento total do IBAN está correto de acordo com o país (este programa não fará isso, mas você pode modificar o código para atender a este requisito se desejar; observação: você deve ensinar o código todos os comprimentos usado na Europa)
(etapa 2) Mova os quatro caracteres iniciais para o final da string (ou seja, o código do país e os dígitos de verificação)
(etapa 3) Substitua cada letra da string por dois dígitos, expandindo assim a string, onde A = 10 , B = 11 ... Z = 35 ;
(etapa 4) Interprete a string como um inteiro decimal e calcule o restante desse número na divisão por 97; Se o resto for 1 , o teste do dígito de verificação foi aprovado e o IBAN pode ser válido.
Observe o código no editor. Vamos analisar:

linha 03: peça ao usuário para inserir o IBAN (o número pode conter espaços, pois melhoram significativamente a legibilidade do número ...
linha 04: ... mas remova-os imediatamente)
linha 05: o IBAN inserido deve consistir em apenas dígitos e letras - se não ...
linha 06: ... envia a mensagem;
linha 07: o IBAN não deve ter menos de 15 caracteres (esta é a variante mais curta, usada na Noruega)
linha 08: se for mais curta, o usuário é informado;
linha 09: além disso, o IBAN não pode ter mais de 31 caracteres (esta é a variante mais longa, usada em Malta)
linha 10: se for mais longa, faça um anúncio;
linha 11: inicia o processamento real;
linha 12: mova os quatro caracteres iniciais para o final do número e converta todas as letras para maiúsculas (etapa 02 do algoritmo)
linha 13: esta é a variável utilizada para completar o número, criada a partir da substituição das letras por dígitos (conforme passo 03 do algoritmo)
linha 14: itera por meio do IBAN;
linha 15: se o caractere for um dígito ...
linha 16: apenas copie;
linha 17: caso contrário ...
linha 18: ... converta em dois dígitos (observe a maneira como é feito aqui)
linha 19: a forma convertida do IBAN está pronta - faça um inteiro a partir dela;
linha 20: o resto da divisão de iban2por é 97igual a 1?
linha 21: Se sim, então sucesso;
linha 22: Caso contrário ...
linha 23: ... o número é inválido.
Vamos adicionar alguns dados de teste (todos esses números são válidos - você pode invalidá-los alterando qualquer caractere).

Britânico: GB72 HBZU 7006 7212 1253 00
Francês: FR76 30003 03620 00020216907 50
Alemão: DE02100100100152517108
Se você é residente na UE, pode usar o número da sua conta para os testes.
"""

# IBAN Validator

iban = input("Enter IBAN, please: ")
iban = iban.replace(' ','')
if not iban.isalnum():
    print("You have entered invalid characters.")
elif len(iban) < 15:
    print("IBAN entered is too short.")
elif len(iban) > 31:
    print("IBAN entered is too long.")
else:
    iban = (iban[4:] + iban[0:4]).upper()
    iban2 = ''
    for ch in iban:
        if ch.isdigit():
            iban2 += ch
        else:
            iban2 += str(10 + ord(ch) - ord('A'))
    ibann = int(iban2)
    if ibann % 97 == 1:
        print("IBAN entered is valid.")
    else:
        print("IBAN entered is invalid.")