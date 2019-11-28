# PythonU4and5

#checar detalles
#hacer tokens de inicio(<php>) y final de php
#ordenar salida 



https://github.com/maryito/Analisis-lexico-sintactico-Python/blob/master/analizador_lexico.py

actividad individual de compilador de php hechon python
importacions de las librerias y creacion de las listas de tokens

Un token o también llamado componente léxico es una cadena de caracteres que tiene un significado coherente en cierto lenguaje de programación. Ejemplos de tókenes podrían ser palabras clave (if, else, while, int, ...), identificadores, números, signos, o un operador de varios caracteres, (por ejemplo, := "':+"' ).

Son los elementos más básicos sobre los cuales se desarrolla toda traducción de un programa, surgen en la primera fase, llamada análisis léxico, sin embargo se siguen utilizando en las siguientes fases (análisis sintáctico y análisis semántico) antes de perderse en la fase de síntesis.

Ejemplo
Supongamos la siguiente línea de un programa:

  SI Nuevo > MaxNúm ENTONCES
Los tókenes son:

  * "SI"
  * "Nuevo"
  * ">"
  * "MaxNúm"
  * "ENTONCES"
Y se describen por lo general en dos partes, un tipo o clase y un valor, así: Token=(Tipo,Valor)

Para la secuencia anterior, los tókenes pueden describirse

  * [Palabra Reservada, "SI"]
  * [Identificador, "Nuevo"]
  * [Operador, ">"]
  * [Identificador, "MáxNúm"]
  * [Palabra Reservada, "ENTONCES"]
