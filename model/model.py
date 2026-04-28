from database.corso_DAO import get_all_corsi
from database.studente_DAO import get_studenti_by_corso

# Nota. Il Model non sa le cose… E' un semplice passacarte! Chiede al DAO!
#       Il Model è l'unico che parla col Controller e con il DAO.

class Model:
    def __init__(self):
        pass


    def get_all_corsi(self):
        return get_all_corsi()


    def get_studenti_by_corso(self, codins):
        return get_studenti_by_corso(codins)