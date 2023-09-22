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
        
        if self.tipo.operar(arbol) == 'Suma' or self.tipo.operar(arbol) == 'suma':
            return izqValue + derValue
        elif self.tipo.operar(arbol) == 'Resta' or self.tipo.operar(arbol) == 'resta':
            return izqValue - derValue
        elif self.tipo.operar(arbol) == 'Multiplicacion' or self.tipo.operar(arbol) == 'multiplicacion':
            return izqValue * derValue
        elif self.tipo.operar(arbol) == 'Division' or self.tipo.operar(arbol) == 'division':
            return izqValue / derValue
        elif self.tipo.operar(arbol) == 'Potencia' or self.tipo.operar(arbol) == 'potencia':
            return izqValue ** derValue
        elif self.tipo.operar(arbol) == 'Raiz' or self.tipo.operar(arbol) == 'raiz':
            return izqValue ** (1 / derValue)
        #elif self.tipo.operar(arbol) == 'Inverso' or self.tipo.operar(arbol) == 'inverso':
        #    return 1 / izqValue 
        elif self.tipo.operar(arbol) == 'Mod' or self.tipo.operar(arbol) == 'mod':
            return izqValue % derValue
        else:
            return None
        
    def getFila(self):
        return super().getFila()
    
    def getColumna(self):
        return super().getColumna()