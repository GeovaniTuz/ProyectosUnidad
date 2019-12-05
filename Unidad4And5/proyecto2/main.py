# -*- coding: utf-8 -*-
import ply.yacc as yacc
from analizador_lexico import tokens
from analizador_lexico import analizador
import ply.lex as lex  # inportacion de librerias necesarias
import re

# resultado del analisis
resultado_gramatica = []

precedence = (
    ('right', 'ASIGNAR'),
    ('left', 'SUMA', 'RESTA'),
    ('left', 'MULT', 'DIV'),
    ('right', 'UMINUS'),
)
nombres = {}

def p_declaracion_decimal(t):
    'declaracion : DECIMAL'
    print("decimal")

def p_declaracion_asignar(t):
    'declaracion : IDENTIFICADOR ASIGNAR expresion PUNTOCOMA'
    nombres[t[1]] = t[3]

def p_declaraxion_taginicio(p):
    'declaracion : TAGINICIO'
    print("Inicio de sintaxis PHP")

def p_declaraxion_tag_final(p):
    'declaracion : TAG_FINAL'
    print("Final de sintaxis")

def p_declaracion_expr(t):
    'declaracion : expresion'
    # print("Resultado: " + str(t[1]))
    t[0] = t[1]


def p_expresion_operaciones(t):
    '''
    expresion  :   expresion SUMA expresion
                |   expresion RESTA expresion
                |   expresion MULT expresion
                |   expresion DIV expresion
                |   expresion POTENCIA expresion
                |   expresion MODULO expresion

    '''
    if t[2] == '+':
        t[0] = t[1] + t[3]
    elif t[2] == '-':
        t[0] = t[1] - t[3]
    elif t[2] == '*':
        t[0] = t[1] * t[3]
    elif t[2] == '/':
        t[0] = t[1] / t[3]
    elif t[2] == '%':
        t[0] = t[1] % t[3]
    elif t[2] == '**':
        i = t[3]
        t[0] = t[1]
        while i > 1:
            t[0] *= t[1]
            i -= 1


def p_expresion_uminus(t):
    'expresion : RESTA expresion %prec UMINUS'
    t[0] = -t[2]


def p_expresion_grupo(t):
    '''
    expresion  : PARIZQ expresion PARDER
                | LLAIZQ expresion LLADER
                | CORIZQ expresion CORDER
    '''
    t[0] = t[2]
# sintactico de expresiones logicas


def p_expresion_numero(t):
    'expresion : ENTERO'
    t[0] = t[1]

def p_expresion_cadena(t):
    'expresion : COMDOB expresion COMDOB'
    t[0] = t[2]

def p_expresion_nombre(t):
    'expresion : IDENTIFICADOR'
    try:
        t[0] = nombres[t[1]]
    except LookupError:
        print("Nombre desconocido ", t[1])
        t[0] = 0


def p_error(t):
    global resultado_gramatica
    if t:
        #type: es para el tipo
        #value:valor que hace que falle
        #lineno: es para que linea pertenece
        #lexpos: para la posicion donde se encuentra
        resultado = "Error sintactico de tipo {} en el valor {} de linea {}".format(
            str(t.type), str(t.value), str(t.lineno))
        print(resultado)
    else:
        resultado = "Error sintactico {}".format(t)
        print(resultado)
    resultado_gramatica.append(resultado)


# instanciamos el analizador sistactico
parser = yacc.yacc()


def prueba_sintactica(data):
    global resultado_gramatica
   # resultado_gramatica.clear()

    print('-------------------------------------------------')
    print('-----Resultado del patron encontrado-------------')
    print('-------------------------------------------------')
    print('')
    for item in data.splitlines():
        if item:
            gram = parser.parse(item)
            if gram:
                resultado_gramatica.append(str(gram))
        else:
            print("")

    #print("result: ", resultado_gramatica)
    return resultado_gramatica
path = "index.php"

try:
    archivo = open(path, 'r')
except:
    print("el archivo no se encontro")
    quit()

text = ""
for linea in archivo:
   text += linea

prueba_sintactica(text)

## agregamos un pratron
#ESTA TOMANDO LOS VALORES QUE ENCUENTRE COMO UNA EXPRESION BASICA DE DOS NUMEROS REALIZANDO UNA OPERACION
#[\$?][a-z0-9|0-9.0-9]+\s*[\+|\-|\*|\/]+\s*[\$?][a-z0-9-_|0-9.0-9]+
#TOMA
patronbasico = r'[\$]?[a-z0-9|0-9.0-9]+\s*[\+|\-|\*|\/]+\s*[\$]?[a-z0-9-_|0-9.0-9]+'
#$a - $b * ( $c + $d)
#reconoce las variables y numeros pero no parentesis --> ([\$?]+[a-z]+|[0-9]+\[\+|\-|\*|\/]+)
patronavanzado = r'[\$]?[a-z|0-9.0-9]+\[\+|\-|\*|\/]+[(][\$]?[a-z|0-9.0-9]+\[\+|\-|\*|\/]+[\$]?[a-z|0-9.0-9][)]+'
#se analiza con el patron
resultadobasico = re.findall(patronbasico, text)
resultadoavanzado = re.findall(patronavanzado,text)


#print ("avanzado", text)
#print(''.join(list(map(''.join, text))))

# se imprime el patron 
print('-------------------------------------------------')
print('------------Patron encontrado--------------------')
print('-------------------------------------------------')
print('')
print("Avanzado", resultadoavanzado)
print('')
print("Basico", resultadobasico)
print('')

# aqui se imprime los resultados de la operacion
print('-------------------------------------------------')
print('-----contenido del archivo index.php-------------')
print('-------------------------------------------------')
print('')
print(''.join(list(map(''.join, text))))
print('')

print('-------------------------------------------------')
print('--------resultados de la operaciones-------------')
print('-------------------------------------------------')
print('\n'.join(list(map(''.join, resultado_gramatica))))


#1.-agregar patrones para saber si es una operacion basica o avanzada

#2.-falta: la estrutura de control {if}{else}

#3.-solo falta resta

#solo faltan estos tres puntos, agaren uno para terminar
