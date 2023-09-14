# Empresas En Mora

> Este programa esta diseñado para calcular la cantidad de días en mora de diferentes empresas para cada uno de los años registrados en su base de datos.

Es un algoritmo diseñado en Python que recibe como entrada una base de datos en formato CSV y genera como salida otro archivo CSV con un listado de las empresas por cada año registrado, y la cantidad de días en mora que tuvieron en el respectivo año para cada mes.

## Uso del programa

Sigue los pasos que se mencionan a continuación para ejecutar el algoritmo en tu equipo:
1. Asegurate de tener un entorno de programación donde ejecutar el algoritmo de Python.
1. Descarga la carpeta del proyecto de GitHub.
1. En tu entorno de programación ejecuta el archivo llamado "*Dias_mora.py*"
1. Lee atentamente las indicaciones que aparecen en tu terminal.
1. Ingresa los datos solicitados de la siguiente manera:
- Ingresa la direccion del archivo CSV que se encuentra en tu equipo, donde están almacenadas las fechas de mora de las empresas a analizar, por ejemplo: 
    E:\Users\UserName\Downloads\Base_Datos.csv
- Ingresa la direccion de tu equipo donde deseas crear el archivo CSV de salida con el resultado de la operacion de la aplicación, y el nombre del archivo con extension ".csv" que deseas darle, por ejemplo, deseamos un archivo de salida llamado "Resultado.csv" en la carpeta "Downloads":
    E:\Users\UserName\Downloads\Resultado.csv
- Ingresa el número de la columna que contiene las fechas de inicio de la mora, contando las columnas de izquierda a derecha, iniciando el conteo con el número 0.
- Ingresa el número de la columna que contiene las fechas de finalización de la mora, contando las columnas de izquierda a derecha, iniciando el conteo con el número 0.

Despues de haber ingresado correctamente todos los datos solicitados, aparecerá en pantalla el nombre de cada una de las empresas analizadas, con los respectivos años evaluados, y la cantidad de fechas que se analizaron para cada una de ellas, ademas de generar un archivo CSV en la ubicacion indicada y con el nombre establecido, que contiene una tabla indicando la cantidad de días de mora de cada empresa, en cada año, para cada uno de los meses del año.


## Requerimientos mínimos del programa

Es importante tener en cuenta lo siguiente:
- El archivo de entrada siempre debe estar en formato CSV, y el de salida siempre debe ser formato CSV
- Las fechas de inicio y final de mora de las empresas deben estar en formato dd/mm/aaaa, no funcionará con formatos dd/mm/aa o diferentes al mencionado.
- La primera columna de la tabla siempre debe tener los nombres de las empresas.

------------


###### ¡Gracias por descargar y probar este algoritmo!