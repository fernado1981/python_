# muy útil para cálculos científicos con Python
import inline
import matplotlib
import numpy as np
# Librería para estructar datos primarios
import pandas as pd

# read_excel(), para esxtraer datos del excel, necesario instalar el módulo pip3 install xlrd
df_can = pd.read_excel(
    'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DV0101EN/labs/Data_Files/Canada.xlsx',
    sheet_name='Canada by Citizenship',
    skiprows=range(20),
    skipfooter=2)

print('Data read into a pandas dataframe!')

# leemos las 5 primeras lineasd para asegurarnos de que tenemos los datos descargados en df_can
print(df_can.head())

# leemos las ultimas 5 lineas del fichero
print(df_can.tail())

# obteniendo información básica sobre tu dataframe.
# print(df_can.info())

# obtener la lista de las cabeceras de las columnas
print(df_can.columns.values)

# obtener una lista de los índices
print(df_can.index.values)

# El tipo de dato
print(type(df_can.columns))
print(type(df_can.index))

# obtener los índices y columnas como tipo lista (list), usar el método tolist()
df_can.columns.tolist()
df_can.index.tolist()

print(type(df_can.columns.tolist()))
print(type(df_can.index.tolist()))

# ver las dimensiones del dataframe
print(df_can.shape)

# Nota: Los tipos principales almacenados en objetos pandas son float, int, bool, datetime64[ns] y datetime64[ns, tz] (in >= 0.17.0), timedelta[ns], category (in >= 0.15.0), y object. Además estos tipos de datos posen tamaño, por ejemplo int64 and int32.
# Limpiemos el conjunto de datos para retirar columnas innecesarias, usar drop()
df_can.drop(['AREA', 'REG', 'DEV', 'Type', 'Coverage'], axis=1, inplace=True)
print(df_can.head(2))

# Renombremos las columnas para que tengan sentido. Podemos usar el método rename(),
# pasándole un diccionario con nombres viejos y nuevos de la siguiente manera:
df_can.rename(columns={'OdName': 'Country', 'AreaName': 'Continent', 'RegName': 'Region'}, inplace=True)
print(df_can.columns)

# añadir una columna 'Total' para el numero total de inmigrantes por país a lo largo del periodo 1980 – 2013:
df_can['Total'] = df_can.sum(axis=1)

# revisar cuantos objetos vacíos (null) tenemos en el conjunto de datos
print("objetos vacios: ", df_can.isnull().sum())

# veamos un resumen rápido de cada columna en nuestro dataframe
print(df_can.describe())

# Indexado y Selección (slicing)
# Seleccionar Columna
# Hay dos maneras de filtrar por el nombre de una columna:
# Método 1: Rápido y fácil, pero solo funcionará si el nombre de la columna NO tiene caracteres especiales o espacios.
# df.column_name
# (returns series)
# Método 2: Es mas robusto y puede filtrar múltiples columnas.
# df['column']
# (returns series)
# df[['column 1', 'column 2']]
# (returns dataframe)

# filtro en la lista de países ('Country').
print(df_can.Country)

# filtrar en la lista de países ('OdName') y en los datos para los años 1980 – 1985.
print(df_can[['Country', 1980, 1981, 1982, 1983, 1984, 1985]])

# Seleccionar Fila
# Existen tres formas principales para seleccionar filas:
# df.loc[label]
# #filtra por la etiqueta del índice/columna
# df.iloc[index]
# #filtra por la posición del índice/columna

# estableciendo la columna 'Country' como índice
df_can.set_index('Country', inplace=True)
print(df_can.head(3))

# opcional: remueve el nombre del índice
df_can.index.name = None

# 1. El total de filas de datos (todas las columnas)
print(df_can.loc['Japan'])

# métodos alternativos
print(df_can.iloc[87])
print(df_can[df_can.index == 'Japan'].T.squeeze())

# 2. Para el año 2013
print(df_can.loc['Japan', 2013])

# método alternativo
# el año 2013 esta en la ultima columna con una posición de índice de 36
print(df_can.iloc[87, 36])

# 3. Para los años 1980 a 1985
print(df_can.loc['Japan', [1980, 1981, 1982, 1983, 1984, 1984]])
print(df_can.iloc[87, [3, 4, 5, 6, 7, 8]])

# NOTA: Los nombres de las columnas que son enteros (como las de los años) puede provocar cierta confusión. Por ejemplo, cuando hacemos referencia al año 2013 uno pudiera confundirlo con la posición 2013 del índice.
# Para evitar esta ambigüedad, vamos a convertir los nombres de las columnas a tipo cadena: '1980' a '2013'.

df_can.columns = list(map(str, df_can.columns))
# [print (type(x)) for x in df_can.columns.values] #<-- retirar el código comentado para revisar el tipo de dato de las cabeceras de las columnas
# Dado a que convertimos los años a tipo cadena, declaremos una variable que nos permita fácilmente hacer una llamada al rango completo de años:
# de utilidad para graficar mas adelante
years = list(map(str, range(1980, 2014)))
print(years)

# Filtrado basado en Criterios
# Para filtrar un dataframe en base a una condición implemente debemos pasar la condición como vector boleano.
# Por ejemplo, filtremos el dataframe para mostrar los datos acerca de los países asiáticos (AreaName = Asia).
# 1. crear las series de condiciones boleanas
condition = df_can['Continent'] == 'Asia'
print(condition)

# 2. pasar al dataframe esta condición
df_can[condition]

# Podemos pasar múltiples condiciones en la misma línea
# filtremos por AreaNAme = Asia y RegName = Southern Asia
condition = df_can[(df_can['Continent'] == 'Asia') & (df_can['Region'] == 'Southern Asia')]
print(condition)

