# Proyecto de Ciencia de Datos "Abortos en México"
Proyecto de ciencia de datos sobre abortos en México.
Este proyecto es para la materia de Ciencia de datos de la carrera de Actuaría en la IBERO.


## Estructura
- Scripts 
  - preprocesar_y_limpar.py
    > En este archivo se lee el dataset y se eliminan valores incorrectos y extremos.
  - generar_graficas.py
    > Con este archivo se generan las gráficas en seaborn
  - Interrupcion-legal-del-embarazo.csv
    > Archivo CSV sin procesar
  - listo.csv
    > Archivo CSV después de limpiar y procesar
- Documentación
  -Diccionario de datos ILE.csv
    > Diccionario con la explicación de cada variable original 
  -Documentación1.txt
    > Diccionario con las variables nuevas y procesadas
- Motivación
  > Documento detallando el propósito del proyecto


## Dependencias
Se utilizaron las siguientes librerías para el manejo de datos y visualización:

- Pandas
- Seaborn

Se instalan de la siguiente manera:

```bash
pip install pandas
```
```bash
pip install seaborn
```


## Uso
Después de instalar las dependencias se puede correr el primer programa. 
Es necesario estar en la carpeta del proyecto antes de ejecutar los programas
Primer programa **Scripts/preprocesar_y_limpiar.py**.
El primer programa limpia el dataset, es importante ejecutarlo primero.
Segundo programa **Scripts/generar_graficas.py**.
El segundo programa crea las graficas a partir de los datos procesados
```python
python3 preprocesar_y_limpiar.py
python3 generar_graficas.py
```

## Contributing
Este proyecto está hecho por Sofía Pereznegrón, cualquier comentario o sugerencia es bienvenida!

## Bibliografía

## Base consultada en:
https://datos.cdmx.gob.mx/explore/dataset/interrupcion-legal-del-embarazo/table/

## Diccionario consultado en:
https://data.opendatasoft.com/explore/dataset/interrupcion-legal-del-embarazo%40lab-cdmx/information/?refine.clues_hospital=DFSSA003932

Los datos fueron adquiridos de la página de datos abiertos de la Ciudad de México.
## Datos sobre hospitales consultados en:
http://www.amv.org.mx/asociacion-mexicana-de-vacunologia-directorio.php?estado=&_pagi_pg=244
https://www.gob.mx/cms/uploads/attachment/file/545458/df.pdf
