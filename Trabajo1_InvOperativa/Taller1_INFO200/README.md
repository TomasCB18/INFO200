El programa se ejecuta abriendo el programa en visual (o cualquier editor). Al ejcutar el codigo, se  preguntara si se quieren modificar los Coeficientes que acompañan a las variables
x1 y x2(pelota de tenis y futbol respectivamente) y el lado derecho de las restricciones, de no cambiarlas, el programa se ejecutara con las variables dadas en el enunciado que
son las siguientes: 
x1:pelota_de_tenis
x2:pelota_de_futbol

5000x1 + 8000x2 <= 150000
155x1 + 5700x2 <= 50000
58x1 + 450x2 <= 5000

max: z = x1 + x2

x1,x2>=0

el contexto del es el siguiente: 
Una persona desea comprar pelotas de futbol y tenis para su centro deportivo, por lo cual lleva una caja donde almacenara 
los productos que comprara, donde la caja soporta una cierta cantidad de peso, al igual el dinero acotado que tiene.
Una pelota de tenis y futbol tienen el valor de 5.000 y 8.000 pesos respectivamente cada una.
El dinero que posee la persona que quiere comprar es de 150.000 pesos como maximo para gastar.
El espacio de volumen que posee una pelota de tenis y futbol es de 155 y 5700 cm cubicos respectivamente,
y la caja tiene un volumen de 50000 cm cubicos.
El peso que puede soportar la caja es de maximo 5000 gramos, donde una pelota de tenis pesa 58 gramos y una de futbol 450 gramos.

si al cambiar las restricciones, estas llegasen a tener numeros donde no haya solucion factible, se dira en consola un mensaje diciendo
que no hay solucion, de no ser asi, en consola se dara el punto optimo y la soluccion de x1 y x2

al cambiar los parametros en el grafico puede que la region factible no se abarque, pero el punto optimo de la solucion siempre estara en el grafico, los mismo con las graficas que no 
abarcan toda la region en algunos casos por las limitaciones del ancho y largo del grafico
