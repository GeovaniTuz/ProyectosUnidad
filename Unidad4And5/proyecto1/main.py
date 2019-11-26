# -*- coding: utf-8 -*-
# desarollo de aanalizardor lexico

# inportacion de librerias necesarias
#import ply.lex as lex
import re
import codecs
import os
import sys

# lista de tockes necesarios para el compilador

tokens = ['',

          ]

# lista de palabras reservadas

reservadas = {
    '__halt_compiler',
    'abstract', 'and', 'array', 'as', 'break',
    'callable', 'case', 'catch', 'class',
    'clone', 'const', 'continue', 'declare',
    'default', 'die', 'do', 'echo',
    'else', 'elseif',
    'empty', 'enddeclare', 'endfor',
    'endforeach', 'endif', 'endswitch',
    'endwhile', 'eval', 'exit', 'extends',
    'final', 'for', 'foreach', 'function',
    'global', 'goto', 'if', 'implements',
    'include', 'include_once', 'instanceof',
    'insteadof', 'interface', 'isset', 'list',
    'namespace', 'new', 'or', 'print', 'private',
    'protected', 'public', 'require', 'require_once',
    'return', 'static', 'switch', 'throw', 'trait',
    'try', 'unset', 'use', 'var', 'while', 'xor'
}

print("termino de ejecucion")
