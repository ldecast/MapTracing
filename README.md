# MapTracing

### Hecho por: Luis Danniel Ernesto Castellanos Galindo
_Carnet: 201902238_

**Descripción del programa:** la funcionalidad principal de la aplicación MapTracing es el trazado de 
mapas, en los cuales se calcula la ruta con menos afluencia vehicular a partir de un archivo de texto 
que será cargado por el usuario y será capaz de reconocer y reportar errores que se encuentren en él 
así como un listado de tokens.

#### Clases:
- Main.py: menú en consola que permite al usuario seleccionar la opción que desee.
- Automata.py: clase que se encarga de leer el archivo de texto y realizar un análisis léxico y sintáctico
para obtener los datos.
- Reportador.py: genera archivos .csv con la lista de errores y tokens respectivamente que fueron recabados
por el autómata.
- Graficador.py: implementa el uso de Graphviz para graficar las mapas y rutas que el usuario desee y genera
un documento .pdf del grafo.
