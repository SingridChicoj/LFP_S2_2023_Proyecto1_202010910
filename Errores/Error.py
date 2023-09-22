from Abstract.abstract import Expression

class Error(Expression):
    def __init__(self, lexema, fila, columna):
        self.lexema = lexema
        super().__init__(fila, columna)
    
    def operar(self, no):
        num = f'\t\t"No.": {no}\n'
        desc = '\t\t "Descripcion": {'
        lex = f'\t\t\t"Lexema": {self.lexema}\n'
        tipo = f'\t\t\t"Tipo": Error Lexico\n'
        fil = f'\t\t\t"Fila": {self.fila}\n'
        colum = f'\t\t\t"Columna": {self.columna}\n'
        fin = '\t\t}\n'
        return '\t{\n' + num + desc + lex + tipo + fil + colum + fin + '\t}'
    
    
    def getFila(self):
        return super().getFila()
    
    def getColumna(self):
        return super().getColumna()