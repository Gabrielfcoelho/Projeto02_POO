from package.maths.poligono import Poligono

class Icosagono(Poligono):

    def __init__(self, x, y, lado):
        super().__init__(x, y, lado)
        self.numLado = 20

    def __str__(self):
        return f'Icoságono com lado = {self.lado} un'
    
    @property
    def numLado(self):
        return self._numLado
    
    @numLado.setter
    def numLado(self, x):
        if x == 20:
            self._numLado = x
        else:
            self._numLado = 20