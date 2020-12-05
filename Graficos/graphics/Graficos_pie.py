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

# agrupar los países por continente y aplicar la función sum()
df_continents = df_can.groupby('Continent', axis=0).sum()

# observación: la salida del método groupby es un objeto `groupby'
# no podemos usarla hasta que se aplique una función (p. ej. .sum())
print('Es de tipo:', type(df_can.groupby('Continent', axis=0)))
print(df_continents.head())

# autopct crea %, el angulo de inicio representa el punto de inicio
df_continents['Total'].plot(kind='pie', figsize=(5, 6), # el pastel tiene aspecto circular
                            autopct='%1.1f%%', # añade en porcentajes
                            startangle=90,     # angulo de inicio 90° (Africa)
                            shadow=True,       # añade sombreado
                            )
plt.title('Immigration to Canada by Continent [1980 - 2013]')
plt.axis('equal')
plt.show()

#Ajuste para mejor visualizacion
colors_list = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'lightgreen', 'pink']
# la relacion para cada continente para compensar cada parte del pastel.
explode_list = [0.1, 0, 0, 0, 0.1, 0.1]

df_continents['Total'].plot(kind='pie',
                            figsize=(15, 6),
                            autopct='%1.1f%%',
                            startangle=90,
                            shadow=True,
                            labels=None,         # deshabilita las etiquetas de la gráfica
                            pctdistance=1.12,    # la relación entre el centro de cada trozo del pastel y el inicio del texto generado por autopct
                            colors=colors_list,  # añadir colores personalizados
                            explode=explode_list # 'explota' los últimos tres continentes
                            )

# escala el título un 12% para igualar pctdistance
plt.title('Immigration to Canada by Continent [1980 - 2013]', y=1.12)

plt.axis('equal')

# añade etiqueta
plt.legend(labels=df_continents.index, loc='upper left')

plt.show()
