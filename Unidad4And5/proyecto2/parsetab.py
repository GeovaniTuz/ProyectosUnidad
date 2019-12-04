
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'rightASIGNARleftSUMARESTAleftMULTDIVrightUMINUSAND ARIAVANZ ARIBASIS ASIGNAR CADENA CIN COMA COMDOB CORDER CORIZQ COUT DECIMAL DISTINTO DIV ENDL ENTERO GET IDENTIFICADOR IGUAL INCLUDE INT LLADER LLAIZQ MAYORDER MAYORIGUAL MAYORIZQ MAYORQUE MENORIGUAL MENORQUE MIENTRAS MINUSMINUS MODULO MULT NAMESPACE NOT NUMERAL OR PARA PARDER PARIZQ PLUSPLUS POTENCIA PUNTOCOMA RESTA RETURN SI SINO STD SUMA TAGINICIO TAG_FINAL USING VOIDdeclaracion : DECIMALdeclaracion : IDENTIFICADOR ASIGNAR expresion PUNTOCOMAdeclaracion : TAGINICIOdeclaracion : TAG_FINALdeclaracion : expresion\n    expresion  :   expresion SUMA expresion\n                |   expresion RESTA expresion\n                |   expresion MULT expresion\n                |   expresion DIV expresion\n                |   expresion POTENCIA expresion\n                |   expresion MODULO expresion\n\n    expresion : RESTA expresion %prec UMINUS\n    expresion  : PARIZQ expresion PARDER\n                | LLAIZQ expresion LLADER\n                | CORIZQ expresion CORDER\n    expresion : ENTEROexpresion : DECIMAL expresion DECIMALexpresion : COMDOB expresion COMDOBexpresion : IDENTIFICADOR'
    
