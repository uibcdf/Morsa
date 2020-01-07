class Animal:

    """Jugador de tipo general

    Los jugadores son animales con los siguientes atributos y funciones.
    Las distintas clases de jugadores como especies animales (ballena, pingüino o morsa) heredaran todo
    lo relativo a esta superclase.

    Attributes
    ----------
    nombre : str
        Nombre propio del jugador.
    edad : int
        Edad del jugador.
    especie : str or None
        Especie animal a la que pertenece el jugador.
    suerte : float
        Numero flotante entre 0.0 y 1.0 que define el factor suerte del jugador.
    habilidad : dict
        Diccionario que almacena el nombre de los juegos que el jugador conoce (claves del
        diccionario) y los numeros flotantes entre 0.0 y 1.0 que definen el factor habilidad para
        cada juego (valores del diccionario).
    puntos : int
        Puntuación del jugador.

    Methods
    -------
    reiniciar_puntos()
        El atributo puntos adquiere el valor 0.
    quien_soy(solo_nombre=False)
        Devuelve un string que presenta al jugador.
    cual_es_mi_mejor_habilidad()
        Devuele el nombre del juego en el que el jugador es más habil.

    """

    def __init__(self, nombre=None, edad=None):

        """Inicialización de la clase Animal

        Un jugador animal, de especie desconocida o sin especie, puede ser instancializado
        especificando, optativamente, su nombre y edad.

        Parameters
        ----------
        nombre : str or None, optional
            Nombre propio del jugador (`None` por defecto). Si el valor es `None` el nombre propio es
            generado aleatoriamente.
        edad : int or None, optional
            Edad del jugador (`None` por defecto). Si el valor es `None` la edad es generada
            aleatoriamente como un entero entre 18 y 100.

        Methods
        -------
        reiniciar_puntos()
            El atributo puntos adquiere el valor 0.
        quien_soy(solo_nombre=False)
            Devuelve un string que presenta al jugador.
        cual_es_mi_mejor_habilidad()
            Devuele el nombre del juego en el que el jugador es más habil.

        """


        self.nombre = nombre
        self.edad = edad
        self.especie = None

        self.suerte = asignar_suerte()
        self.habilidad = {}
        self.puntos = 0

        if self.nombre is None:
            from faker import Faker as _generador_identidades
            self.nombre = _generador_identidades('es_ES').name()

        if self.edad is None:
            from numpy.random import randint as _randint
            self.edad = _randint(18,100)

    def reiniciar_puntos(self):

        """Puntuación a cero

        El valor del atributo `puntos` es reinicializado a cero.

        Examples
        --------

        >>> jugador = Animal()
        >>> jugador.puntos = 100
        >>> jugador.reiniciar_puntos()
        >>> print(jugador.puntos)
        0

        """

        self.puntos = 0

    def quien_soy(self, solo_nombre=False):

        """Presentación del jugador

        Devuelve una frase presentando al jugador mencionando su nombre, edad y especie, o
        únicamente su nombre.

        Parameters
        ----------
        solo_nombre : bool, optional
            La frase de salida puede contener únicamente el nombre del jugador, si
            `solo_nombre`=True, o su nombre, edad y especie, si `solo_nombre`=False (valor por
            defecto).

        Examples
        --------

        >>> jugador = Animal(nombre='Ramón', edad=40)
        >>> jugador.especie = 'morsa'
        >>> print(jugador.quien_soy(solo_nombre=True))
        Soy Ramón
        >>> print(jugador.quien_soy())
        Soy Ramón, tengo 40 años y soy una morsa

        """

        if solo_nombre:
            print('Soy {}'.format(self.nombre, self.edad))
        else:
            if self.especie.endswith('o'):
                print('Soy {}, tengo {} años y soy un {}'.format(self.nombre, self.edad, self.especie))
            else:
                print('Soy {}, tengo {} años y soy una {}'.format(self.nombre, self.edad, self.especie))

    def cual_es_mi_mejor_habilidad(self):

        """Juego con mayor habilidad

        Devuelve el nombre del juego con el factor de habilidad más alto.

        Returns
        -------
        juego: str
            Nombre del juego con el factor habilidad más alto.

        Examples
        --------

        >>> jugador = Animal()
        >>> print(jugador.cual_es_mi_mejor_habilidad())
        Ninguna

        Las clases `Ballena`, `Pinguino` y `Morsa` heredan todos los atributos y métodos de la
        clase `Animal`:

        >>> jugador = Ballena()
        >>> print(jugador.cual_es_mi_mejor_habilidad())
        'dominó'

        """

        mejor_score = 0.0
        mejor_habilidad = 'Ninguna'

        for habilidad, score in self.habilidad.items():
            if mejor_score < score:
                mejor_score = score
                mejor_habilidad = habilidad

        return mejor_habilidad

def asignar_suerte():

        """Generación aleatoria del factor suerte

        Devuelve un número flotante aleatorio entre 0.0 y 1.0.

        Returns
        -------
        factor_suerte: float
            Número flotante aleatorio entre 0.0 y 1.0.

        Examples
        --------

        >>> asignar_suerte()
        0.52
        >>> asignar_suerte()
        0.18

        """

    from numpy.random import random
    return random()

def asignar_nivel_de_habilidad():

        """Generación aleatoria del factor habilidad

        Devuelve un número flotante aleatorio entre 0.0 y 1.0.

        Returns
        -------
        factor_habilidad: float
            Número flotante aleatorio entre 0.0 y 1.0.

        Examples
        --------

        >>> asignar_nivel_de_habilidad()
        0.85
        >>> asignar_nivel_de_habilidad()
        0.64

        """

    from numpy.random import random
    return random()

