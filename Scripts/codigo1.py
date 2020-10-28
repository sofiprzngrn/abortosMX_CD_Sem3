
import pandas as pd
import seaborn as sns

datos = pd.read_csv('interrupcion-legal-del-embarazo.csv', low_memory=False) 

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