# revisemos los cambios que hemos hecho en el dataframe
print('data dimensions:', df_can.shape)
print(df_can.columns)
print(df_can.head(2))

# Visualizar Datos con Matplotlib
# Matplotlib: Librería Estándar de Visualización para Python
# importacion de Matplotlib y Matplotlib.pyplot:

import matplotlib as mpl
import matplotlib.pyplot as plt

# revisar si Matplotlib esta cargado.
print('Matplotlib version: ', mpl.__version__)

# aplicar un estilo a Matplotlib
print(plt.style.available)
# opcional: para el estilo tipo ggplot
mpl.style.use(['ggplot'])

#Graficar con pandas
#Afortunadamente pandas tiene una implementación pre cargada de Matplotlib que podemos usar. Graficar en pandas es tan simple como añadir un método .plot() a una serie o dataframe.

#Gráficas de Líneas (Series/Dataframe)
#¿Qué es una grafica de línea y para que se usa?
#Una grafica de línea muestra información como una seria de puntos de datos llamados 'marcadores' conectados por segmentos de líneas rectas.
#Empecemos con un caso de estudio:
#En 2010 Haití sufrió un terremoto catastrófico de 7.0 grados de magnitud. Esto causo devastación y perdidas de vida en grandes áreas y afectando alrededor de tres millones de personas. Como parte de los esfuerzos humanitarios por parte de Canadá, el gobierno acepto refugiados provenientes de Haití. Podemos visualizar rápidamente este esfuerzo con el uso de una grafica de Línea:
#Pregunta: Dibuja una Grafica de Línea de la inmigración proveniente de Haití usando df.plot().
#Primero, extraeremos la serie de datos de Haití.

# ejecución en los años 1980 a 2013 para excluir la columna 'total'
haiti = df_can.loc['Haiti', years]
print(haiti.head())

#dibujaremos una grafica de línea anexando .plot() al dataframe haiti
haiti.plot()
plt.show()

#pandas completó automáticamente el eje x con los valores de los índices (años) y el eje y con los valores de las columnas (población). Sin embargo, observe que los años no se mostraron porque son del tipo cadena. Por lo tanto, modifiquemos el tipo de los valores de índice a entero para su diagramación.
#Además, etiquetemos el eje x y el eje y con plt.title(), plt.ylabel() y plt.xlabel() de la manera siguiente:

# cambiemos los valores de índice de Haiti al tipo entero para la graficación
haiti.index = haiti.index.map(int)
haiti.plot(kind='line')

plt.title('Immigration from Haiti')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')

plt.show()

#Podemos observar con claridad la mayor cantidad de inmigrantes desde Haití a partir de 2010, año en que Canadá aumentó sus esfuerzos para aceptar refugiados haitianos. Anotemos este pico en el diagrama con el método plt.text()
haiti.plot(kind='line')

plt.title('Immigration from Haiti')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')

# anotar el terremoto de 2010.
# sintaxis: plt.text(x, y, label)
plt.text(2000, 6000, '2010 Earthquake')

plt.show()

#paso1: conjunto de datos para China e India, y muestre el DataFrame.
df_CI = df_can.loc[['India', 'China'], years]
df_CI.head()

#Paso 2: Dibuje el gráfico.
#transponer el DataFrame con el método transpose() a fin de intercambiar la fila y las columnas.
df_CI = df_CI.transpose()
df_CI.head()

#pandas creará automáticamente un gráfico con los dos países. Grafique el nuevo DataFrame transpuesto. Asegúrese de agregar un título al diagrama y de etiquetar los ejes.
df_CI.index = df_CI.index.map(int) # let's change the index values of df_CI to type integer for plotting
df_CI.plot(kind='line')
plt.title('Immigrants from China and India')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')
plt.show()

#A partir de la grafica anterior, podemos observar que China e India tienen tendencias inmigratorias muy similares a lo largo de los años.
#Nota: ¿Por qué no tuvimos que transponer el DataFrame de Haití antes de diagramarlo (como hicimos con df_CI)? did for df_CI)?
#Porque haiti es una serie, en lugar de un DataFrame, y los años son sus índices, como se muestra debajo.
print(type(haiti))
print(haiti.head(5))

#El gráfico de líneas es una herramienta práctica para mostrar varias variables dependientes contra una variable independiente. Sin embargo, no se recomiendan más de 5 a 10 líneas por gráfico. Si hay más líneas, se hace difícil interpretar el gráfico.
#Pregunta: Compara la tendencia de los 5 países principales que aportaron la mayor cantidad de inmigrantes a Canadá.
# Step 1: Get the dataset. Recall that we created a Total column that calculates the cumulative immigration by country. \\ We will sort on this column to get our top 5 countries using pandas sort_values() method.

df_can.sort_values(by='Total', ascending=False, axis=0, inplace=True)

# get the top 5 entries
df_top5 = df_can.head(5)

# transpose the dataframe
df_top5 = df_top5[years].transpose()

print(df_top5)

# Step 2: Plot the dataframe. To make the plot more readeable, we will change the size using the `figsize` parameter.
df_top5.index = df_top5.index.map(int) # let's change the index values of df_top5 to type integer for plotting
df_top5.plot(kind='line', figsize=(14, 8)) # pass a tuple (x, y) size

plt.title('Immigration Trend of Top 5 Countries')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')

plt.show()

#Tipos de gráficos:_
#bar para diagramas de barras verticales
#barh para diagramas de barras horizontales
#hist para histograma
#box para diagrama de caja
#kde o density para diagramas de densidad
#area para diagramas de área
#pie para diagramas circulares (de pastel)
#scatter para diagramas de dispersión
#hexbin para diagramas con agrupamiento hexagonal