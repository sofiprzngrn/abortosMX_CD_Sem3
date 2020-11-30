# Proyecto de Ciencia de Datos "Abortos en México"
Proyecto de ciencia de datos sobre abortos en la Ciudad de México.
Este proyecto es para la materia de Ciencia de datos de la carrera de Actuaría en la IBERO. 
Se utilizó Python para hacer la limpieza del data set y la librería de Seaborn para graficar, de igualmanera se utilizó la plataforma de Tableau para visualizar los datos.

Si desea ver el reporte de este proyecto, este se encuentra en la carpeta de documentación, lo podrá encontrar con el nombre de Abortos_CDMX_Reporte_Final.pdf

## Estructura
- Scripts 
  - preprocesar_y_limpar.py
    > En este archivo se lee el dataset y se eliminan y valores incorrectos y extremos.
  - generar_graficas.py
    > Este archivo muestra el código en pyhton de como generar las gráficas de este proyecto en seaborn.
  - Interrupcion-legal-del-embarazo.csv
    > Archivo CSV sin procesar.
  - listo.csv
    > Archivo CSV después de limpiar y procesar.
- Documentación
  - Abortos_CDMX_Reporte_Final.pdf
    > Documento que recoge la esencia del proyecto, resultados y conclusiones finales.
  - Diccionario de datos ILE.csv
    > Diccionario con la explicación de cada variable original.
  - Documentación1.txt
    > Diccionario con las variables nuevas y procesadas.
- Graficas
  > En este folder se encuentran las gráficas resultantes del análisis.
- Motivación
  > Documento detallando el propósito del proyecto.

## Lenguaje de programación
- python 3.8.3

Para información sobre como instalarlo visite:
https://realpython.com/installing-python/

## Dependencias
Se utilizaron las siguientes librerías para el manejo de datos y visualización:

- Pandas 1.0.5
- Seaborn 0.11.0
- Matplotlib 3.2.2
- Requests 2.24.0


Se instalan de la siguiente manera:

```bash
pip install pandas
```
```bash
pip install seaborn
```
```bash
python -m pip install -U matplotlib
```
```bash
py -m pip install requests
```
## Uso
Después de instalar las dependencias se puede correr el primer programa. 
Es necesario estar en la carpeta del proyecto antes de ejecutar los programas.

Primer programa **Scripts/preprocesar_y_limpiar.py**.
El primer programa limpia el dataset y automáticamente genera el archivo 'listo.csv' que se guarda en la misma carpeta en donde se corre. Es importante ejecutarlo primero.

Segundo programa **Scripts/generar_graficas.py**.
El segundo programa crea las graficas a partir de los datos procesados.
```python
python3 preprocesar_y_limpiar.py
python3 generar_graficas.py
```

## Contributing
Este proyecto está hecho por Sofía Pereznegrón, cualquier comentario o sugerencia es bienvenida!

## Referencias bibliográficas
Documentación de Pandas
https://pandas.pydata.org/docs/user_guide/index.html#user-guide

Documentación de Seaborn
https://seaborn.pydata.org/tutorial.html

Documentación de Matplotlib
https://matplotlib.org/

Documentación de Tableau
https://help.tableau.com/current/pro/desktop/en-us/gettingstarted_overview.htm


## Base consultada en:
https://datos.cdmx.gob.mx/explore/dataset/interrupcion-legal-del-embarazo/table/

Los datos fueron adquiridos de la página de datos abiertos de la Ciudad de México.

## Diccionario consultado en:
https://data.opendatasoft.com/explore/dataset/interrupcion-legal-del-embarazo%40lab-cdmx/information/?refine.clues_hospital=DFSSA003932

## Datos sobre hospitales consultados en:
http://www.amv.org.mx/asociacion-mexicana-de-vacunologia-directorio.php?estado=&_pagi_pg=244
https://www.gob.mx/cms/uploads/attachment/file/545458/df.pdf
