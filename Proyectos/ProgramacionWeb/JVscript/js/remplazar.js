
function remplazar(){

    //pedir datos
    var valor = document.getElementById("parrafo").value;
    var remplaza = document.getElementById("idremplaz").value;    
    var busca = document.getElementById("idbuscar").value;
    //mach a buscar
    var machh =new RegExp(`\\b${busca}\\b`,'gi');
    //var machh = valor.match(busca);
    // busca toda la respuestas y la cambia

    var txt = valor.replace(machh, remplaza);
    //var bus = valor.match(new RegExp(machh,"gi"));

    // remplaza el contenido de text area
    document.getElementById("parrafo").value = txt;
   // document.getElementById("parrafo1").value = bus;
  }
