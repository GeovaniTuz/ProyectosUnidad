function genera_rando() {

    //mandar msg
    alert("Genrando Rando");

    // perdir datos para rando
    var text = document.getElementById("randotxt").value;

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

    try {
        pruebapalabra = textoTroceado.length;
        console.log(pruebapalabra);
    } catch (error) {
        console.log("El mensaje nom contiene ninguna palabra. Para evitar errores, se asignará el valor de cero");
        pruebapalabra = 0;
        console.log(pruebapalabra);
    }

    var nuevo = pruebapalabra;
    console.log(nuevo)

    var randonum = Math.floor(Math.random() * nuevo);
    console.log(randonum);
}

//id="randotxt"