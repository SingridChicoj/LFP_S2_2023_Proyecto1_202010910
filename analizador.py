from Instrucciones.aritmetica import *
from Instrucciones.trigonometricas import *
from Abstract.Lexema import *
from Abstract.Numero import *


reserved = {
    'ROPERACIONES'      : 'Operaciones',
    'ROPERACION'        : 'Operacion',
    'RVALOR1'           : 'Valor1',
    'RVALOR2'           : 'Valor2',
    'RSUMA'             : 'Suma',
    'RRESTA'            : 'Resta',
    'RMULTIPLICACION'   : 'Multiplicacion',
    'RDIVISION'         : 'Division',
    'RPOTENCIA'         : 'Potencia',
    'RRAIZ'             : 'Raiz',
    'RINVERSO'          : 'Inverso',
    'RSENO'             : 'Seno',
    'RCOSENO'           : 'Coseno',
    'RTANGENTE'         : 'Tangente',
    'RMOD'              : 'Mod',
    'RCONFIGURACIONES'  : 'Configuraciones',
    'RTEXTO'            : 'Texto',
    'RFONDO'            : 'Fondo',
    'RFUENTE'           : 'Fuente',
    'RFORMA'            : 'Forma',
    'COMA'              : ',',
    'PUNTO'             : '.',
    'DOSPUNTOS'         : ':',
    'CORI'              : '[',
    'CORD'              : ']',
    'LLAVEI'            : '{',
    'LLAVED'            : '}',
    }

lexemas = list(reserved.values())
global n_linea
global n_columna
global instrucciones
global lista_lexemas

n_linea = 1
n_columna = 1
lista_lexemas = []
instrucciones = [] 



def instruccion(cadena):
    global n_linea
    global n_columna
    global lista_lexemas
    lexema = ''
    puntero = 0

    while cadena:
        char = cadena[puntero]
        puntero += 1
        
        if char == '\"':
            lexema, cadena = armar_lexema(cadena[puntero:])
            if lexema and cadena:
                n_columna += 1
                #Aqui armo mi lexema como clase
                l = Lexema(lexema, n_linea, n_columna)
                #Aqui agregamos el lexema a la lista de lexemas
                lista_lexemas.append(l)
                n_columna += len(lexema) + 1
                puntero = 0
        elif char.isdigit():
            token, cadena = armar_numero(cadena)
            if token and cadena:
                n_columna += 1
                #Aqui armo mi lexema como clase
                n = Numero(token, n_linea, n_columna)
                #Aqui agregamos el lexema a la lista de lexemas
                lista_lexemas.append(n)
                n_columna += len(str(token)) + 1
                puntero = 0
        elif char == '[' or char == ']':
            #Aqui armo mi lexema como clase
            c = Lexema(char, n_linea, n_columna)
            #Aqui agregamos el lexema a la lista de lexemas
            lista_lexemas.append(c)
            cadena = cadena[1:]
            puntero = 0
            n_columna += 1
        elif char == '\t':
            n_columna += 4
            cadena = cadena[4:]
            puntero = 0
        elif char == '\n':
            cadena = cadena[1:]
            puntero = 0
            n_linea = 1
            n_columna = 1
        else:
            cadena = cadena[1:]
            puntero = 0
            n_columna += 1
    for lexema in lista_lexemas:
        print(lexema)

def armar_lexema(cadena):
    global n_linea
    global n_columna
    global lista_lexemas
    lexema = ''
    puntero = ''

    for char in cadena:
        puntero += char
        if char == '\"':
            return lexema, cadena[len(puntero):]
        else:
            lexema += char
    return None, None

def armar_numero(cadena):
    numero = ''
    puntero = ''
    es_decimal = False

    for char in cadena:
        puntero += char
        if char == '.':
            es_decimal = True
        if char == '"' or char == ' ' or char == '\n' or char == '\t':
            if es_decimal:
                return float(numero), cadena[len(puntero)-1:]
            else:
                return int(numero), cadena[len(puntero)-1:]
        else:
            if char != ',':
                numero += char
        #return numero devolvera el numero como tal
    return None, None

def operar():
    global lista_lexemas
    global instrucciones
    operacion = ''
    n1 = ''
    n2 = ''
    while lista_lexemas:
        lexema = lista_lexemas.pop(0)
        if lexema.operar(None) == 'Operacion':
            operacion = lista_lexemas.pop(0)
        elif lexema.operar(None) == 'Valor1':
            n1 = lista_lexemas.pop(0)
            if n1.operar(None) == '[':
                n1 = operar()
        elif lexema.operar(None) == 'Valor2':
            n2 = lista_lexemas.pop(0)
            if n2.operar(None) == '[':
                n2.operar()
        
        if operacion and n1 and n2:
            return aritmetica(n1, n2, operacion, f'Inicio: {operacion.getFila()}:{operacion.getColumna()}', f'Fin: {n2.getFila()}:{n2.getColumna()}')

        elif operacion and n1 and operacion.operar(None) == ('Seno' or 'Coseno' or 'Tangente'):
            return trigonometricas(n1, operacion, f'Inicio: {operacion.getFila()}:{operacion.getColumna()}', f'Fin: {n1.getFila()}:{n1.getColumna()}')
    return None

def operar_recursivo():
    global instrucciones
    while True:
        operacion = operar()
        if operacion:
            instrucciones.append(operacion)
        else:
            break

    for instruccion in instrucciones:
        print(instruccion.operar(None))

    #return instrucciones
    

entrada = '''{ 
    "Operaciones":[
        {
        "Operacion":"Suma",
        "Valor1":4.5,
        "Valor2":5.32
        }, 
        {
        "Operacion":"Resta",
        "Valor1": 4.5,
        "Valor2":[
            {
                "Operacion":"Potencia",
                "Valor1":10,
                "Valor2":3
            }
            ]
        },
        {
        "Operacion":"Suma",
        "Valor1":[
            {
                "Operacion":"seno",
                "Valor1":90
            }
        ],
        "Valor2":5.32
        },
        {
        "Operacion":"Multiplicacion",
        "Valor1":7,
        "Valor2":3
        },
        {
        "Operacion":"Division",
        "Valor1":15,
        "Valor2":3
        }
    ],
    "configuraciones":[
        {
            "texto":"Operaciones",
            "fondo":"azul",
            "fuente":"blanco",
            "forma":"circulo"
        }
    ]
}'''

entrada2 = '''{
{
"Operacion":"Suma"
"Valor1":4.5
"Valor2":5.32
},
{
"Operacion":"Resta"
"Valor1":4.5
"Valor2": [
"Operacion":"Potencia"
"Valor1":10
"Valor2":3
]},
{
"Operacion":"Suma"
"Valor1":[
"Operacion":"Seno"
"Valor1":90
]
"Valor2":5.32
}
"Texto":"Realizacion de Operaciones"
"Color-Fondo-Nodo":"Amarillo"
"Color-Fuente-Nodo":"Rojo"
"Forma-Nodo":"Circulo"
}'''

instruccion(entrada)
operar_recursivo()
