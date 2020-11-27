import pandas as pd
import seaborn as sns
# import requests # http requests are the standard way of communicating with an API
# import json #json is the normal way an API will respond

# url = 'https://datos.cdmx.gob.mx/api/v2/catalog/datasets/interrupcion-legal-del-embarazo/exports/json'
# response= requests.get(url)
# datos = pd.read_json(response.content)

datos = pd.read_csv('interrupcion-legal-del-embarazo.csv', low_memory=False)
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
print(datos.isna().sum())
print(datos.motiles.isna().sum())
'''
Aquí empiezo quitando algunas columnas y ciertos valores.
'''

datos = datos.drop('fecha_cierre', axis=1)
datos = datos.drop('resultado_ile', axis=1)
datos = datos[(datos.menarca != 1218) & (datos.menarca != 147)& (datos.menarca != 123) & (datos.menarca != 121) & (datos.menarca != 113) & (datos.menarca != 99) & (datos.menarca != 88) & (datos.menarca != 58)]
datos = datos[(datos.fsexual != 128) & (datos.fsexual != 55)]
datos['tot_abortos'] = datos['naborto'] + datos['nile']

datos['c_fecha'] =  pd.to_datetime(datos['c_fecha'], format='%Y/%m/%d')
datos['h_fingreso'] =  pd.to_datetime(datos['h_fingreso'], format='%Y/%m/%d')
datos['h_fegreso'] =  pd.to_datetime(datos['h_fegreso'], format='%Y/%m/%d')
datos['fmenstrua'] =  pd.to_datetime(datos['fmenstrua'], format='%Y/%m/%d')
datos['fingreso'] =  pd.to_datetime(datos['fingreso'], format='%Y/%m/%d')

datos = datos.replace(to_replace='DIVORCIADA',value='SEPARADA')
datos = datos.replace(to_replace='NINGU0',value='NINGUNO')
datos = datos.replace(to_replace='NINGUNA',value='NINGUNO')
datos = datos.replace(to_replace='CRISTIA0',value='CRISTIANA')
print(datos.religion.unique())


datos.to_csv('listo.csv')
