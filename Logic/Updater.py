from musixmatch import Musixmatch

from .application_data import *


class Updater:
    """
    actual client: estabilish the connection and retrieve the data
    """

    def __init__(self):
        self.musixmatch = Musixmatch(api_key)

# nota: la ricerca rende un dizionario innestato di tipo json
# per accedere ai risultati:
# result['message']['body']['track_list'], è una lista
# ogni di elemento è un dizionario con un solo elemento: track
# quindi in genere: result['message']['body']['track_list'][X]['track'] è un risultato, X € N
