# -*- coding: utf-8 -*-
import re  # importacion expresion regular

# inicio del archivo que se debe de usar para aplicar la expresion regular
path = "archivo.txt"
codigo = "codigobasico.txt"

# manejo de error para si no se encuentra el archivo
try:
    archivo1 = open(codigo, 'r')
except:
    # por si no se encuentra el archivo
    print("no se encuentra el archivo codigo")
    quit()

muestracodigo = ""

for linea1 in archivo1:
    muestracodigo += linea1


try:
    archivo = open(path, 'r')
except:
    print("El archivo no se encuentra")
    quit()

texto = ""

for linea in archivo:
    texto += linea


#
# para mas informacion de expresion regular se puede buscar en este apartado.7
# link de consulta: https://www.guru99.com/python-regular-expressions-complete-tutorial.html
#
# Variables válidas. Ejemplo: suma, i, cont7, etc.
patronVARIABLES = r'(\b[A-Za-z0-9-_]+\s*[=])+'
# 'r' de espresion regular
# buscar variablas de A-Za-z asi mismo como los numero de 0-9
# '+' diciendole que debe  agregar el otro complento a la primera expresion regular
# asina los resultado a 'resultadoVariables  usnando el patro
resultadoVARIABLES = re.findall(patronVARIABLES, muestracodigo)
# de la expresion anterior que se analiza
# rindall: Re.findall() module is used when you want to iterate over the lines of the file,
# it will return a list of all the matches in a single step. For example, here we have a list of e-mail addresses,
# and we want all the e-mail addresses to be fetched out from the list, we use the re.findall method. It will find
#  all the e-mail addresses from the list.
print("Las variables que estan declaradas son: ",
      resultadoVARIABLES)  # se imprimero los resultados
print("")  # espacio para hacer el salto de linea

# Enteros y decimales. 2.7, 3.1416, 0.2, etc.
# Entero
patronENTERO = r'[+,-]?[0-9]+'
resultadoENTERO = re.findall(patronENTERO, texto)
print("Los numeros enteros del archivo son: ", resultadoENTERO)
print("")

# Decimal
patronDECIMAL = r'[+,-]?[[0-9]*[.]]?[0-9]+'
resultadoDECIMAL = re.findall(patronDECIMAL, texto)

print("Los numeros decimales del archivo son: ", resultadoDECIMAL)
print("")

# Operadores aritméticos (suma, resta, multiplicación, división, etc.)

patronARITMETICO = r'[\d+]+\s*[\+|\-|\*|\/]+\s*[\d+]+'
resultadoARITMETICO = re.findall(patronARITMETICO, texto)
print("Los operadores aritmeticos del archivo son: ", resultadoARITMETICO)
print("")

# Operadores relacionales. (mayor, menor, igual, diferente, etc.)
patronRELACIONAL = r'([A-Za-z0-9|a-z0-9]+\s*[|<|>|!=|<=|>=]=+\s*[A-Za-z0-9|a-z0-9])+'
resultadoRELACIONAL = re.findall(patronRELACIONAL, texto)
print("Los operadores relacionales identificados son: ", resultadoRELACIONAL)
print("")

# Palabras reservadas.
PatronRESERVADAS = r'\b(False|def|if|raise|None|del|import|return|True|elif|in|try|and|else|is|while|as|except|lambda|with|assert|finally|nonlocal|yield|break|for|not|class|from|or|continue|global|pass\s)+|\s[:]+'
resultadoRESERVADAS = re.findall(PatronRESERVADAS, muestracodigo)
print("LAS PALABRAS RESERVADAS SON: ", resultadoRESERVADAS)
print("")
