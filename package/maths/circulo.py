from package.maths.ponto import Ponto
from math import pi


class Circulo(Ponto):

    def __init__(self, x, y, raio):
        super().__init__(x, y)
        self.raio = raio

    def __str__(self):
        return f'Círculo na posição ({self.x};{self.y}) e de raio {self.raio}'

    @property
    def raio(self):
        return self._raio
    
    @raio.setter
    def raio(self, raio):
        if self.isNumber(raio) and raio > 0:
            self._raio = raio
        else:
            self._raio = 1

    def diametro(self):
        return self._raio * 2

    def perimetro(self):
        return 2 * pi * self._raio

    def area(self):
        return pi * self._raio ** 2

    def model(self):
        print(self.__str__())
        print(f'Diametro : {self.diametro()} un')
        print(f'Perimetro : {self.perimetro():.2f} un')
        print(f'Area : {self.area():.2f} un²')

    def type(self):
        return Circulo