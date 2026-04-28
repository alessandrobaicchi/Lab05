from dataclasses import dataclass

# class Corso:
#     def __init__(self):
#         pass


@dataclass
class Corso:
    codins: str
    crediti: int
    nome: str
    pd: int

    def __eq__(self, other):
        return self.codins == other.codins


    def __hash__(self):
        return hash(self.codins)


    def __str__(self):
        return f'{self.nome} ({self.codins})'
