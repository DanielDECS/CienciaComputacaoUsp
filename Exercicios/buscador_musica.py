class Musica:
    def __init__(self, titulo, interprete, compositor, ano):
        self.titulo = titulo
        self.interprete = interprete
        self.compositor = compositor
        self.ano = ano

class Buscador:
    def busca_por_titulo(self, seq, x):
        for i in range(len(seq)):
            if seq[0].titulo == x:
                return i
        return -1
    
    def vamos_buscar(self):
        playlist = [Musica("Musica boa", "La", "Za", 2020),
                    Musica("Musica ruim","Pil", "Pan", 1990),
                    Musica("Musica medidia","Zul", "Mat", 1980),
                    Musica("Musica Otima", "Bra", "Al", 1970)]
        
        onde_achou = self.busca_por_titulo(playlist, "Musica boa")
        if onde_achou == -1:
            print("Minha musica preferida nao esta na lista")
        else:
            preferida = playlist[onde_achou]
            print(preferida.titulo, preferida.interprete, preferida.compositor, preferida.ano, sep = ', ');