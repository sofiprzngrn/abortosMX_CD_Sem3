import pandas as pd
import seaborn as sns
import requests # http requests are the standard way of communicating with an API
import json #json is the normal way an API will respond

url = 'https://datos.cdmx.gob.mx/api/v2/catalog/datasets/interrupcion-legal-del-embarazo/exports/json'
response= requests.get(url)
datos = pd.read_json(response.content)

#datos = pd.read_csv('interrupcion-legal-del-embarazo.csv', low_memory=False)
'''
Estos son algunos comandos que utilicé para visualizar mis datos
'''
print(datos.shape)
print(datos.nunique())
print(datos.describe())
print(datos.describe().apply(lambda s: s.apply(lambda x: format(x, 'f'))))
print(datos.clues_hospital.unique())
print(datos.mes.unique())
print(datos.autoref.unique())
print(datos.edocivil_descripcion.unique())
print(datos.desc_derechohab.unique()) 
print(datos.nivel_edu.unique())
print(datos.ocupacion.unique())
print(datos.religion.unique()) 
print(datos.parentesco.unique())
print(datos.entidad.unique())
print(datos.alc_o_municipio.unique())
print(datos.consejeria.unique())
print(datos.anticonceptivo.unique())
print(datos.motiles.unique())
print(datos.p_consent.unique())
#print(datos.isna().sum())
#print(datos.motiles.isna().sum())
print('holaaaa\n\n\n')
'''
Aquí empiezo quitando algunas columnas y ciertos valores.
'''
print('holaaaa\n\n\n')

datos = datos.drop('fecha_cierre', axis=1)
datos = datos.drop('resultado_ile', axis=1)
datos = datos[(datos.menarca != 1218) & (datos.menarca != 147)& (datos.menarca != 123) & (datos.menarca != 121) & (datos.menarca != 113) & (datos.menarca != 99) & (datos.menarca != 88) & (datos.menarca != 58)]
print('holaaaa termine de borrar\n\n\n')

datos['c_fecha'] =  pd.to_datetime(datos['c_fecha'], format='%Y/%m/%d')
datos['h_fingreso'] =  pd.to_datetime(datos['h_fingreso'], format='%Y/%m/%d')
datos['h_fegreso'] =  pd.to_datetime(datos['h_fegreso'], format='%Y/%m/%d')
datos['fmenstrua'] =  pd.to_datetime(datos['fmenstrua'], format='%Y/%m/%d')
datos['fingreso'] =  pd.to_datetime(datos['fingreso'], format='%Y/%m/%d')
print('holaaaa termine fechas\n\n\n')

'''
Funciones para homogeneizar datos
'''

def clean_condition(row):# Funcion para homogeneizar los datos en religion
  
  ninguno = ['NINGU0','NINGUNA']
  cristiana = ['CRISTIANA','CRISTIA0']   
  
  if row.religion in ninguno:
    return 'NINGUNO'  
  if row.religion in cristiana:
    return 'CRISTIANA'    
  return row.religion# Limpiar el dataframe

  
def clean_df(datos):
  df_cleaned = datos.copy()
  df_cleaned['religion'] = df_cleaned.apply(lambda row: clean_condition(row), axis=1)
  return df_cleaned# obtener el dataframe con la columna 'religion' reclasificada
df_cleaned = clean_df(datos)
print(df_cleaned.religion.unique())

print(df_cleaned)

df_cleaned.to_csv('listo.csv')
