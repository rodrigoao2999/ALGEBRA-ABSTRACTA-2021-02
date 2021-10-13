/*EXPLICACION ALGORITMO DE EUCLIDES*/

Lo primero que hace el codigo es encontrar el resto y cociente de dividir a y b hasta que b sea 0. Cada iteración q hagamos pasara a ser b y b sera el resto de la division.

Usando la formula    -> a = b * c + r
Usando los nums 393 y 267 = 393 = 267 * 1 + 126.
El resultado del cociente es 1 y el resto 126. Repetimos hasta que b sea 0 como lo dije antes.

267 = 126*2+15 -> 126 = 15*8+6 -> 15 = 6*2+3 -> 6 = 3*2+0

Podemos ver en las iteraciones que para la segunda división 126/15, a es el b de la anterior (a = 126) y b es el resto (b =15). Como la siguiente operación seria 3 entre 0 , b es 
igual a 0 asi que paramos. Despues de hacer eso para que sea mas facil el calculo lo que hice fue crear una tabla para que sea mas  de u y v de cada operacion: 

r  | c  | u  | v  |
393|    | u-1| v-1|
267|    | u0 | v0 |
126| 1  | u1 | v1 |
15 | 2  | u2 | v2 |
6  | 8  | u3 | v3 |
3  | 2  | u4 | v4 |

Como podemos observar en esta tabla demostrativa del calculo hemos colocado los restos y cocientes calculados previamente. Y las 2 ultimas columnas don los coeficientes que cumplen la operacion:

r = a * u + b * v , donde tenemos que a = 393 y b = 267.

En los dos primeros caso usaremos (u-1=1,v-1=0) y (u0=0,v0=1). Y si queremos calcular u1 y v1 en adelante tenemos que hacer lo que pongo a continuacion.

ri = ri-2 – cociente * ri-1 , esta formula se utiliza para u y para v.

Lo que nos da de resultado este algoritmo es el resto anterior a la operación en que b es 0. Y como resultado el mcd(393,267) = 3.

Resultado : 3 = 393*(-36) + 267*53

<table style="width: 100%; text-align: center;">
  <tr>
    <td style="width: 33%;">Primera columna</td>
    <td style="width: 33%;">Segunda columna</td>
    <td style="width: 33%;">Tercera columna</td>
  </tr>
  <tr>
    <td colspan="3" style="width: 100%; padding-top: 50px;">Más contenido</td>
  </tr>
  <tr>
    <td  colspan="3" style="width: 100%; padding-top: 50px;">Pie de página</td>
  </tr>
</table>

