from package.maths.poligono import Poligono
from math import sqrt

class Quadrado(Poligono):

    def __init__(self, x, y, lado):
        super().__init__(x, y, lado)
        self.numLado = 4

    def __str__(self):
        return f'Quadrado com lado = {self.lado} un'
    
    @property
    def numLado(self):
        return self._numLado
    
    @numLado.setter
    def numLado(self, x):
        if x == 4:
            self._numLado = x
        else:
            self._numLado = 4
    
    def apotema(self):
        return self.lado / 2
    
    def diagonal(self):
        return self.lado * sqrt(2)
    
    def model(self):
        super().model()
        print(f'Tamanho da Diagonal : {self.diagonal():.2f} un')