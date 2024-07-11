from package.maths.ponto import Ponto
from math import sqrt

class Reta:

    def __init__(self, x1, y1, x2, y2):
        self.ponto1 = Ponto(x1, y1)
        self.ponto2 = Ponto(x2, y2)

    def __str__(self):
        return f'Reta contida entre os pontos {self.ponto1} e {self.ponto2}'

    def comprimento(self):
        return sqrt((self.ponto1.x - self.ponto2.x) ** 2 + (self.ponto1.y - self.ponto2.y) ** 2)
    
    def update(self, x1, y1, x2, y2):
        self.ponto1.x = x1
        self.ponto1.y = y1
        self.ponto2.x = x2
        self.ponto2.y = y2

    def model(self):
        print(self)
        print(f'Comprimento : {self.comprimento()} un')