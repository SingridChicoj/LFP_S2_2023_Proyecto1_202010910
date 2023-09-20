from Abstract.abstract import Expression
from math import *
import math

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
            grados = izqValue
            gradosConver = math.radians(grados)
            return sin(gradosConver)
        elif self.tipo.operar(arbol) == 'Coseno' or self.tipo.operar(arbol) == 'coseno':
            grados = izqValue
            gradosConver = math.radians(grados)
            return cos(gradosConver)
        elif self.tipo.operar(arbol) == 'Tangente' or self.tipo.operar(arbol) == 'tangente':
            grados = izqValue
            gradosConver = math.radians(grados)
            return tan(gradosConver)
        else:
            return None
        
    def getFila(self):
        return super().getFila()
    
    def getColumna(self):
        return super().getColumna()