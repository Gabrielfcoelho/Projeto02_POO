from package.maths.ponto import Ponto
from package.maths.isNumber import IsNumber
from math import sqrt

class TrianguloEscaleno:

    def __init__(self, x, y, lado, lado2, lado3):
        self.ponto = Ponto(x, y)
        self.lado = lado
        self.lado2 = lado2
        self.lado3 = lado3
        self.__numLado = 3

    def __str__(self):
        return f'Triângulo Escaleno com lados iguais a {self.lado}, {self.lado2} e {self.lado3}'

    @property
    def lado(self):
        return self._lado

    @lado.setter
    def lado(self, lado):
        if IsNumber.isNumber(lado) and lado > 0:
            self._lado = lado
        else:
            self._lado = 1

    @property
    def lado2(self):
        return self._lado2
    
    @lado2.setter
    def lado2(self, lado2):
        if IsNumber.isNumber(lado2) and lado2 < (self.lado * 2) and lado2 != self.lado:
            self._lado2 = lado2
        else:
            self._lado2 = (self.lado * 2) - 1

    @property
    def lado3(self):
        return self._lado3
    
    @lado3.setter
    def lado3(self, lado3):
        if IsNumber.isNumber(lado3) and lado3 != self.lado2 and lado3 != self.lado and lado3 < self.lado + self.lado2:
            self._lado3 = lado3
        else:
            self._lado3 = (self.lado * 2) - 2

    def perimetro(self):
        return self.lado3 + self.lado + self.lado2
    
    def area(self):
        semiPerimetro = self.perimetro() / 2
        return sqrt(semiPerimetro * (semiPerimetro - self.lado) * (semiPerimetro - self.lado2) * (semiPerimetro - self.lado3))
    
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