from Abstract.abstract import Expression

class aritmetica(Expression):

    def __init__(self, vizq, vder, tipo, fila, columna):
        self.vizq = vizq
        self.vder = vder
        self.tipo = tipo
        super().__init__(fila, columna)
    
    def operar(self, arbol):
        izqValue = ''
        derValue = ''
        if self.vizq != None:
            izqValue = self.vizq.operar(arbol)
        if self.vder != None:
            derValue = self.vder.operar(arbol)
        
        if self.tipo.operar(arbol) == 'Suma':
            return izqValue + derValue
        elif self.tipo.operar(arbol) == 'Resta':
            return izqValue - derValue
        elif self.tipo.operar(arbol) == 'Multiplicacion':
            return izqValue * derValue
        elif self.tipo.operar(arbol) == 'Division':
            return izqValue / derValue
        elif self.tipo.operar(arbol) == 'Potencia':
            return izqValue ** derValue
        elif self.tipo.operar(arbol) == 'Raiz':
            return izqValue ** (1/derValue)
        elif self.tipo.operar(arbol) == 'Inverso':
            return 1/izqValue
        elif self.tipo.operar(arbol) == 'Mod':
            return izqValue % derValue
        else:
            return None
        
    def getFila(self):
        return super().getFila()
    
    def getColumna(self):
        return super().getColumna()