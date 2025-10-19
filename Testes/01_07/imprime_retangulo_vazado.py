largura = int(input('digite a largura: '))
altura = int(input('digite a altura: '))
l = 1 
a = 1
while a <= altura:
   print('#' * largura, end = '')
   print()
   a = a + 1
   while a > 1 and a < altura:
      print('#' + ' ' * (largura - 2) + '#')
      a = a + 1