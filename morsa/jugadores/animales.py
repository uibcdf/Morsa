from .plantilla import Animal
from .plantilla import asignar_nivel_de_habilidad
from .plantilla import asignar_suerte

class Morsa(Animal):

    def __init__(self, nombre=None, edad=None):

        super().__init__(nombre=nombre, edad=edad)

        self.tipo = 'morsa'

        for juego in ['parchís', 'dominó', 'tres en raya']:
            self.habilidad[juego] = asignar_nivel_de_habilidad()

    def reasigno_suerte(self):

        self.suerte = asignar_suerte()

class Pinguino(Animal):

    def __init__(self, nombre=None, edad=None):

        super().__init__(nombre=nombre, edad=edad)

        self.tipo = 'pingüino'

        for juego in ['ajedrez', 'dominó', 'tres en raya']:
            self.habilidad[juego] = asignar_nivel_de_habilidad()

    def reasigno_habilidades(self):

        for juego in ['ajedrez', 'dominó', 'tres en raya']:
            self.habilidad[juego] = asignar_nivel_de_habilidad()

class Ballena(Animal):

    def __init__(self, nombre=None, edad=None):

        super().__init__(nombre=nombre, edad=edad)

        self.tipo = 'ballena'

        for juego in ['parchís', 'dominó', 'ajedrez']:
            self.habilidad[juego] = asignar_nivel_de_habilidad()

    def reasigno_suerte_y_habilidades(self):

        for juego in ['parchís', 'dominó', 'ajedrez']:
            self.habilidad[juego] = asignar_nivel_de_habilidad()

        self.suerte = asignar_suerte()

