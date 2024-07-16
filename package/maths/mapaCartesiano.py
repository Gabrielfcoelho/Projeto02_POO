class MapaCartesiano:

    _memoria = {}


    @classmethod
    def armazenarFormas(cls, name, formaGeometrica):
        cls._memoria.update({name : formaGeometrica})

    @classmethod
    def mostrarFormas(cls):
        for i in cls._memoria:
            print(f'{i} : {cls._memoria[i]}')

    @classmethod
    def detalharFormas(cls, name):
        cls._memoria[name].model()

    @classmethod
    def removerFormas(cls, name):
        cls._memoria.pop(name)
