# -*- coding: utf-8 -*-
import ply.yacc as yacc
from analizador_lexico import tokens
#from analizador_lexico import analizador
import ply.lex as lex  # inportacion de librerias necesarias
import re

# resultado del analisis
resultado_gramatica = []

precedence = (
    ('right', 'ASIGNAR'),
    ('left', 'SUMA', 'RESTA'),
    ('left', 'MULT', 'DIV'),
    ('right', 'UMINUS',),
)
nombres = {}

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
# sintactico de expresiones logicas


def p_expresion_logicas(t):
    '''
    expresion   :  expresion MENORQUE expresion 
                |  expresion MAYORQUE expresion 
                |  expresion MENORIGUAL expresion 
                |   expresion MAYORIGUAL expresion 
                |   expresion IGUAL expresion 
                |   expresion DISTINTO expresion
                |  PARIZQ expresion PARDER MENORQUE PARIZQ expresion PARDER
                |  PARIZQ expresion PARDER MAYORQUE PARIZQ expresion PARDER
                |  PARIZQ expresion PARDER MENORIGUAL PARIZQ expresion PARDER 
                |  PARIZQ  expresion PARDER MAYORIGUAL PARIZQ expresion PARDER
                |  PARIZQ  expresion PARDER IGUAL PARIZQ expresion PARDER
                |  PARIZQ  expresion PARDER DISTINTO PARIZQ expresion PARDER
    '''
    if t[2] == "<":
        t[0] = t[1] < t[3]
    elif t[2] == ">":
        t[0] = t[1] > t[3]
    elif t[2] == "<=":
        t[0] = t[1] <= t[3]
    elif t[2] == ">=":
        t[0] = t[1] >= t[3]
    elif t[2] == "==":
        t[0] = t[1] is t[3]
    elif t[2] == "!=":
        t[0] = t[1] != t[3]
    elif t[3] == "<":
        t[0] = t[2] < t[4]
    elif t[2] == ">":
        t[0] = t[2] > t[4]
    elif t[3] == "<=":
        t[0] = t[2] <= t[4]
    elif t[3] == ">=":
        t[0] = t[2] >= t[4]
    elif t[3] == "==":
        t[0] = t[2] is t[4]
    elif t[3] == "!=":
        t[0] = t[2] != t[4]

    # print('logica ',[x for x in t])

# gramatica de expresiones booleanadas


def p_expresion_booleana(t):
    '''
    expresion   :   expresion AND expresion 
                |   expresion OR expresion 
                |   expresion NOT expresion 
                |  PARIZQ expresion AND expresion PARDER
                |  PARIZQ expresion OR expresion PARDER
                |  PARIZQ expresion NOT expresion PARDER
    '''
    if t[2] == "&&":
        t[0] = t[1] and t[3]
    elif t[2] == "||":
        t[0] = t[1] or t[3]
    elif t[2] == "!":
        t[0] = t[1] is not t[3]
    elif t[3] == "&&":
        t[0] = t[2] and t[4]
    elif t[3] == "||":
        t[0] = t[2] or t[4]
    elif t[3] == "!":
        t[0] = t[2] is not t[4]

def p_expresion_numero(t):
    'expresion : ENTERO'
    t[0] = t[1]

def p_expresion_decimal(t):
    'expresion : DECIMAL'
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
#([\$?][a-z0-9|0-9.0-9]+\s*[\+|\-|\*|\/]+\s*[\$]?[a-z0-9-_|0-9.0-9]+)
#LOS DOS FUNCIONAN PERO DETALLES ES --> SEPARACION DE LETRAS Y NUMEROS
patronbasico = r'[\$?][a-z|0-9.0-9]+\s*[\+|\-|\*|\/]+\s*[\$]?[a-z|0-9.0-9]+'
patronBLetra = r'[\$?][a-z]+\s*[\+|\-|\*|\/]+\s*[\$]?[a-z]+'
patronBNum = r'[0-9.0-9]+\s*[\+|\-|\*|\/]+\s*[0-9.0-9]+'
#funciona pero tiene detalles --> SEPARACION DE NUMEROS CON LETRAS
patronavanzado = r'[\$?][a-z|0-9.0-9\s*\+|\-|\*|\/\s*\$?a-z|0-9.0-9]+\s*[(?][\$?a-z|0-9.0-9\s*\+|\-|\*|\/\s*\$?a-z|0-9.0-9]+[)?]'
patronALetra = r'[\$?][a-z\s*\+|\-|\*|\/\s*\$?a-z|]+\s*[(?][\$?a-z\s*\+|\-|\*|\/\s*\$?a-z]+[)?]'
patronANum = r'[0-9.0-9\s*\+|\-|\*|\/\s*0-9.0-9]+\s*[(?][0-9.0-9\s*\+|\-|\*|\/\s*0-9.0-9]+[)?]'
patrooo  = r'\d+\.\d+'
#se analiza con el patron
resultadobasico = re.findall(patronbasico, text)
resultadoBLetra = re.findall(patronBLetra, text)
resultadoBNum = re.findall(patronBNum, text)
resultadoavanzado = re.findall(patronavanzado,text)
resultadoALetra = re.findall(patronALetra, text)
resultadoANum = re.findall(patronANum, text)
resultado = re.findall(patrooo, text)


#print ("avanzado", text)
#print(''.join(list(map(''.join, text))))

# se imprime el patron 
print('-------------------------------------------------')
print('------------Patron encontrado--------------------')
print('-------------------------------------------------')
print('')
print("Avanzado", resultadoavanzado, resultadoALetra, resultadoANum)
print('')
print("Basico", resultadobasico, resultadoBLetra, resultadoBNum)
print('')
print(resultado)

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
