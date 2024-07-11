from package.maths.poligono import Poligono

class Decagono(Poligono):

    def __init__(self, x, y, lado):
        super().__init__(x, y, lado)
        self.numLado = 10

    def __str__(self):
        return f'Decágono com lado = {self.lado} un'
    
    @property
    def numLado(self):
        return self._numLado
    
    @numLado.setter
    def numLado(self, x):
        if x == 10:
            self._numLado = x
        else:
            self._numLado = 10