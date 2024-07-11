from package.maths.poligono import Poligono
from math import sqrt

class TrianguloEquilatero(Poligono):

    def __init__(self, x, y, lado):
        super().__init__(x, y, lado)


    def __str__(self):
        return f'Triângulo Equilátero com lado = {self.lado} un'
    
    @property
    def numLado(self):
        return self._numLado
    
    @numLado.setter
    def numLado(self, x):
        if x == 3:
            self._numLado = x
        else:
            self._numLado = 3

    def altura(self):
        return self.lado * sqrt(3) / 2
    
    def apotema(self):
        return self.altura() / 3
    
    def model(self):
        super().model()
        print(f'Altura : {self.altura():.2f} un')