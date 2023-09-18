from Abstract.abstract import Expression
from math import *

class trigonometricas(Expression):

    def __init__(self, vizq, tipo, fila, columna):
        super().__init__(fila, columna)
        self.vizq = vizq
        self.tipo = tipo

    def operar(self, arbol):
        izqValue = ''
        if self.vizq != None:
            izqValue = self.vizq.operar(arbol)
        
        if self.tipo == 'Seno':
            return sin(izqValue)
        elif self.tipo == 'Coseno':
            return cos(izqValue)
        elif self.tipo == 'Tangente':
            return tan(izqValue)
        else:
            return None
        
    def getFila(self):
        return super().getFila()
    
    def getColumna(self):
        return super().getColumna()