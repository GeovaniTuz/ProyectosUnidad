var ecuacion = "2 + 33 / 77";


//let arrayEcua = ecuaSinEspa.match(new);
if(ecuacion != null){
    var expres = /\d{1,}\s{0,}['+']\s{0,1}\d{1,}/gi; 
    //var re = new RegExp(`\\b${expres}\\b`,'gi');
    var suma = ecuacion.match(expres);
    var i = 0;
    var t = 't';
    var resutl = t + i + '=' + suma + '';
    var otro = ecuacion.replace(expres,t+i);
    i++;
    var result2 = t+i+'='+otro;
    var imprime = "'"+ resutl + 
    + result2 +"'";
    };
console.log(imprime);
//console.log(result2);