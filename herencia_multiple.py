class Telefono:
    def __init__(self):

        pass

    def llamar(self):
        print("Llamando...")

    def ocupado(self):
        print('Ocupado...')

class Camara:
    def __init__(self):

        pass

    def fotografia(self):

        print('Tomando fotografia...')

class Reproduccion:

    def __init__(self):

        pass

    def reproduccionmusica(self):

        print('Reproducir musica...')

    def reproduccirunvideo(self):

        print('Reproduciendo un video...')

class Smartphone(Telefono, Camara, Reproduccion):

    def __del__(self):
        print('Telefono apagado...')

movil = Smartphone()
print(movil.fotografia())
