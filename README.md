# Solucionador De Ecuaciones

Este programa tiene como objetivo principal el ser capaz de solucionar y graficar diferentes ecuaciones, llegando a las diferentes soluciones de la misma (si es que tiene más de una) mediante el uso de seis métodos: Tanteo, Bisección, Regla Falsa, Newton Raphson, Secante y Steffensen.

La finalidad de usar diferentes métodos es poder concluir cuál se adapta mejor a las diferentes situaciones y casos específicos que se pueden presentar a la hora de desarrollar las ecuaciones. El apartado de iteraciones muestra cuánta veces en promedio el programa tuvo que recorrer el método para llegar a cada solución, por lo tanto, el método que requiera menos iteraciones, y tenga más precisión en su respuesta, será el más óptimo para esa ecuación.

En la sección donde se sitúa la gráfica se puede observar el trazo de la línea correspondiente a esa función y en qué punto o puntos logra tocar el eje x (Marcado con un punto rojo en cada lugar donde la función toque el eje). En la gráfica se tiene la posibilidad de moverse dentro de cualquier punto de la grilla y acercarse para ver con exactitud los puntos de corte.

Es importante que antes de iniciar el programa se descarguen las librerías necesarias para su correcto funcionamiento. Esto se puede hacer fácilmente con el comando **pip install -r "requirements.txt"**. Dentro del archivo requirements.txt están las librerías necesarias, con la versión específica, que necesita el proyecto para funcionar.

Al programa se le añadió una pequeña pantalla de carga al presionar el botón resolver. Esta permanece presente mientras que el programa termina de hacer los diferentes cálculos. A su vez, mientras esta pantalla esté presente, se inhabilita cualquier acción dentro del programa para evitar sobrecargarlo de peticiones y que el código se rompa. Es preciso mencionar que a veces los tiempos de carga son largos, debido a que se tuvo que encontrar el equilibrio entre precisión y tiempo de carga. Estos son directamente proporcionales.

Si ha pasado un buen tiempo y no ha desaparecido la pantalla, es porque la ecuación es muy compleja para alguno de los métodos (o todos) y debe de hacer todas las iteraciones posibles para resolverlo. Deje que el programa termine de resolver y que la pantalla de carga desaparezca. No presione la pantalla desesperadamente ni esfuerce mucho el equipo con otras aplicaciones. Los únicos dos indicativo de que el programa se rompió y debe volver a ejecutarlo es que windows le reporte que el programa dejó de responder, o que le salga algún mensaje en consola informando de un error. Si ese es el caso, por favor reportelo detalladamente para poder mejorar el software.

Entre menos métodos de solución seleccione al mismo tiempo, más ágil será la respuesta del programa ante su petición.

Cabe resaltar que cada uno de los métodos tiene un límite de iteraciones, con el objetivo de no obstaculizar la ejecución de los métodos que están después. Si este límite de iteraciones se cumple, le saltará una pantalla informándole, con el nombre del método y su razón. Al presionar “OK” le dará vía al programa para que pueda continuar la ejecución de la ecuación por los otros métodos de manera normal.

Al lado del botón “Resolver” encontrará el botón “Reporte”, este le generará un reporte en formato PDF de la información exacta que tiene en pantalla al momento de presionar el botón, tanto de los resultados como de la gráfica. Este archivo se guardará en la carpeta “Reports” que encontrará situada en la misma carpeta desde donde ejecutó el archivo **main.py**.

Por último, debajo del apartado donde el usuario coloca la ecuación a resolver, se encuentra un caja de texto donde aparece la derivada de la ecuación introducida. Esta solo aparece después de presionar el botón de resolver, no sin antes haber seleccionado el método que lo requiera (Newton Raphson).
