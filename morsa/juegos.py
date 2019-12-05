_dict_puntos_por_juego={

        'parchís' : {
            'gana' : +1,
            'pierde' : -1
            },

        'ajedrez' : {
            'gana' : +2,
            'pierde' : -1
            },

        'dominó' : {
            'gana' : +1,
            'pierde' : 0
            },

        'tres en raya' : {
            'gana' : +1,
            'pierde' : -2
            },

        }

_lista_de_juegos=list(_dict_puntos_por_juego.keys())

def _reparte_puntos(juego=None, resultado=None):

    return _dict_puntos_por_juego[juego][resultado]

def consulta_lista_de_juegos():

    return _lista_de_juegos

def consulta_puntos_por_juego(juego=None):

    return _dict_puntos_por_juego[juego]

def asignar_puntos_por_juego(juego=None, gana=0, pierde=0):

    _dict_puntos_por_juego[juego]['gana'] = gana
    _dict_puntos_por_juego[juego]['pierde'] = pierde

def generador_aleatorio_de_juegos():

    from numpy.random import choice

    return choice(_lista_de_juegos)