_lr_action_items = {'DIV':([6,7,10,13,15,16,17,19,20,27,28,29,30,31,32,33,34,35,36,37,38,39,],[-19,-16,25,25,-19,-12,25,25,25,25,-13,-18,25,-17,-15,25,25,25,25,-9,-8,-14,]),'$end':([1,4,6,7,8,10,12,15,16,28,29,31,32,33,34,35,36,37,38,39,40,],[-4,-3,-19,-16,-1,-5,0,-19,-12,-13,-18,-17,-15,-11,-6,-10,-7,-9,-8,-14,-2,]),'LLAIZQ':([0,2,3,5,8,9,11,14,18,21,22,23,24,25,26,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'MODULO':([6,7,10,13,15,16,17,19,20,27,28,29,30,31,32,33,34,35,36,37,38,39,],[-19,-16,21,21,-19,-12,21,21,21,21,-13,-18,21,-17,-15,21,-6,21,-7,-9,-8,-14,]),'MULT':([6,7,10,13,15,16,17,19,20,27,28,29,30,31,32,33,34,35,36,37,38,39,],[-19,-16,26,26,-19,-12,26,26,26,26,-13,-18,26,-17,-15,26,26,26,26,-9,-8,-14,]),'PUNTOCOMA':([7,15,16,28,29,30,31,32,33,34,35,36,37,38,39,],[-16,-19,-12,-13,-18,40,-17,-15,-11,-6,-10,-7,-9,-8,-14,]),'TAGINICIO':([0,],[4,]),'LLADER':([7,15,16,27,28,29,31,32,33,34,35,36,37,38,39,],[-16,-19,-12,39,-13,-18,-17,-15,-11,-6,-10,-7,-9,-8,-14,]),'DECIMAL':([0,2,3,5,7,8,9,11,14,15,16,18,19,21,22,23,24,25,26,28,29,31,32,33,34,35,36,37,38,39,],[8,14,14,14,-16,14,14,14,14,-19,-12,14,31,14,14,14,14,14,14,-13,-18,-17,-15,-11,-6,-10,-7,-9,-8,-14,]),'TAG_FINAL':([0,],[1,]),'CORDER':([7,15,16,20,28,29,31,32,33,34,35,36,37,38,39,],[-16,-19,-12,32,-13,-18,-17,-15,-11,-6,-10,-7,-9,-8,-14,]),'ASIGNAR':([6,],[18,]),'COMDOB':([0,2,3,5,7,8,9,11,14,15,16,17,18,21,22,23,24,25,26,28,29,31,32,33,34,35,36,37,38,39,],[5,5,5,5,-16,5,5,5,5,-19,-12,29,5,5,5,5,5,5,5,-13,-18,-17,-15,-11,-6,-10,-7,-9,-8,-14,]),'CORIZQ':([0,2,3,5,8,9,11,14,18,21,22,23,24,25,26,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'POTENCIA':([6,7,10,13,15,16,17,19,20,27,28,29,30,31,32,33,34,35,36,37,38,39,],[-19,-16,23,23,-19,-12,23,23,23,23,-13,-18,23,-17,-15,23,-6,23,-7,-9,-8,-14,]),'PARDER':([7,13,15,16,28,29,31,32,33,34,35,36,37,38,39,],[-16,28,-19,-12,-13,-18,-17,-15,-11,-6,-10,-7,-9,-8,-14,]),'RESTA':([0,2,3,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,],[3,3,3,3,-19,-16,3,3,24,3,24,3,-19,-12,24,3,24,24,3,3,3,3,3,3,24,-13,-18,24,-17,-15,24,-6,24,-7,-9,-8,-14,]),'PARIZQ':([0,2,3,5,8,9,11,14,18,21,22,23,24,25,26,],[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,]),'IDENTIFICADOR':([0,2,3,5,8,9,11,14,18,21,22,23,24,25,26,],[6,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'SUMA':([6,7,10,13,15,16,17,19,20,27,28,29,30,31,32,33,34,35,36,37,38,39,],[-19,-16,22,22,-19,-12,22,22,22,22,-13,-18,22,-17,-15,22,-6,22,-7,-9,-8,-14,]),'ENTERO':([0,2,3,5,8,9,11,14,18,21,22,23,24,25,26,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expresion':([0,2,3,5,8,9,11,14,18,21,22,23,24,25,26,],[10,13,16,17,19,20,27,19,30,33,34,35,36,37,38,]),'declaracion':([0,],[12,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> declaracion","S'",1,None,None,None),
  ('declaracion -> DECIMAL','declaracion',1,'p_declaracion_decimal','main.py',20),
  ('declaracion -> IDENTIFICADOR ASIGNAR expresion PUNTOCOMA','declaracion',4,'p_declaracion_asignar','main.py',24),
  ('declaracion -> TAGINICIO','declaracion',1,'p_declaraxion_taginicio','main.py',28),
  ('declaracion -> TAG_FINAL','declaracion',1,'p_declaraxion_tag_final','main.py',32),
  ('declaracion -> expresion','declaracion',1,'p_declaracion_expr','main.py',36),
  ('expresion -> expresion SUMA expresion','expresion',3,'p_expresion_operaciones','main.py',43),
  ('expresion -> expresion RESTA expresion','expresion',3,'p_expresion_operaciones','main.py',44),
  ('expresion -> expresion MULT expresion','expresion',3,'p_expresion_operaciones','main.py',45),
  ('expresion -> expresion DIV expresion','expresion',3,'p_expresion_operaciones','main.py',46),
  ('expresion -> expresion POTENCIA expresion','expresion',3,'p_expresion_operaciones','main.py',47),
  ('expresion -> expresion MODULO expresion','expresion',3,'p_expresion_operaciones','main.py',48),
  ('expresion -> RESTA expresion','expresion',2,'p_expresion_uminus','main.py',70),
  ('expresion -> PARIZQ expresion PARDER','expresion',3,'p_expresion_grupo','main.py',76),
  ('expresion -> LLAIZQ expresion LLADER','expresion',3,'p_expresion_grupo','main.py',77),
  ('expresion -> CORIZQ expresion CORDER','expresion',3,'p_expresion_grupo','main.py',78),
  ('expresion -> ENTERO','expresion',1,'p_expresion_numero','main.py',85),
  ('expresion -> DECIMAL expresion DECIMAL','expresion',3,'p_expresion_decimal','main.py',89),
  ('expresion -> COMDOB expresion COMDOB','expresion',3,'p_expresion_cadena','main.py',93),
  ('expresion -> IDENTIFICADOR','expresion',1,'p_expresion_nombre','main.py',97),
]
