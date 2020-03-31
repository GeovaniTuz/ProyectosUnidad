
var cuenta = -1;

function EcuArit() {
    
    var ecuacion = document.getElementById('ecu').value; //tomo lo que el usuario haya escrito para analizar
   
   var finales = []; //Aquí almacenaré el resultado que se imprimirá en la pagina

   finales = JerarquiaRecursiva(ecuacion); //llamo a la función recursiva de análisis y guardo lo que devuelva en "finales"
   console.log(finales);
   document.getElementById('para').value = finales;

   for(var i = 0; i<= cuenta; i++){
    document.getElementById('para').value = document.getElementById('para').value.replace(",", "\n");
   }

   cuenta = -1;


}




function JerarquiaRecursiva(texto){

    //Esta seráuna version recursiva del analisis, cada condicion podrá llevar a un nuevo analisis para poder reducir el sistema a solo sumas y restas
    //

    var generalparentesis = /['('][a-z\d\s+\-*\/\+\*\-]+[')']/gi; //Expresion para buscar parentesis
    var generalmultidiv = /[\d\sa-z\*\/]+[\*\/][\d\sa-z\*\/]+/gi; //Expresion para buscar Multiplicaciones o divisiones
    var generalsumaresta = /[\d{1,}\s{0,}a-z\+\-]+[+\-][\s{0,}\d{1,}a-z\+\-]+/gi; //Expresion para buscar Sumas y restas
    var formula = texto.toString();

    console.log("Cuenta = ");
    console.log(cuenta);


    //Cabe destacar que solo necesitamos esas expresiones generales para poder reducirlas y saber cuándo parar.
    //Por ejemplo, en la ecuación "12 + 3 * (8 / 2)" debe quedar que:
    //t0 = 8/2 (los parentesis indican que lo que este dentro de ellos se resuelve primero)
    //t1 = 3 * t0 (Se resuelve la multiplicacion)
    //t2 = 12 + t1

    //En ese proceso, primero se identifican los grupos con paréntesis, pero estos pueden contener grupos con sumas y restas que se deben atender, por eso la idea de hacerlo recursivo

    var tokens = [];//Necesitaremos dónde guardar los tokens encontrados, en general la cadena "t0 = ..." y las que le siguen, facilitando la acción de mostrar los resultados
    var pushear = [];
       if(texto != null){ //Si la cadena no es nula, empieza el analisis
           
            while(texto.match(generalparentesis) != null){ //Si encuentra un grupo con parentesis
               var parentesis = texto.match(generalparentesis) //Almacena todos los resultados,incluso los que tengan más parentesis internos
               //Éstos parentesis internos NO los cuenta como otros resutados hasta que sean depurados los que los contienen
               console.log(parentesis.length);
               for(var p = 0; p < (parentesis.length); p++) {//con cada uno de las coincidencias, haré lo siguente:
                   console.log(parentesis[p]); //Del resultado que este analizando quito

                   var respaldo = parentesis[p];//almaceno una copia para saber qué quitar despupes de la resolución de los paréntesis

                   parentesis[p] = parentesis[p].replace('(', ''); //El primer
                   parentesis[p] = parentesis[p].replace(')', ''); //Y ultimo parentesis

                   console.log("Este es parentesis:");
                   console.log(parentesis);
                   console.log("este es parentesis[p]");
                   console.log(parentesis[p]);
                   console.log("llamo a la funcion recursiva");
                   pushear = JerarquiaRecursiva(parentesis[p]);
                   console.log("Pushear:");
                   console.log(pushear);
                   tokens.push(pushear);
                   console.log("despues de recursiva, en tokens hay:");
                   console.log(tokens.length);
                   console.log("Que son:");
                   console.log(tokens);                   
                   console.log("cuantos:");
                   var cuantos = tokens.length - 1;
                   console.log(cuantos);
                   pp = tokens[cuantos];
                   var porsi = pp.length - 1;
                   console.log("pp = ");
                   console.log(pp);
                   console.log("porsi = ");
                   console.log(porsi);
                   console.log("pp[porsi]=")
                   console.log(pp[porsi]);
                   pp = pp[porsi].match(/["t"][0-9]+/);
                   console.log("Valor de pp despues del match:")
                   console.log(pp);
                   texto = texto.replace(respaldo, pp ); // y mando esa cadena a analizar hasta acabar con los paréntesis
                   console.log("Éste es el resultado sustituido:");
                   console.log(texto);
                   
               } ;
               parentesis = texto.match(generalparentesis); 
            };

           

           if(texto.match(generalmultidiv) != null){ //cuando llegue aquí, los resultados que analizaré serán puras multiplicaciones y divisiones
                //esas cadenas deben ser resueltas antes que las sumas y restas
                //Buscaré todas las multiplicaciones y divisiones que hayan para depurarlas
                
                var multidiv = texto.match(generalmultidiv) //Almacena todas las cadenas con multiplicaciones y divisiones
                
                for(var md = 0; md < multidiv.length; md++){//por cada uno de esos resultados:
                    
                    
                    if(tokens.length == null){
                        console.log("multi Tokens = null")
                        formula.replace(multidiv[md], "t1")
                        tokens.push(tes + " = " + multidiv[md]); //almaceno esa multiplicacion y/o division en la lista de tokens
                    }else{
                        console.log("multi Tokens != null")
                        cuenta = cuenta + 1;
                        var tes = "t" + cuenta;
                        texto = texto.replace(multidiv[md], tes)
                        console.log(texto);
                        console.log(multidiv[md]);
                        
                        tokens.push(tes + " = " + multidiv[md]); //almaceno esa multiplicacion y/o division en la lista de tokens
                    }
                    
                    //Si solo quedasen multiplicaciones, esas conformarian el token completo
                }
                console.log(tokens);
            }

            if(texto.match(generalsumaresta) != null){//Cuando llegue aqui, los resultados que analizaré seran puras sumas y restas
                //estas cadenas seran resueltas de ultimo, por lo mismo, ya habran puros tokens sumando o restando
                //Esto provocará que esas sean todo el token
                var sumaresta = texto.match(generalsumaresta)//Almacena todas las coincidencias de sumas y restas
                if(tokens.length == null){
                    console.log("suma Tokens = null")
                    texto.replace(sumaresta,"t1")
                    tokens.push("t1 = " + sumaresta);
                }else{
                    console.log("suma Tokens != null")
                    cuenta = cuenta + 1;
                    var tes = "t" + cuenta;
                    texto = texto.replace(sumaresta,tes);
                    tokens.push(tes + " = " + sumaresta);
                    console.log("Estoy en sumaresta\nEn tokens ahora hay:");
                    console.log(tokens.length);
                    console.log("Que son:");
                    console.log(tokens)
                }
                
            }
            
            
    return(tokens); 
    };

}

