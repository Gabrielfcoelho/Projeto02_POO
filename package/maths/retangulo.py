from package.maths.ponto import Ponto
from package.maths.isNumber import IsNumber
from math import sqrt


class Retangulo:

    def __init__(self, x, y, base, altura):
        self.ponto = Ponto(x, y)
        self.base = base
        self.altura = altura
        self.__numLado = 4

    def __str__(self):
        return f'Retângulo com base = {self.base} e altura = {self.altura}'

    @property
    def base(self):
        return self._base
    
    @base.setter
    def base(self, base):
        if IsNumber.isNumber(base) and base > 0:
            self._base = base
        else:
            self._base = 1

    @property
    def altura(self):
        return self._altura
    
    @altura.setter
    def altura(self, altura):
        if IsNumber.isNumber(altura) and altura > 0:
            self._altura = altura
        else:
            self._altura = 1
    
    def perimetro(self):
        return 2 * self.base + 2 * self.altura
    
    def area(self):
        return self.base * self.altura
    
    def diagonal(self):
        return sqrt(self.base ** 2 + self.altura ** 2)
    
    def numDiagonal(self):
        return int(self.__numLado * (self.__numLado - 3) / 2)
    
    def anguloInterno(self):
        return (self.__numLado - 2) * 180
    
    def model(self):
        print(self)
        print(f'Posição : ({self.ponto.x};{self.ponto.y})')
        print(f'Perimetro : {self.perimetro()} un')
        print(f'Area : {self.area():.2f} un²')
        print(f'Numero de diagonais : {self.numDiagonal()}')
        print(f'Soma dos angulos internos : {self.anguloInterno()}º')