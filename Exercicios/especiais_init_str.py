def main():
    pri = Carro('brasilia', 1968, 'amarela', 80)
    seg = Carro('fuscao', 1981, 'preto', 95)

    print(pri)
    print(seg)

    pri.acelere(40)
    seg.acelere(50)
    pri.acelere(80)
    pri.pare()
    seg.acelere(100)

class Carro:
    def __init__(self, m, a, c, vm):
        self.modelo = m
        self.ano    = a
        self.cor    = c
        self.vel    = 0
        self.maxV   = vm  # velocidade maxima
        
    ''' Funcao subistituida pela __str__ que devolve o mesmo resultado
    def imprima(self):
        if self.vel == 0: # parado da para ver o ano
            print( "%s %s %d"%(self.modelo, self.cor, self.ano)     )
        elif self.vel < self.maxV:
            print( "%s %s indo a %d Km/h"%(self.modelo, self.cor, self.vel) )
        else:
            print( "%s %s indo muito raaaaaapiiiiiiiidoooooo!"%(self.modelo, self.cor)) '''
    
    
    ''' O código abaixo é basicamente o mesmo que o anterior, 
    mas substituimos o método imprima pelo método especial __str__. 
    No corpo desse método, ao invés de chamar a função print, 
    carrega-se um string apropriado em s, que é retornado pelo método 
    para a função print ou str. Veja que nos métodos acelere e pare, 
    basta chamar print(self).'''
    
    def __str__(self):
        if self.vel == 0: # parado da para ver o ano
            s = "%s %s %d"%(self.modelo, self.cor, self.ano)
        elif self.vel < self.maxV:
            s = "%s %s indo a %d Km/h"%(self.modelo, self.cor, self.vel)
        else:
            s = "%s %s indo muito raaaaaapiiiiiiiidoooooo!"%(self.modelo, self.cor)
        return s

    def acelere(self, v):
        self.vel = v
        if self.vel > self.maxV:
            self.vel = self.maxV
        print(self)

    def pare(self):
        self.vel = 0
        print(self)

main()