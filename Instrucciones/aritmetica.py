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
            resultados = izqValue + derValue
            aprox = round(resultados, 3)
            return aprox
        elif self.tipo.operar(arbol) == 'Resta' or self.tipo.operar(arbol) == 'resta':
            resultados = izqValue - derValue
            aprox = round(resultados, 3)
            return aprox
        elif self.tipo.operar(arbol) == 'Multiplicacion' or self.tipo.operar(arbol) == 'multiplicacion':
            resultados = izqValue * derValue
            aprox = round(resultados, 3)
            return aprox
        elif self.tipo.operar(arbol) == 'Division' or self.tipo.operar(arbol) == 'division':
            resultados = izqValue / derValue
            aprox = round(resultados, 3)
            return aprox
        elif self.tipo.operar(arbol) == 'Potencia' or self.tipo.operar(arbol) == 'potencia':
            resultados = izqValue ** derValue
            aprox = round(resultados, 3)
            return aprox
        elif self.tipo.operar(arbol) == 'Raiz' or self.tipo.operar(arbol) == 'raiz':
            resultados = izqValue ** (1 / derValue)
            aprox = round(resultados, 3)
            return aprox
        #elif self.tipo.operar(arbol) == 'Inverso' or self.tipo.operar(arbol) == 'inverso':
            #resultados = izqValue + derValue
            #round(resultados, 2)
            #return resultados
            #return 1 / izqValue 
        elif self.tipo.operar(arbol) == 'Mod' or self.tipo.operar(arbol) == 'mod':
            resultados = izqValue % derValue
            aprox = round(resultados, 3)
            return aprox
        else:
            return None
        
    def getFila(self):
        return super().getFila()
    
    def getColumna(self):
        return super().getColumna()