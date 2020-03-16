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
    contador = textoTroceado.length;
    console.log(contador);
    document.getElementById('resultadorandom').innerHTML = pruebapalabra;
    //FIN DEL CONTADOR DE PALABRAS


    var randonum = Math.floor(Math.random() * pruebapalabra);
    console.log(randonum);
    
    document.getElementById('resultadorandom3').innerHTML = randonum;

    var iniciolink = "<a href='https://www.w3schools.com/colors/colors_picker.asp'>", finlink = "</a>";
    var iniciop = "<p>", finp = "</p>", espa = "<br>";

    //document.write(espa);

    document.write(iniciop);
    for (var i = 0; i < randonum; i++) {
        var les = iniciolink + contador[i] + finlink;
       // document.write(iniciolink + contador[i] + finlink);
        document.write(les);

       

        document.write(espa);
    }
    //document.write(finp);
    // total de palabras que se deben de hacer viculo
    console.log(i);
    //FIN DE GENERACION DE NUMERO RANDOM

}