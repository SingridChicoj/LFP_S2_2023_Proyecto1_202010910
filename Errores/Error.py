from Abstract.abstract import Expression

class Error(Expression):
    def __init__(self, lexema, fila, columna):
        self.lexema = lexema
        super().__init__(fila, columna)
    
    def operar(self, no):
        num = f'\t\t\t"No.": {no}\n'
        desc = '\t\t\t"Descripcion": {\n'
        lex = f'\t\t\t\t"Lexema": {self.lexema}\n'
        tipo = f'\t\t\t\t"Tipo": Error Lexico\n'
        colum = f'\t\t\t\t"Columna": {self.columna}\n'
        fil = f'\t\t\t\t"Fila": {self.fila}\n'
        fin = '\t\t\t}\n'

        return '\t\t{\n' + num + desc + lex + tipo + colum + fil  + fin + '\t\t}\n'
    
    
    def getFila(self):
        return super().getFila()
    
    def getColumna(self):
        return super().getColumna()