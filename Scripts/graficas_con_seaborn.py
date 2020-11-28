import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

#sns.set_theme()

df = pd.read_csv('listo.csv', low_memory=False)

def se_cuido(s):
    if (s['anticonceptivo'] == 'NINGUNO'):
        return 'No'
    elif (s['anticonceptivo'] ==""):
        return 'NA'
    else:
        return 'Si'

def ordenar_nived(s):
    if (s['nivel_edu'] == 'NA'):
        return -1
    if (s['nivel_edu'] == 'SIN ACCESO A LA EDUCACION FORMAL'):
        return 0
    if (s['nivel_edu'] == 'PRIMARIA'):
        return 1
    if (s['nivel_edu'] == 'SECUNDARIA'):
        return 2
    if (s['nivel_edu'] == 'PREPARATORIA'):
        return 3
    if (s['nivel_edu'] == 'LICENCIATURA'):
        return 4
    if (s['nivel_edu'] == 'MAESTRIA'):
        return 5
    if (s['nivel_edu'] == 'DOCTORADO'):
        return 6

def ordenar_edociv(s):
    if (s['edocivil_descripcion']==""):
        return -1
    if (s['edocivil_descripcion'] == 'SOLTERA'):
        return 0
    if (s['edocivil_descripcion'] == 'UNION LIBRE'):
        return 1
    if (s['edocivil_descripcion'] == 'CASADA'):
        return 2
    if (s['edocivil_descripcion'] == 'SEPARADA'):
        return 3
    if (s['edocivil_descripcion'] == 'VIUDA'):
        return 4


df['uso_anticon'] = df.apply(se_cuido, axis=1)
df['nivel_edu_num'] = df.apply(ordenar_nived, axis=1)
df['edocivil_num'] = df.apply(ordenar_edociv,axis=1)
sns.jointplot(data=df, x="edocivil_num", y="nivel_edu_num", hue="uso_anticon")
sns.jointplot(data=df, x="sememb", y="nivel_edu_num", hue="uso_anticon")

df = df[df.procile!= 'LEGRADO']
g = sns.catplot(x="edocivil_descripcion", y="fsexual",hue="nivel_edu", col="procile", data=df, kind="box", height=11, aspect=.8)

sns.set_theme()
sns.jointplot(data=df, x= "c_num",y ="tot_abortos" ,hue="edad")


plt.show()
