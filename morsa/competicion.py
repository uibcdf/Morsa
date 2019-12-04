puntos_por_juego={

        'parchís' : {
            'gana' : +2,
            'pierde' : -1
            },

        'ajedrez' : {
            'gana' : +3,
            'pierde' : -2
            },

        'dominó' : {
            'gana' : +2,
            'pierde' : 0
            },

        'tres en raya' : {
            'gana' : +1,
            'pierde' : -1
            },

        }


def jugar(juego=None, jugador1=None, jugador2=None):

    for jugador in [jugador1, jugador2]:
        if juego not in jugador.habilidades:
            print("{} no sabe jugar {}".format(jugador.nombre, juego))
            pass

    acierto_jugador1 = random()*jugador1.suerte*jugador1.habilidad[juego]
    acierto_jugador2 = random()*jugador2.suerte*jugador2.habilidad[juego]

    resultado = None

    if acierto_jugador1>acierto_jugador2:

        jugador1.puntos += puntos_por_juego[juego]['gana']
        jugador2.puntos += puntos_por_juego[juego]['pierde']

        resultado = "Ganó {}".format(jugador1.nombre)

    elif acierto_jugador2<acierto_jugador1:

        jugador2.puntos += puntos_por_juego[juego]['gana']
        jugador1.puntos += puntos_por_juego[juego]['pierde']

        resultado = "Ganó {}".format(jugador2.nombre)

    else:

        resultado = "Ninguno gana"

def quien_tiene_mas_puntos(jugadores=[]):

    from numpy import minimum

    puntuaciones = [jugador.puntuacion for jugador in jugadores]
    peor_puntuacion = minimum(puntuaciones)

    mejor_jugador = None
    mejor_puntuacion = peor_puntuacion

    for jugador in jugadores:
        if jugador.puntuacion > mejor_puntuacion:
            mejor_jugador = jugador.nombre
            mejor_puntuacion = jugador.puntuacion

    return mejor_jugador, mejor_puntuacion

def consulta_puntos_por_juego(juego=None):

    return puntos_por_juego[juego]

