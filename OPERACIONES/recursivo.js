
function EcuArit() {
    
    var ecuacion = document.getElementById('ecu').value;
   //let arrayEcua = ecuaSinEspa.match(new);
   var finales = [];
   
    //document.getElementById('para').value = result +"\n"+result2;
    console.log("Estoy en acuarit, intento invocar a la otra funcion")
   finales = JerarquiaRecursiva(ecuacion);
   console.log("termino ecuarit")
   document.getElementById('para').value = finales;


}

function JerarquiaRecursiva(texto){

    //Esta seráuna version recursiva del analisis, cada condicion podrá llevar a un nuevo analisis para poder reducir el sistema a solo sumas y restas
    //

    var generalparentesis = /['('][a-z\d\s+\-*\/]+[')']/gi; //Expresion para buscar parentesis
    var generalmultidiv = /[\(\d\sa-z\)]+[\*|\/][\(\d\sa-z\)]+/gi; //Expresion para buscar Multiplicaciones o divisiones
    var generalsumaresta = /[\(]*[\d{1,}\s{0,}a-z]+[\)]*[+\-][\(]*[\s{0,}\d{1,}a-z]+[\)]*/gi; //Expresion para buscar Sumas y restas
    var formula = texto.toString();

    //Cabe destacar que solo necesitamos esas expresiones generales para poder reducirlas y saber cuándo parar.
    //Por ejemplo, en la ecuación "12 + 3 * (8 / 2)" debe quedar que:
    //t0 = 8/2 (los parentesis indican que lo que este dentro de ellos se resuelve primero)
    //t1 = 3 * t0 (Se resuelve la multiplicacion)
    //t2 = 12 + t1

    //En ese proceso, primero se identifican los grupos con paréntesis, pero estos pueden contener grupos con sumas y restas que se deben atender, por eso la idea de hacerlo recursivo

    var tokens = [];//Necesitaremos dónde guardar los tokens encontrados, en general la cadena "t0 = ..." y las que le siguen, facilitando la acción de mostrar los resultados
       if(texto != null){ //Si la cadena no es nula, empieza el analisis
           
            if(texto.match(generalparentesis) != null){ //Si encuentra un grupo con parentesis
               var parentesis = texto.match(generalparentesis) //Almacena todos los resultados,incluso los que tengan más parentesis internos
               //Éstos parentesis internos NO los cuenta como otros resutados hasta que sean depurados los que los contienen
               console.log(parentesis.length);
               for(var p = 0; p < (parentesis.length); p++) {//con cada uno de las coincidencias, haré lo siguente:
                   console.log(parentesis[p]); //Del resultado que este analizando quito
                   parentesis[p] = parentesis[p].replace('(', ''); //El primer
                   parentesis[p] = parentesis[p].replace(')', ''); //Y ultimo parentesis
                   
                   console.log(parentesis);
                   console.log(parentesis[p]);
                   JerarquiaRecursiva(parentesis[p]); // y mando esa cadena a analizar hasta acabar con los paréntesis
               } ;  
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
                        var tes = "t" + tokens.length;
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
                    var tes = "t" + tokens.length;
                    texto = texto.replace(sumaresta,tes);
                    tokens.push(tes + " = " + sumaresta);
                }
                
            }
            
            
    return(tokens); 
    };

}

