"""
A função nomeada incIntsI()obtém um objeto de qualquer classe, verifica seu 
conteúdo para encontrar todos os atributos inteiros com nomes começando com i 
e os incrementa em um.

Impossível? De modo nenhum!

É assim que funciona:

linha 1: defina uma classe muito simples ...
linhas 3 a 10: ... e preencha-o com alguns atributos;
linha 12: esta é a nossa função!
linha 13: verifique o __dict__atributo, procurando por todos os nomes de atributos;
linha 14: se um nome começa com i ...
linha 15: ... use a getattr()função para obter seu valor atual; nota: 
    getattr()recebe dois argumentos: um objeto e seu nome de propriedade 
    (como uma string) e retorna o valor do atributo atual;
linha 16: verifique se o valor é do tipo inteiro e use a função isinstance()
para esse propósito (discutiremos isso mais tarde);
linha 17: se a verificação for bem, incremente o valor da propriedade utilizando 
a setattr()função; a função recebe três argumentos: um objeto, o nome da 
propriedade (como uma string) e o novo valor da propriedade.
"""

class MyClass:
    pass

obj = MyClass()
obj.a = 1
obj.b = 2
obj.i = 3
obj.ireal = 3.5
obj.integer = 4
obj.z = 5

def incIntsI(obj):
    for name in obj.__dict__.keys():
        if name.startswith('i'):
            val = getattr(obj, name)
            if isinstance(val, int):
                setattr(obj, name, val + 1)

print(obj.__dict__)
incIntsI(obj)
print(obj.__dict__)