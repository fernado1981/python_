# Visualizacion de datos
### Tipo de gráficos:
1) Gráfico de área
2) Gráfico de histogramas
3) Gráficos de barras
4) Gráficos bar_chart

#### Gráfico de área:
Los gráficos de área se utilizan para mostrar el desarrollo de valores cuantitativos a lo largo de un intervalo o período de tiempo.
<br/>Ejemplo:<br/>
##### Importamos las librerías necesarias:

    import matplotlib as mpl
    import matplotlib.pyplot as plt
    import numpy as np  # muy útil para cálculos científicos con Python
    import pandas as pd # Librería para estructar datos primarios
    
##### Obtenemos el dataset deprueba (como se puede observar es de tipo excel):
    
    df_can = pd.read_excel('https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-   data/CognitiveClass/DV0101EN/labs/Data_Files/Canada.xlsx',
                       sheet_name='Canada by Citizenship',
                       skiprows=range(20),
                       skipfooter=2
                      )

    print('Data downloaded and read into a dataframe!')

![React](../Images/data_set_bruto.png)

##### Cambiamos los indices por country y añadimos la columna total:
    
    df_can.set_index('Country', inplace=True)
    df_can.head()

    df_can['Total'] = df_can.sum(axis=1)
    df_can.head()

![React](../Images/data_set_modificado.png)

#### Generación de area plot
##### Obtenemos la lista de años dese 1980 a 2014
     
     years = list(map(str,range(1980,2014)))
     
##### Ordenadmos los datos de la columna total, sort_values()

    df_canada.sort_values(['Total'], ascending=False, axis=0, inplace=True)
    
![React](../Images/data_set_limpio.png)
    
##### Obtenemos los cinco primeros valores, head()

    df_top5= df_canada.head()
    df_top5.head()
    # cambiar el valor de los índices de df_top5 a tipo entero para graficarlos
    df_top5.index = df_top5.index.map(int)
    # generamos el tipo de gráfico
    df_top5.plot(kind='area', 
             alpha=0.25,   #0-1, valor por defecto a 0.5
             stacked=False,   #Para crear una grafica no apilada estableceremos stacked=False.
             figsize=(20, 10), # pasar el tamaño de tupla (x, y)
             )
##### Pintamos el gráfico y lo mostramos

    plt.title('Immigration Trend of Top 5 Countries')
    plt.ylabel('Number of Immigrants')
    plt.xlabel('Years')

    plt.show()
    
![React](../Images/gráfico_area.png)
    



