from package.maths.isNumber import IsNumber
from abc import ABC
from math import tan, radians, sqrt, pi

class Ponto(IsNumber):

    def __init__(self, x = 0, y = 0):
            self.x = x
            self.y = y

    def __str__(self):
        return f'Ponto({self.x};{self.y})'
    
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, x):
        if self.isNumber(x) and x >= 0:
            self._x = x
        else:
            self._x = 0

    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, y):
        if self.isNumber(y) and y >= 0:
            self._y = y
        else:
            self._y = 0

    def modulo(self):
        return sqrt(self._x ** 2 + self._y ** 2)
    
    def update(self, x, y):
        self.x = x
        self.y = y

    def type(self):
        return Ponto
    
    def model(self):
        print(self)
        print(f'Distância até a origem : {self.modulo():.2f} un')

class Circulo(Ponto):

    def __init__(self, x, y, raio):
        super().__init__(x, y)
        self.raio = raio

    def __str__(self):
        return f'Círculo na posição ({self.x};{self.y}) e de raio {self.raio}'
    
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, x):
        if self.isNumber(x) and x >= 1:
            self._x = x
        else:
            self._x = 1

    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, y):
        if self.isNumber(y) and y >= 1:
            self._y = y
        else:
            self._y = 1

    @property
    def raio(self):
        return self._raio
    
    @raio.setter
    def raio(self, raio):
        if self.isNumber(raio) and raio > 0 and raio <= self.x and raio <= self.y:
            self._raio = raio
        else:
            print('Circulo invalido, insira um novo valor')
            self.raio = self.turnInNumber(input('Raio: '))

    def diametro(self):
        return self._raio * 2

    def perimetro(self):
        return 2 * pi * self._raio

    def area(self):
        return pi * self._raio ** 2

    def type(self):
        return Circulo
    
    def update(self, x, y, raio):
        super().update(x, y)
        self.raio = raio
    
    def model(self):
        print(self.__str__())
        print(f'Diametro : {self.diametro()} un')
        print(f'Perimetro : {self.perimetro():.2f} un')
        print(f'Area : {self.area():.2f} un²')

    

class Reta:

    def __init__(self, x1, y1, x2, y2):
        self.ponto1 = Ponto(x1, y1)
        self.ponto2 = Ponto(x2, y2)


    def __str__(self):
        return f'Reta contida entre os pontos {self.ponto1} e {self.ponto2}'
    
    def coeficienteAngular(self):
        return (self.ponto1.y - self.ponto2.y) / (self.ponto1.x - self.ponto2.x)
    
    def coeficienteLinear(self):
        return  self.ponto2.y +  self.coeficienteAngular() * self.ponto2.x
    
    def equacaoReta(self):
        return f'y = ({self.coeficienteAngular()})x + ({self.coeficienteLinear()})'

    def comprimento(self):
        return sqrt((self.ponto1.x - self.ponto2.x) ** 2 + (self.ponto1.y - self.ponto2.y) ** 2)
    
    def update(self, x1, y1, x2, y2):
        self.ponto1.update(x1, y1)
        self.ponto2.update(x2, y2)


    def type(self):
        return Reta

    def model(self):
        print(self)
        print(f'Comprimento : {self.comprimento():2f} un')
        print(f'Coeficiente angular: {self.coeficienteAngular()}')
        print(f'Equacao da reta: {self.equacaoReta()}')


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


class Hexagono(Poligono):

    def __init__(self, x, y, lado):
        super().__init__(x, y, lado)
        self.numLado = 6

    def __str__(self):
        return f'Hexágono com lado = {self.lado} un'
    
    @property
    def numLado(self):
        return self._numLado
    
    @numLado.setter
    def numLado(self, x):
        if x == 6:
            self._numLado = x
        else:
            self._numLado = 6


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
    
    def type(self):
        return Retangulo
    
    def update(self, x, y, base, altura):
        self.ponto.x = x
        self.ponto.y = y
        self.base = base
        self.altura = altura
    
    def model(self):
        print(self)
        print(f'Posição : ({self.ponto.x};{self.ponto.y})')
        print(f'Perimetro : {self.perimetro()} un')
        print(f'Area : {self.area():.2f} un²')
        print(f'Numero de diagonais : {self.numDiagonal()}')
        print(f'Soma dos angulos internos : {self.anguloInterno()}º')