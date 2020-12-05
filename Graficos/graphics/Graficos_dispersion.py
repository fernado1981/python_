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

# Paso 1: Obtener el conjunto de datos. Debido a que esperamos usar la relación entre años y población total, convertiremos años a tipo int.
# podemos usar el método sum() para obtner la población total anual
df_tot = pd.DataFrame(df_can[years].sum(axis=0))

# cmabiar los años a tipo entero (será util para hacer regresión mas adelante)
df_tot.index = map(int, df_tot.index)

# establecer de nuevo el índice para regresarlas a columnas en el dataframe df_tot
df_tot.reset_index(inplace=True)

# renombrar las columnas
df_tot.columns = ['year', 'total']

# ver el dataframe final
print(df_tot.head())

# Paso 2: Dibujar los datos. En Matplotlib podemos crear gráficos de dispersión pasando kind='scatter' como argumento. También necesitaremos pasar x y y para especificar las columnas que iran en los ejes x e y.

df_tot.plot(kind='scatter', x='year', y='total', figsize=(10, 6), color='darkblue')

plt.title('Total Immigration to Canada from 1980 - 2013')
plt.xlabel('Year')
plt.ylabel('Number of Immigrants')

plt.show()


#Observa como la gráfica de dispersión no conecta los datos entre si. Podemos obervar con facilidad un tendencia positiva en los datos: a medida que pasan los años, el número total de inmigrantes asciende. Podemos analizar matematicamente esta tendencia positiva usando una línea de regresión.
#Tratemos de gráficar una línea de regresión y utilizarla para predecir el numero de inmigrantes en 2015.
#Paso 1: Obtener la ecuación de la línea. Usaremos el método polyfit() de Numpy pasando lo siguiente:
#x: coordenadas x de los datos
#y: coordenadas y de los datos
#deg: Grados polinomiales. 1 = lineal, 2 = cuadrática, etc ..
x = df_tot['year']      # año en el eje x
y = df_tot['total']     # total en el eje y
fit = np.polyfit(x, y, deg=1)

print(fit)

#La salida es un arreglo con los coeficientes polinomiales, las potencias mas grandes primero. Debido a que estamos graficando una regresión lineal y= a*x + b, la salida tiene 2 elementos [5.56709228e+03, -1.09261952e+07] con la pendiente en 0 y la intercepción en 1.
#Paso 2: Gráficar la regresión lineal en la gráfica de dispersión.
df_tot.plot(kind='scatter', x='year', y='total', figsize=(10, 6), color='darkblue')

plt.title('Total Immigration to Canada from 1980 - 2013')
plt.xlabel('Year')
plt.ylabel('Number of Immigrants')

# dibujar línea de regresión
# recuerda que x son los Años
plt.plot(x, fit[0] * x + fit[1], color='red')
plt.annotate('y={0:.0f} x + {1:.0f}'.format(fit[0], fit[1]), xy=(2000, 150000))

plt.show()

# imprimir la línea optima
print('No. Immigrants = {0:.0f} * Year + {1:.0f}'.format(fit[0], fit[1]))