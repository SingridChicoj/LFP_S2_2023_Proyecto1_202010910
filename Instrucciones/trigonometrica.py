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
        
        if self.tipo.operar(arbol) == 'Inverso' or self.tipo.operar(arbol) == 'inverso':
            resultados =  1 / izqValue
            aprox = round(resultados, 3)
            return aprox
        elif self.tipo.operar(arbol) == 'Seno' or self.tipo.operar(arbol) == 'seno':
            grados = izqValue
            gradosConver = math.radians(grados)
            aprox = round(gradosConver, 3)
            return sin(aprox)
        elif self.tipo.operar(arbol) == 'Coseno' or self.tipo.operar(arbol) == 'coseno':
            grados = izqValue
            gradosConver = math.radians(grados)
            aprox = round(gradosConver, 3)
            return cos(aprox)
        elif self.tipo.operar(arbol) == 'Tangente' or self.tipo.operar(arbol) == 'tangente':
            grados = izqValue
            gradosConver = math.radians(grados)
            aprox = round(gradosConver, 3)
            return tan(aprox)
        
        else:
            return None
        
    def getFila(self):
        return super().getFila()
    
    def getColumna(self):
        return super().getColumna()