from package.maths.poligono import Poligono

class Eneagono(Poligono):

    def __init__(self, x, y, lado):
        super().__init__(x, y, lado)
        self.numLado = 9

    def __str__(self):
        return f'Eneágono com lado = {self.lado} un'
    
    @property
    def numLado(self):
        return self._numLado
    
    @numLado.setter
    def numLado(self, x):
        if x == 9:
            self._numLado = x
        else:
            self._numLado = 9