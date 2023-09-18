from Abstract.abstract import Expression

class aritmetica(Expression):

    def __init__(self, vizq, vder, tipo, fila, columna):
        super().__init__(fila, columna)
        self.vizq = vizq
        self.vder = vder
        self.tipo = tipo
    
    def operar(self, arbol):
        izqValue = ''
        derValue = ''
        if self.vizq != None:
            izqValue = self.vizq.operar(arbol)
        if self.vder != None:
            derValue = self.vder.operar(arbol)
        
        if self.tipo == 'Suma':
            return izqValue + derValue
        elif self.tipo == 'Resta':
            return izqValue - derValue
        elif self.tipo == 'Multiplicacion':
            return izqValue * derValue
        elif self.tipo == 'Division':
            return izqValue / derValue
        elif self.tipo == 'Potencia':
            return izqValue ** derValue
        elif self.tipo == 'Raiz':
            return izqValue ** (1/derValue)
        elif self.tipo == 'Inverso':
            return 1/izqValue
        elif self.tipo == 'Mod':
            return izqValue % derValue
        else:
            return None
        
    def getFila(self):
        return super().getFila()
    
    def getColumna(self):
        return super().getColumna()