<h1 style="text-align: center;">Informe de la Práctica 3</h1>
<h3 style="text-align: center;">Elaborar y Controlar el proyecto TAD</h3>
<h3 style="text-align: center;">Realizado por: Ramón Francisco Ramos Tristán</h3>


Descripción

<p align="justify">En esta práctica lo que haremos será la implementación en Python de una serie de tipos abstractos de datos. Los tipos que tendrán que desarrollar los alumnos variarán dependiendo de a que proyecto hayan sido asignado.

<p align="justify">Cada proyecto tendrá que tener un repositorio propio en la cunta de la asignatura. Además de desarrollar su propio proyecto cada alumno estará encargado de supervisar el proyecto de otro compañero que tenga que implementar el mismo tipo de dato.

<p align="justify">De esta forma cada alumno tendrá que desarrollar su propio proyecto a medida que va solucionando los problemas que su supervisor le indica y mientras supervisa otro proyecto.

####_Realización_

<p align="justify">En este caso el tipo de dato al que ha sido asignado es <a href="https://aulavirtual.ual.es/bbcswebdav/pid-1469282-dt-content-rid-6293229_1/courses/COURSE_0000020549/Poligono.pdf">Poligono</a>, en el cual se nos pide implementar una clase que represente a los poligonos y crear una serie de funciones que nos permitan saber si el poligono creado es cóncavo o convexo, triangular un poligono cualquiera mediante el algoritmo de Van Gogh, calcular el centroide del poligono. Además de crear otras clases que nos permitan representar un punto o linea bidimensional.

En este repositorio se pueden apreciar las diferentes clases que representan estas entidades:

- <p align="justify">La clase <a href="https://github.com/PRIS2/ro/blob/main/poligono.py">poligono.py</a> tiene un metodo que permite craer un poligono cualquiera (incluido un triangulo) al pasarle un array con una serie de puntos que representan sus vertices. Esta clase contiene todas las funciones describidas anteriormente.

- <p align="justify">La clase <a href="https://github.com/PRIS2/ro/blob/main/punto.py">punto.py</a> permite crear un punto bidimensional al pasarle las coordenadas del mismo.

- <p align="justify">La clase <a href="https://github.com/PRIS2/ro/blob/main/vector.py">vector.py</a> sirve de clase auxiliar que nos ayuda a determinar si un poligono es cóncavo o no.

- <p align="justify">La clase <a href="https://github.com/PRIS2/ro/blob/main/linea.py">linea.py</a> nos permite definir una linea bidimensional a traves de las diferentes posibles ecuaciones de la recta y que cuenta con dos funciones: una que permite devolver la representación implicita de la linea independientemente de como se haya establecido en primer lugar, y otra que al psarle otra linea cualquiera nos permite clacular si las lineas son secantes o paralelas y devolver 0 o 1 en función de ello.

- <p align="justify">La clase <a href="https://github.com/PRIS2/ro/blob/main/tests.py">tests.py</a> en dónde realizamos las comprabociones de la funcionlidad de las clases poligono y linea, además de implementar una función que nos permite crear un poligono mediante la interacción con la consola y que nos devuelve si el poligono creado es cóncavo o convexo.


####_Monitoreo_

<p align="justify">En este apartado se describirá el proceso de como se ha llevado a cabo la supervisión del proyecto que tenía que revisar y como he modificado mi código para evitar los errores que me ha indicado mi supervisor.

<p align="justify">En esta práctica se han intentado supervisar los diferentes errores que puede contener el código así como los smells del mismo, como pueden ser problemas de nomenclatura, trozos de código repetido, funciones vacías, condicionales if sin else...

<p align="justify">Para intentar identificar estos errores hemos hecho uso de 2 herramientas diferentes, Sonarcloud y Codacy, una vez se identificaban los posibles errores del proyecto que tenías que monitorear, se creaban issues en el repositorio del mismo indicandolos para su arreglo.

![Sonarcloud](https://github.com/PRIS2/ro/blob/main/img/img1.PNG "Sonarcloud")
![Codacy](https://github.com/PRIS2/ro/blob/main/img/img2.PNG "Codacy")


<p align="justify">A medida que iba desarrollando mi código mi supervisor me indicó una serie de errores que había en mi código, una vez considerados, los corregí y una vez resueltos cerré los issues de mi repositorio, cabe destacar que la mayoróa de los smell se deben a Codacy dado que a la hora de programar, lo hacía en VSCode con el paquete de Sonarlint instalado que me indicaba los smells de mi código.

![Issues](https://github.com/PRIS2/ro/blob/main/img/img3.PNG "Issues")

A la vez iba monitoreando el proyecto que me había sido asignado, el proyecto Pi, para ello mire los issues que presentaba el código tanto en Codacy como en Sonarcloud e hice un resumen, además de destacar la fulta de funcialidades en una de las clases.


![Issues Pi](https://github.com/PRIS2/ro/blob/main/img/img5.PNG "Issues Pi")
![Issues Pi](https://github.com/PRIS2/ro/blob/main/img/img1.PNG "Issues Pi")


<p align="justify">Con todo esto termina mi informe de la Práctica 3, tambien adjunto el Codacy Badge que indica la calidad del código de mi proyecto según Codacy.




[![Codacy Badge](https://app.codacy.com/project/badge/Grade/9e5a2de079784e75b399af45b8f38a37)](https://www.codacy.com/gh/PRIS2/ro/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=PRIS2/ro&amp;utm_campaign=Badge_Grade)

