#numeros enteros r"[+,-]?[0-9]+"
#numero decimal [+-]?([0-9]*[.])?[0-9]+
#operaciones aritmeticas (-)?N+(.N+)? (‘+’|’-‘|’*’|’/’) (-)?N+(.N+)? ((‘+’|’-‘|’*’|’/’) (-)?N+(.N+)?)*
#operadores relacionales [A-Za-z0-9]\s+(==|<|>|!=|<=|>=)\s+[A-Za-z0-9]|[A-Za-z0-9]\S+(==|<|>|!=|<=|>=)\S+[A-Za-z0-9]
# PALABRAS RESERVADAS
#(False|def|if|raise|None|del|import|return|True|elif|in|try|and|else|is|while|as|except|lambda|with|assert|finally|nonlocal|yield|break|for|not|class|from|or|continue|global|pass\b\w\S)+
#['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

import re

path = "archivo.txt"
codigo = "codigobasico.txt"

try:
	archivo1 = open(codigo,'r')
except:
	print("no se encuentra el archivo codigo")
	quit()

muestracodigo = ""

for linea1 in archivo1:
	muestracodigo += linea1



try:
	archivo = open(path,'r')
except:
	print("El archivo no se encuentra")
	quit()

texto = ""

for linea in archivo:
	texto += linea




#	Variables válidas. Ejemplo: suma, i, cont7, etc.
patronVARIABLES = r'(\b[A-Za-z0-9-_]+\s*[=])+'
resultadoVARIABLES = re.findall(patronVARIABLES,muestracodigo)
print("\n Las variables que estan declaradas son:\n", resultadoVARIABLES)

#	Enteros y decimales. 2.7, 3.1416, 0.2, etc.
patronENTERO = r'[+,-]?[0-9]+'
patronDECIMAL = r'[+,-]?[[0-9]*[.]]?[0-9]+'
resultadoENTERO = re.findall(patronENTERO,texto)
resultadoDECIMAL = re.findall(patronDECIMAL,texto)
print("\n Los numeros enteros del archivo son:\n", resultadoENTERO)
print("\nLos numeros decimales del archivo son:\n", resultadoDECIMAL)

#	Operadores aritméticos (suma, resta, multiplicación, división, etc.)

patronARITMETICO = r'[\d+]+?[\s+,\-,*,/]+?[\d+]+'
resultadoARITMETICO = re.findall(patronARITMETICO,texto)
print("\nLos operadores aritmeticos del archivo son:\n", resultadoARITMETICO)

#	Operadores relacionales. (mayor, menor, igual, diferente, etc.)
patronRELACIONAL = r'([A-Za-z0-9|a-z0-9]+\s*[|<|>|!=|<=|>=]=+\s*[A-Za-z0-9|a-z0-9])+'
resultadoRELACIONAL = re.findall(patronRELACIONAL, texto)
print("\n Los operadores relacionales identificados son:\n", resultadoRELACIONAL)

#	Palabras reservadas.
PatronRESERVADAS = r'\b(False|def|if|raise|None|del|import|return|True|elif|in|try|and|else|is|while|as|except|lambda|with|assert|finally|nonlocal|yield|break|for|not|class|from|or|continue|global|pass\s)+|\s[:]+'
resultadoRESERVADAS = re.findall(PatronRESERVADAS,muestracodigo)
print("\nLAS PALABRAS RESERVADAS SON:\n", resultadoRESERVADAS)