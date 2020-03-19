function EcuArit() {
    
        var ecuacion = document.getElementById('ecu').value;
       //let arrayEcua = ecuaSinEspa.match(new);
           if(ecuacion != null){
               var expres = /\d{1,}\s{0,}['+']\s{0,1}\d{1,}/gi; 
               var suma = ecuacion.match(expres);
               var i = 0;
               var t = 't';
               var result = t + i + '=' + suma;
               var otro = ecuacion.replace(expres,t+i);
               i++;
               var result2 = t+i+'='+otro;
          };
        document.getElementById('para').value = result +"\n"+result2;
       
}