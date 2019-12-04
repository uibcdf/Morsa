class Animal:

    def __init__(self, nombre=None, edad=None):

        self.nombre = nombre
        self.edad = edad
        self.tipo = None

        self.suerte = asignar_suerte()
        self.habilidad = {}
        self.puntos = 0

    def quien_soy(self, solo_nombre=False):

        if solo_nombre:
            print('Soy {}'.format(self.nombre, self.edad))
        else:
            if self.tipo.endswith('o'):
                print('Soy {}, tengo {} años y soy un {}'.format(self.nombre, self.edad, self.tipo))
            else:
                print('Soy {}, tengo {} años y soy una {}'.format(self.nombre, self.edad, self.tipo))

    def cual_es_mi_mejor_habilidad(self):

        mejor_score = 0.0
        mejor_habilidad = 'Ninguna'

        for habilidad, score in self.habilidad.items():
            if mejor_score < score:
                mejor_score = score
                mejor_habilidad = habilidad

        return mejor_habilidad

def asignar_suerte():

    from numpy.random import random
    return random()

def asignar_nivel_de_habilidad():

    from numpy.random import random
    return 2.0*random()

