from package.maths.isNumber import IsNumber
from abc import ABC
from package.maths.ponto import Ponto
from math import tan, radians

class Poligono(ABC, IsNumber):
    _numLado = 3

    def __init__(self, x, y, lado):
        self.ponto = Ponto(x, y) 
        self.lado = lado
        

    def __str__(self):
        return f'Este polígono possui {self.numLado} lados de tamanho {self.lado} un'

    @property
    def numLado(self):
        return self._numLado
    
    @numLado.setter
    def numLado(self, x):
        if self.isNumber(x) and x >= 3:
            self._numLado = x
        else:
            self._numLado = 3
    
    @property
    def lado(self):
        return self._lado
    
    @lado.setter
    def lado(self, lado):
        if self.isNumber(lado) and lado > 0:
            self._lado = lado
        else:
            self._lado = 1

    def perimetro(self):
        return self.numLado * self.lado

    def area(self):
       return self.apotema() * self.perimetro() / 2

    def numDiagonal(self):
        return int(self.numLado * (self.numLado - 3) / 2)
    
    def anguloInterno(self):
        return (self.numLado - 2) * 180

    def apotema(self):
        return (self.lado / 2) / (tan(radians(360 / (self.numLado * 2))))
    
    def type(self):
        return Poligono
    
    def update(self, x, y, lado):
        self.ponto.x = x
        self.ponto.y = y
        self.lado = lado

    def model(self):
        print(self)
        print(f'Posição : ({self.ponto.x};{self.ponto.y})')
        print(f'Perimetro : {self.perimetro()} un')
        print(f'Area : {self.area():.2f} un²')
        print(f'Numero de diagonais : {self.numDiagonal()}')
        print(f'Soma dos angulos internos : {self.anguloInterno()}º')
