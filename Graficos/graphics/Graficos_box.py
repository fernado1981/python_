# muy útil para cálculos científicos con Python
import numpy as np
# Librería para estructar datos primarios
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

# opcional: para estilo tipo ggplot
mpl.style.use('ggplot')

# revisar la última versión de Matplotlib >= 2.0.0
print('Matplotlib version: ', mpl.__version__)

df_can = pd.read_excel(
    'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DV0101EN/labs/Data_Files/Canada.xlsx',
    sheet_name='Canada by Citizenship',
    skiprows=range(20),
    skipfooter=2
)

print('Data downloaded and read into a dataframe!')

print(df_can.head())

# imprimir el tamaño del DataFrame
print('Tamaño DataFrame:', df_can.shape)

# depurar el conjunto de datos para borrar columnas innecesarias (eg. REG)
df_can.drop(['AREA', 'REG', 'DEV', 'Type', 'Coverage'], axis=1, inplace=True)

# Cambiar el nombre de algunas columnas para que tengan sentido
df_can.rename(columns={'OdName': 'Country', 'AreaName': 'Continent', 'RegName': 'Region'}, inplace=True)

# Para tener consistencia, asegúrate de que todas las columnas sean del tipo cadena
df_can.columns = list(map(str, df_can.columns))

# Establece el nombre del país (country) como índice – muy útil para hacer búsquedas por países utilizando el método .loc
df_can.set_index('Country', inplace=True)

# Agrega un columna para el total
df_can['Total'] = df_can.sum(axis=1)

# años que usaremos – de utilidad para graficar mas adelante
years = list(map(str, range(1980, 2014)))
print('Tamaño DataFrame:', df_can.shape)

# para obtener el dataframe se colocan corchetes alrededor de Japan (Japón)
df_japan = df_can.loc[['Japan'], years].transpose()
print(df_japan.head())

# Paso 2: Dibujar la gráfica con kind='box'.
df_japan.plot(kind='box', figsize=(8, 6))

plt.title('Box plot of Japanese Immigrants from 1980 - 2013')
plt.ylabel('Number of Immigrants')

plt.show()

# Paso 3: describe
print(df_japan.describe())

# Paso 1: Obtener el conjunto de datos para China e India y llamar al dataframe df_CI.
df_CI = df_can.loc[['China', 'India'], years].transpose()
df_CI.head()

# Paso 2: describe
print(df_CI.describe())

# Paso 3: Graficamos vertical
df_CI.plot(kind='box', figsize=(8, 6))

plt.title('Box plot of Japanese Immigrants from 1980 - 2013')
plt.ylabel('Number of Immigrants')

plt.show()

# Paso 3: Graficamos horizontal
df_CI.plot(kind='box', figsize=(10, 7), color='blue', vert=False)

plt.title('Box plots of Immigrants from China and India (1980 - 2013)')
plt.xlabel('Number of Immigrants')

plt.show()

# crear imagen
fig = plt.figure()

ax0 = fig.add_subplot(1, 2, 1)  # añadir sub gráfica 1 (1 fila, 2 columnas, primer gráfica)
ax1 = fig.add_subplot(1, 2, 2)  # añadir sub gráfica 2 (1 fila, 2 columnas, segunda gráfica). Mirar tip mas abajo**

# Sub gráfica 1: Gráfica de Caja
df_CI.plot(kind='box', color='blue', vert=False, figsize=(20, 6), ax=ax0)  # añadir sub gráfica 1
ax0.set_title('Box Plots of Immigrants from China and India')
ax0.set_xlabel('Number of Immigrants')
ax0.set_ylabel('Countries')

# Sub gráfica 2: Gráfica de Línea
df_CI.plot(kind='line', figsize=(20, 6), ax=ax1)  # añadir sub gráfica 2
ax1.set_title('Line Plots (1980 - 2013)')
ax1.set_ylabel('Number of Immigrants')
ax1.set_xlabel('Years')

plt.show()

# identificamos los 15 principales paises en base a su inmigración total desde 1980 a 2013.
# Crea una gráfica de caja para visualizar la distribución de los 15 países principales (en base al total de inmigración) agrupados por las décadas 1980, 1990 y 2000.
# Paso 1: Obtener el conjunto de datos. Obtener los 15 primeros países en base al total de la poblacion inmigrante. Nombra al dataframe df_top15.

df_top15 = df_can.sort_values(['Total'], ascending=False, axis=0).head(15)
print(df_top15)

# Paso 2: Crea un nuevo dataframe el cual contenga el agregado de cada década. Una forma de hacerlo es:

# 1.- Crear una lista de todos los años separados por las decadas 80, 90 y 2000.
# 2.- Divide el dataframe original df_can para crear una serie para cada década y hacer la suma de todos los años para cada país.
# 3.- Juntar las tres series en un nuevo dataframe. Llama a este dataframe new_df.

years_80s = list(map(str, range(1980, 1990)))
years_90s = list(map(str, range(1990, 2000)))
years_00s = list(map(str, range(2000, 2010)))

# slice the original dataframe df_can to create a series for each decade
df_80s = df_top15.loc[:, years_80s].sum(axis=1)
df_90s = df_top15.loc[:, years_90s].sum(axis=1)
df_00s = df_top15.loc[:, years_00s].sum(axis=1)

# merge the three series into a new data frame
new_df = pd.DataFrame({'1980s': df_80s, '1990s': df_90s, '2000s': df_00s})

# display dataframe
print(new_df.head())

print(new_df.describe())

#Paso 3: Graficas
new_df.plot(kind='box', figsize=(10, 7), color='blue', vert=False)

plt.title('Box plots of Immigrants from China and India (1980 - 2013)')
plt.xlabel('Number of Immigrants')

plt.show()

#Observa como la gráfica de caja es distinta de la tabla resumida que se creó. La gráfica escanea los datos e identifica los que estan separados (outliers). Para reconocer un dato separado, su valor debe ser:

#mayor a Q3 por al menos 1.5 veces el rango intercuartil (IQR), o,
#mas pequeño que Q1 por la menos 1.5 veces IQR.
#Revisemos la decada del 2000 como ejemplo:

#Q1 (25%) = 36,101.5
#Q3 (75%) = 105,505.5
#IQR = Q3 - Q1 = 69,404
#Usando esto para definir datos atípicos (outliers), cualquier valor mayor a Q3 por 1.5 veces IQR tendra esta caracteristica.

#Outlier > 105,505.5 + (1.5 * 69,404)
#Outlier > 209,611.5
#Paso 4: comprobemos cuantas entradas caen en la definición de dato separado
print(new_df[new_df['2000s']> 209611.5])

#China e India se consideran atípicos debido a que su población para la década excede 209,611.5