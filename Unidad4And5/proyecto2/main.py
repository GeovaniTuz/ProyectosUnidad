# -*- coding: utf-8 -*-
import ply.yacc as yacc
from analizador_lexico import tokens
from analizador_lexico import analizador
import ply.lex as lex  # inportacion de librerias necesarias
import re

# resultado del analisis
resultado_gramatica = []

# se declara que se debe de hacer
precedence = (
    ('right', 'ASIGNAR'),
    ('left', 'SUMA', 'RESTA'),
    ('left', 'MULT', 'DIV'),
    ('right', 'UMINUS'),
)
nombres = {}


# def p_declaracion_decimall(p):
#    'declaracion : DECIMAL'
#    print("decimal")

# se definde como debe de funcionar
def p_declaracion_asignar(t):
    'declaracion : VARIABLE ASIGNAR expresion PUNTOYCOMA '
    nombres[t[1]] = t[3]

# def p_declaracion_asignar(t):
 #   'declaracion : IDENTIFICADOR ASIGNAR expresion PUNTOCOMA'
  #  nombres[t[1]] = t[3]


# aqui la idea de como hacer la primera declaracion
def p_declaracion_taginicio(t):
    'declaracion : TAGINICIO ASIGNAR expresion TAG_FINAL'
    inicio[t[1]] = t[3]
 #   print("no cumplio")

# def p_declaracion_taginicio(p):
 #   'declaracion : TAGINICIO'
  #  print("Inicio de sintaxis PHP")


# def p_declaraxion_tag_final(p):
 #   'declaracion : TAG_FINAL'
  #  print("Final de sintaxis")


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


# def p_expresion_cadena(t):
   # 'expresion : COMDOB expresion COMDOB'
   # t[0] = t[2]


def p_expresion_nombre(t):
    'expresion : VARIABLE'
    try:
        t[0] = nombres[t[1]]
    except LookupError:
        print("---------------------------------------------")
        print("SINTAXIS ERROR ")
        print("--------------------------------------------")
        print("")
        print("VERIFICAR: ", t[1])
        print("¿verificar si se definio o asigno un valor(en caso de operacion arimetica)?")
        t[0] = 0
        print("---------------------------------------------")


def p_error(t):
    global resultado_gramatica
    if t:
        # type: es para el tipo
        # value:valor que hace que falle
        # lineno: es para que linea pertenece
        # lexpos: para la posicion donde se encuentra
        resultado = "Error sintactico de tipo {} en el valor {}".format(
            str(t.type), str(t.value))
       # print("SINTAXIS ERROR")
       # print(resultado)
    else:
        resultado = "Error sintactico {}".format(t)
       # print(resultado)
    resultado_gramatica.append(resultado)


# instanciamos el analizador sistactico
parser = yacc.yacc()


def prueba_sintactica(data):
    global resultado_gramatica
   # resultado_gramatica.clear()

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

# agregamos un pratron
patronsin = r'[a-zA-Z]'
# se analiza con el patron
resultadoCOMPLEJO = re.findall(patronsin, text)


#print ("avanzado", text)
#print(''.join(list(map(''.join, text))))

# se imprime el patron
# print('-------------------------------------------------')
#print('------------Patron encontrado--------------------')
# print('-------------------------------------------------')
# print('')
#print("Avanzado", resultadoCOMPLEJO)
# print('')
#print("Basico", resultadoCOMPLEJO)
# print('')

# aqui se imprime los resultados de la operacion
# print('-------------------------------------------------')
#print('-----contenido del archivo index.php-------------')
# print('-------------------------------------------------')
# print('')
#print(''.join(list(map(''.join, text))))
# print('')

#print('-------------------------------------------------')
#print('----------resultado de la gramatica-------------')
#print('-------------------------------------------------')

#print("es correcto")

print('\n'.join(list(map(''.join, resultado_gramatica))))
#print("SINTAXIS CORRECTA")
