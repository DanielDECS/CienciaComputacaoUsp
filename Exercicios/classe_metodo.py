# Atribuição de valores aos objetos e uso dos metodos
def main():
    carro1 = Carro('Ferrari', 2010, 'vermelha', 80)
    carro2 = Carro('McLarem', 2020, 'prata', 95)
    
    carro1.acelera(40)
    carro2.acelera(50)
    carro1.acelera(80)
    carro1.pare()
    carro2.acelera(100)

# Definião da Classe e dos atributos dos objetos
class Carro:
    def __init__(self, m, a, c, vm):
        self.modelo = m
        self.ano    = a
        self.cor    = c
        self.maxVel = vm
        self.vel    = 0

    def imprima(self):
        if self.vel ==0:
            print("%s %s %s"%(self.modelo, self.cor, self.ano))
        elif self.vel < self.maxVel:
            print("%s %s indo a %s Km/h"%(self.modelo, self.cor, self.vel))
        else:
            print("%s %s indo a muito rápido!!!!"%(self.modelo, self.cor))
            
    def acelera(self, velocidade):
        self.vel = velocidade
        if self.vel > self.maxVel:
            self.vel = self.maxVel
        self.imprima()
    
    def pare(self):
        self.vel = 0
        self.imprima()

main()
        