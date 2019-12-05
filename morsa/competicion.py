
def jugar(juego=None, jugador1=None, jugador2=None, verbose=False):

    from .juegos import _reparte_puntos
    from numpy.random import random

    for jugador in [jugador1, jugador2]:
        if juego not in jugador.habilidad:
            if verbose:
                print("{} no sabe jugar {}".format(jugador.nombre, juego))
            return

    inspiracion_jugador1 = 2.0*random()
    inspiracion_jugador2 = 2.0*random()

    acierto_jugador1 = inspiracion_jugador1+jugador1.suerte*jugador1.habilidad[juego]
    acierto_jugador2 = inspiracion_jugador2+jugador2.suerte*jugador2.habilidad[juego]

    resultado = None

    if acierto_jugador1>acierto_jugador2:

        jugador1.puntos += _reparte_puntos(juego,'gana')
        jugador2.puntos += _reparte_puntos(juego,'pierde')

        if verbose:
            resultado = "Ganó {}".format(jugador1.nombre)

    elif acierto_jugador2>acierto_jugador1:

        jugador2.puntos += _reparte_puntos(juego,'gana')
        jugador1.puntos += _reparte_puntos(juego,'pierde')

        if verbose:
            resultado = "Ganó {}".format(jugador2.nombre)

    else:

        if verbose:
            resultado = "Ninguno gana"

def quien_tiene_mas_puntos(jugadores=[]):

    from numpy import amin

    puntos = [jugador.puntos for jugador in jugadores]
    peor_puntuacion = amin(puntos)

    mejor_jugador = None
    mejor_puntuacion = peor_puntuacion

    for jugador in jugadores:
        if jugador.puntos > mejor_puntuacion:
            mejor_jugador = jugador.nombre
            mejor_especie = jugador.especie
            mejor_puntuacion = jugador.puntos

    return mejor_jugador, mejor_puntuacion, mejor_especie

