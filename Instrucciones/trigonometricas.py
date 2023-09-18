from Abstract.abstract import Expression
from math import *

class trigonometricas(Expression):

    def __init__(self, vizq, tipo, fila, columna):
        self.vizq = vizq
        self.tipo = tipo
        super().__init__(fila, columna)

    def operar(self, arbol):
        izqValue = ''
        if self.vizq != None:
            izqValue = self.vizq.operar(arbol)
        
        if self.tipo.operar(arbol) == 'Seno':
            return sin(izqValue)
        elif self.tipo.operar(arbol) == 'Coseno':
            return cos(izqValue)
        elif self.tipo.operar(arbol) == 'Tangente':
            return tan(izqValue)
        else:
            return None
        
    def getFila(self):
        return super().getFila()
    
    def getColumna(self):
        return super().getColumna()