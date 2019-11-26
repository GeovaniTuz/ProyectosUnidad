import re

path = "archivo.txt"

try:
	archivo = open(path,'r')
except:
	print("El archivo no se encuentra")
	quit()

texto = ""
 
for linea in archivo:
	texto += linea

#	Sentencia de asignación. Ejemplo: suma = 0, factorial = 1, vidas = cont, etc.
patronASIGNACION = r'([a-z0-9]+\s*[=]+\s*[a-z0-9+]+)'
resultadoASIGNACION = re.findall(patronASIGNACION,texto)
print("\n Las sentencias de asignacion son:\n", resultadoASIGNACION)

#	Operaciones aritméticas básicas. Ejemplo: suma = 2.7 + 3, cont = cont + 1, etc.
#([a-z0-9-_]+\s*[=]+\s*[a-z0-9-_]+\s*[+,-,*,/,%]+\s*[a-z0-9-_]+)
patronARITMETICO = r'([A-Za-z0-9-_]+\s*[=]+\s*[A-Za-z0-9-_|0-9.0-9]+\s*[\+,\-,\*,\/,\%]+\s*[A-Za-z0-9-_|0-9.0-9]+)'
resultadoARITMETICO = re.findall(patronARITMETICO,texto)
print("\n Las operaciones aritmeticas son:\n", resultadoARITMETICO)

#	Expresiones booleanas básicas. Ejemplo: edad >= 5, suma != 0, etc.
patronBOOLEANO = r'([A-Za-z0-9]+\s*[|<|>|!|<=|>=]=+\s*[A-Za-z0-9])'
resultadoBOOLEANO = re.findall(patronBOOLEANO, texto)
print("\nEn las operaciones booleanas son:\n", resultadoBOOLEANO)

#	Formulas más complejas del tipo c = a op ( b op d)
#([A-Za-z0-9-_]=+\s*[A-Za-z0-9-_]+\s*[<,>,!,<=,>=,*,+,/,-]=+\s*([A-Za-z0-9-_]+\s*[<,>,!,<=,>=,*,+,/,-]+\s*[A-Za-z0-9-_]+\s*)+)
patronCOMPLEJO = r'([A-Za-z0-9]+\s*=+\s*[A-Za-z0-9]+\s*[|<|>|!|<=|>=|\+|\-\*\/]\s*[(]+\s*[A-Za-z0-9]+\s*[|<|>|!|<=|>=|\+|\-\*\/]+\s*[A-Za-z0-9]+\s*[)])'
resultadoCOMPLEJO = re.findall(patronCOMPLEJO,texto)
print("\n ENTRADA DE CUALQUIER OPERADOR, formula compleja:\n", resultadoCOMPLEJO)

#	El encabezado de estructura de control. if, while, for, etc.
patronFOR = r'(for+\s*[A-Za-z0-9-_]+\s*[in]+\s*[A-Za-z0-9-_]+\s*:)'
patronWHILE = r'(while+\s*[A-Za-z0-9-_]+\s*[|<|>|!|<=|>=]=+\s*[A-Za-z0-9-_]+\s*:)'
patronIF = r'(if+\s*[A-Za-z0-9-_]+\s*[|<|>|!|<=|>=]=+\s*[A-Za-z0-9-_]+\s*:)'
patronTRY = r'(try:+\s*[A-Za-z0-9-_]+\s*except+\s*[A-Za-z0-9-_]+\s*:)'
resultadoFOR = re.findall(patronFOR, texto)
resultadoWHILE = re.findall(patronWHILE,texto)
resultadoIF = re.findall(patronIF,texto)
resultadoTRY = re.findall(patronTRY,texto)
print("\n Las operaciones de encabezado FOR son:\n", resultadoFOR)
print("\n Las operaciones de encabezado WHILE son:\n", resultadoWHILE)
print("\n Las operaciones de encabezado IF son:\n", resultadoIF)
print("\n Las operaciones de encabezado TRY son:\n", resultadoTRY)
