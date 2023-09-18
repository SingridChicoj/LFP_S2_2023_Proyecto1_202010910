from Abstract.abstract import Expression

class Numero(Expression):
    
    def __init__(self, fila, columna, valor):
        super().__init__(fila, columna)
        self.valor = valor
    
    def operar(self, arbol):
        return self.valor
    
    def getFila(self):
        return super().getFila()
    
    def getColumna(self):
        return super().getColumna()
