import random


class Dado:

    #método constructor de la clase
    def __init__(self):
        self.valor=0


    def girar(self):
        self.valor=random.randint(1,6)


    def getValor(self):
        return self.valor




