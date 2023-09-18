from Abstract.abstract import Expression
from math import *

class trigonometrica(Expression):

    def __init__(self, vizq, tipo, fila, columna):
        self.vizq = vizq
        self.tipo = tipo
        super().__init__(fila, columna)

    def operar(self, arbol):
        izqValue = ''
        if self.vizq != None:
            izqValue = self.vizq.operar(arbol)
        
        if self.tipo.operar(arbol) == 'Seno' or self.tipo.operar(arbol) == 'seno':
            return sin(izqValue)
        elif self.tipo.operar(arbol) == 'Coseno' or self.tipo.operar(arbol) == 'coseno':
            return cos(izqValue)
        elif self.tipo.operar(arbol) == 'Tangente' or self.tipo.operar(arbol) == 'tangente':
            return tan(izqValue)
        else:
            return None
        
    def getFila(self):
        return super().getFila()
    
    def getColumna(self):
        return super().getColumna()