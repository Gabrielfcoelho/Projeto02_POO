from package.maths.mapaCartesiano import MapaCartesiano
from package.maths.isNumber import IsNumber
from package.maths.verificador import Verificador
from package.maths.formas import Ponto, Circulo, Reta, TrianguloEquilatero, Quadrado, Retangulo, Hexagono

class Menu:

    def __init__(self):
        self._actions = [self.criar, self.exibir, self.update, self.verificar, self.remover, exit]
        self._formas = [Ponto, Circulo, Reta, TrianguloEquilatero, Quadrado, Retangulo, Hexagono]

    def criar(self):
        print('Escolha a forma geometrica:\n')
        print('1. Ponto')
        print('2. Circulo')
        print('3. Reta')
        print('4. Triangulo Equilatero')
        print('5. Quadrado')
        print('6. Retangulo')
        print('7. Hexagono\n')

        flag = 0

        while flag == 0:
                
            escolha = int(input('Digite um dos numeros acima:'))

            if escolha in range(1,8):
                flag = 1
        
        name = input('Insira um nome:')
        forma = None

        if escolha != 3:
            x = int(input('Coordenada x: '))
            y = int(input('Coordenada y: '))

            if escolha == 1:
                forma = self._formas[escolha - 1](x, y)
      
            elif escolha == 2:
                raio = int(input('Raio: '))
                forma = self._formas[escolha - 1](x, y, raio)

            elif escolha != 6:
                lado = int(input('Lado: ')) 
                forma = self._formas[escolha - 1](x, y, lado)

            else:
                base = int(input('Base: '))
                altura = int(input('Altura:')) 
                forma = self._formas[escolha - 1](x, y, base, altura)

        else:
            x = int(input('Coordenada x primeiro ponto: '))
            y = int(input('Coordenada y primeiro ponto: '))
            x2 = int(input('Coordenada x segundo ponto: '))
            y2 = int(input('Coordenada y segundo ponto: '))
            forma = self._formas[escolha - 1](x, y, x2, y2)

        MapaCartesiano.armazenarFormas(name, forma)    
        MapaCartesiano.mostrarFormas()


    def exibir(self):
        x = True
        while x:
            MapaCartesiano.mostrarFormas()
            print('1. Voltar ao menu')
            print('2. Detalhar')
            escolha = int(input('Resposta:'))
            if escolha == 1:
                x = False
            else:
                escolha = input('Digite o nome da forma que deseja detalhar:')
                MapaCartesiano.detalharFormas(escolha)

    def update(self):
        MapaCartesiano.mostrarFormas()
        name = input('\nDigite o nome da forma que deseja atualizar: ')

        if MapaCartesiano._memoria[name].type() != Reta:
            x = IsNumber.turnInNumber(input('Nova coordenada x: '))
            y = IsNumber.turnInNumber(input('Nova coordenada y: '))

            if MapaCartesiano._memoria[name].type() == Ponto:
                MapaCartesiano._memoria[name].update(x, y)
                
            elif MapaCartesiano._memoria[name].type() == Circulo:
                raio = IsNumber.turnInNumber(input('Novo Raio: '))
                MapaCartesiano._memoria[name].update(x, y, raio)

            elif MapaCartesiano._memoria[name].type() != Retangulo:
                lado = IsNumber.turnInNumber(input('Novo Lado: ')) 
                if MapaCartesiano._memoria[name].type() == TrianguloEquilatero:
                    MapaCartesiano._memoria[name].update(x, y, lado)

                elif MapaCartesiano._memoria[name].type() == Quadrado:
                    MapaCartesiano._memoria[name].update(x, y, lado)

                else:
                    MapaCartesiano._memoria[name].update(x, y, lado)

            else:
                base = IsNumber.turnInNumber(input('Nova Base: '))
                altura = IsNumber.turnInNumber(input('Nova Altura:')) 
                MapaCartesiano._memoria[name].update(x, y, base, altura)

        else:
            x = IsNumber.turnInNumber(input('Nova Coordenada x primeiro ponto: '))
            y = IsNumber.turnInNumber(input('Nova Coordenada y primeiro ponto: '))
            x2 = IsNumber.turnInNumber(input('Nova Coordenada x segundo ponto: '))
            y2 = IsNumber.turnInNumber(input('Nova Coordenada y segundo ponto: '))
            MapaCartesiano._memoria[name].update(x, y, x2, y2)

        print('1. Voltar ao menu')
        print('2. Atualizar mais formas')
        escolha = int(input('Resposta:'))
        if escolha == 2:
            self.update()            
        
    def verificar(self):
        pass

    def remover(self):
        MapaCartesiano.mostrarFormas()
        name = input('\nDigite o nome da forma que deseja atualizar: ')
        MapaCartesiano.removerFormas(name)

    def run(self):
        while True:

            print('\n########## Bem vindo ao Projeto 2! ##########\n')
            print('Menu:\n')
            print('1. Criar Formas Geometricas')
            print('2. Mostrar Formas Geometricas Criadas')
            print('3. Atualizar Formas Geometricas Criadas')
            print('4. Fazer verificacoes')
            print('5. Remover Formas Geometricas')
            print('6. Sair\n')

            flag = 0

            while flag == 0:
                        
                escolha = int(input('Digite um dos numeros acima:'))

                if int(escolha) in range(1,7):
                    flag = 1
                else:
                    print('Valor invalido! Tente novamente')
            
            self._actions[escolha - 1]()