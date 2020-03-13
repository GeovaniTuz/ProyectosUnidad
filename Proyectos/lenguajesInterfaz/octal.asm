.model small
.stack
.data

   cad  db 9 dup (' '),'$'
   M1 DB 10, 13, 'DAME EL PRIMER NUMERO : $' ;variable de mensaje 0
   M2 DB 10, 13, 'DAME EL PRIMER NUMERO : $' ;variable de mensaje 0
   var1 db ?
   num  db ?
   aux  db ?
 
.code
.startup
    
   mov ah, 9
   lea dx, M1
   int 21h
   
   mov ah,01h   ;Utilizado con la interrupcuón siguiente
   int 21h      ;Interrupción para leer
   sub al,30h   ;Obtención de valor real
   mov num,al   ;Número con que trabajaremos

   mov al,num  
   mov bl,10    ;Movemos a bl 10
   mul bl       ;Multiplicamos 10 por el número a convertir
   mov aux,al   ;Asignamos a aux el residuo

   mov var1,0   
   mov ah,01h
   int 21h      
   sub al,30h
   add aux,al   ;Lo agregamos al número anterior multiplicado por 10
   mov bl,aux   ;Éste ya no necesita ser multiplicado
   mov num,bl   ;

   mov ah,02h   ;Imprimimos signo de igual
   int 21h

   mov SI,2     ;Comienzan los ciclos de division entre 2
   bin:         ;Uso de etiqueta

      mov Ah,00h;+
      mov Al,num
      mov Bl,8
      div Bl
      mov var1,Ah
      mov num,Al

      mov dl,var1
      add dl,30h

      mov cad[SI],dl;Concatenamos resultados

      cmp num,1 ;Hacemos comparacion
      dec SI
      jne bin   ;Indicamos volver a etiqueta bin o:
       je salida   ;Ir a etiqueta salir



      cmp num,0 ;Comparación con 0
       jne bin
        je salida

   salida:          ;Etiqueta de salida   
   
   mov ah, 9
   lea dx, M2
   int 21h

      mov dl,num ;Proceso para imprimir cadena final
      add dl,30h

      mov cad[SI],dl

  mov ah,09h
  lea Dx,cad
  int 21h

.exit
end