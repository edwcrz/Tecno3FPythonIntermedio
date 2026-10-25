se generea un a clase abstracta cuentabancaria padre
cuenta bancaria: readme_cb.md

se generan 3 clases concretas hijas de cuenta bancaria
cuenta ahorro: readme_ca.md
cuenta corriente: readme_cc.md
cuenta cheque: readme_ch.md

inicialmente genere main.py para llamar a los archivos y operar con pequeñas pruebas invocando a los objetos, clases, atributos y metodos
el objetivo era seguir el video de la clase paso a paso
a las pruebas de la clase le sumaba nuevos llamados que me generaban curiosidad

cuando anduvo todo, pase a probar desde codigo prueba
me costo mucho pasarme a ese codigo de prueba porque tenia un mindset diferente
lo adapte minimamente para enteder lo que estabamos probando
no entendi con que debe compararse los resultados correctos, pero creo que esta operando correctamente

aprendizajes que costaron

issue1: durante toda la practica pensaba que el saldo entre las 3 cuentas debia ser uno, pero no era el espiritu de esta tarea
issue2: usaba los metodos como funciones tradicionales, entonces pasaba parametros que no hace falta pasar, simplemente se obtienen de los atributos del objeto. Primero hay que cargar los nuevos valores en el objeto, y luego llamo a metodos y le paso la cantidad minima de parametros posible para que opere, tambien haciendo uso de los atributos del objeto actualizado