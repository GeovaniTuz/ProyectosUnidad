function genera_tabla() {

    function multiple(valor, multiple)
    {
        resto = valor % multiple;
        if(resto==0)
            return true;
        else
            return false;
    }


   var matriz = new Array(20);
   var aumento = 1;

     //creamos arrary de una dimensión del tamaño tabla anterior
      for (var i = 0; i < matriz.length; i++) { 
      matriz[i] = []; 
      } 
     //creamos bidimensional con el array anterior, duplicando en columnas y lo llenamos
       
      for (var i = 0; i < matriz.length; i++) { 
          for (var j = 0; j < matriz.length; j++) { 
              
              matriz[i][j] = [aumento++]; 
          }
      }
      
      var abretabla= "<table style'width:100%' >";
      var cierratabla = "</table>";
      var abretr = "<tr>", abretd ="<td>";
      var cierratr = "</tr>", cierratd ="</td>";
      var color = "<td style='background: red'>";
      document.write(abretabla);
      for (var i = 0; i < matriz.length; i++) {
          document.write(abretr); 
          for (var j = 0; j < matriz.length; j++)             
          {
              var nob = matriz[i][j];
            if (multiple(nob,5)) {
              document.write(color + matriz[i][j]); 
          }else{
            document.write(abretd + matriz[i][j]);
          }
          } 
          document.write(cierratr); 
      } 
      document.write(cierratabla);
      
    // Obtenemos la referencia del elemento body
 /*    var body = document.getElementsByTagName("body")[0];
    // Creamos un elemento <table> y un elemento <tbody>
    var tabla = document.createElement("table");
    var tblBody = document.createElement("tbody");
    // Creamos las celdas
    for (var i = 0; i < 1; i++) {
        // Creamos las hileras de la tabla
        var fila = document.createElement("tr");
        
        //(<th scope="row"> y <th scope="col"></th>
        for (var j = 0; j < 500; j++) {
            // Crea un elemento <td> y un nodo de texto, hace que el nodo de
            // texto sea el contenido de <td>, ubica el elemento <td> al final
            // de la hilera de la tabla
            var celda = document.createElement("td");
            var textoCelda = document.createTextNode(+ j);
            celda.appendChild(textoCelda);
            fila.appendChild(celda);
            
        }
        // agregamos la hilera al final de la tabla (al final del elemento tblbody)
       tblBody.appendChild(fila);
    }
    // posicionamos el <tbody> debajo del elemento <table>
    tabla.appendChild(tblBody);
    // appends <table> into <body>
    body.appendChild(tabla);
    // modifica el atributo "border" de la tabla y lo fija a "2";
    tabla.setAttribute("border", 1);
    tabla.setAttribute("id", "tabla");
    

  var result = document.getElementById("resultado");
   //result.appendChild(tabla);
   document.getElementById("tabla").width= 10 ;
   document.getElementById("tabla").height= 10; //ALTO

*/
    

    
  
   
}