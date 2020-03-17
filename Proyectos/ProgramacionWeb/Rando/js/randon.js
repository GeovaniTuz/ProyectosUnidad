function numerorandom() {

    //mandar msg
    //alert("Genrando Rando");

    // perdir datos para rando
    var text = document.getElementById("caja2").value;

    //contar palabras del mesage

    var texto = text;
    if (texto != "") {

        //Reemplazamos los saltos de linea por espacios
        texto = texto.replace(/\r?\n/g, " ");
        //Reemplazamos los espacios seguidos por uno solo
        texto = texto.replace(/[ ]+/g, " ");
        //Quitamos los espacios del principio y del final
        texto = texto.replace(/^ /, "");
        texto = texto.replace(/ $/, "");
        //Troceamos el texto por los espacios
        var textoTroceado = texto.split(" ");
        //Contamos todos los trozos de cadenas que existen

    }
    var pruebapalabra;
    pruebapalabra = textoTroceado.length;

    // total de palabras que existen. 
    console.log(pruebapalabra)
    //-------------------------------------
    var contador = [];

    //console.log(contador);
    document.getElementById('resultadorandom').innerHTML = pruebapalabra;
    //FIN DEL CONTADOR DE PALABRAS


    var randonum = Math.floor(Math.random() * pruebapalabra);
    console.log(randonum);

    document.getElementById('resultadorandom3').innerHTML = randonum;

    var iniciolink = "<a href='https://www.w3schools.com/colors/colors_picker.asp'>", finlink = "</a>";
    var iniciop = "<p>", finp = "</p>", punto = ". ", saltar = "<br>";
    var elemento = " TEXTO TOMADO DE LA CAJA Y TROCEADO --> ", elemento2 = "Numero random generado: ";
    //var n = a + "<br>" + b + "<br>" + c + "<br>" + d;

    //document.write(espa);
   // document.write(iniciop); // INICIO DE LA ETIQUETA P
    for (var i = 0; i < randonum; i++) {
        contador = textoTroceado;
        var les = iniciolink + contador[i] + finlink;
        // document.write(iniciolink + contador[i] + finlink);
        // les.toString();
        //var cade = les.toString();
        document.write(" ", les);
        //document.write(punto);


    }

    // total de palabras que se deben de hacer viculo
    //console.log(i);

   // document.write(saltar + saltar + elemento + contador, saltar + saltar + elemento2 + randonum);
    //var cade = les.toString();


   // document.write(finp); //FIN DE LA ETIQUETA P
    //FIN DE GENERACION DE NUMERO RANDOM

}

