/*EXPLICACION ALGORITMO DE EUCLIDES*/

Lo primero que hace el codigo es encontrar el resto y cociente de dividir a y b hasta que b sea 0. Cada iteración q hagamos pasara a ser b y b sera el resto de la division.

Usando la formula    -> a = b * c + r
Usando los nums 393 y 267 = 393 = 267 * 1 + 126.
El resultado del cociente es 1 y el resto 126. Repetimos hasta que b sea 0 como lo dije antes.

267 = 126*2+15 -> 126 = 15*8+6 -> 15 = 6*2+3 -> 6 = 3*2+0

Podemos ver en las iteraciones que para la segunda división 126/15, a es el b de la anterior (a = 126) y b es el resto (b =15). Como la siguiente operación seria 3 entre 0 , b es 
igual a 0 asi que paramos. Despues de hacer eso para que sea mas facil el calculo lo que hice fue crear una tabla para que sea mas  de u y v de cada operacion: 

<table style="width: 100%; text-align: center;">
  <tr>
    <td style="width: 33%;">r</td>
    <td style="width: 33%;">c</td>
    <td style="width: 33%;">u</td>
    <td style="width: 33%;">v</td>
  </tr>
  <tr>
    <td colspan="0.5" style="width: 100%; padding-top: 50px;">393</td>
    <td colspan="0.5" style="width: 100%; padding-top: 50px;"></td>
    <td colspan="0.5" style="width: 100%; padding-top: 50px;">u-1</td>
    <td colspan="0.5" style="width: 100%; padding-top: 50px;">v-1</td>
  </tr>
    <tr>
    <td colspan="0.5" style="width: 100%; padding-top: 50px;">267</td>
    <td colspan="0.5" style="width: 100%; padding-top: 50px;"></td>
    <td colspan="0.5" style="width: 100%; padding-top: 50px;">u0</td>
    <td colspan="0.5" style="width: 100%; padding-top: 50px;">v0</td>
  </tr>
    <tr>
    <td colspan="0.5" style="width: 100%; padding-top: 50px;">126</td>
    <td colspan="0.5" style="width: 100%; padding-top: 50px;">1</td>
    <td colspan="0.5" style="width: 100%; padding-top: 50px;">u1</td>
    <td colspan="0.5" style="width: 100%; padding-top: 50px;">v1</td>
  </tr>
   <tr>
    <td colspan="0.5" style="width: 100%; padding-top: 50px;">15</td>
    <td colspan="0.5" style="width: 100%; padding-top: 50px;">2</td>
    <td colspan="0.5" style="width: 100%; padding-top: 50px;">u2</td>
    <td colspan="0.5" style="width: 100%; padding-top: 50px;">v2</td>
  </tr>
    <tr>
    <td colspan="0.5" style="width: 100%; padding-top: 50px;">6</td>
    <td colspan="0.5" style="width: 100%; padding-top: 50px;">8</td>
    <td colspan="0.5" style="width: 100%; padding-top: 50px;">u3</td>
    <td colspan="0.5" style="width: 100%; padding-top: 50px;">v3</td>
  </tr>
    <tr>
    <td colspan="0.5" style="width: 100%; padding-top: 50px;">3</td>
    <td colspan="0.5" style="width: 100%; padding-top: 50px;">2</td>
    <td colspan="0.5" style="width: 100%; padding-top: 50px;">u4</td>
    <td colspan="0.5" style="width: 100%; padding-top: 50px;">v4</td>
  </tr>
</table>



Como podemos observar en esta tabla demostrativa del calculo hemos colocado los restos y cocientes calculados previamente. Y las 2 ultimas columnas don los coeficientes que cumplen la operacion:

r = a * u + b * v , donde tenemos que a = 393 y b = 267.

En los dos primeros caso usaremos (u-1=1,v-1=0) y (u0=0,v0=1). Y si queremos calcular u1 y v1 en adelante tenemos que hacer lo que pongo a continuacion.

ri = ri-2 – cociente * ri-1 , esta formula se utiliza para u y para v.

Lo que nos da de resultado este algoritmo es el resto anterior a la operación en que b es 0. Y como resultado el mcd(393,267) = 3.

Resultado : 3 = 393*(-36) + 267*53

