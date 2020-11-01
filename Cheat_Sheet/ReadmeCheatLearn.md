# la librería scikit-learn para implementar regresión lineal simple:
## Descargaremos un set de datos relacionado al consumo de combustible y a la emisión del dióxido de Carbono en autos. Luego, separaremos nuestros datos en un set de entrenamiento y en otro set de prueba, crearemos un modelo utilizando un set de entrenamiento, se evaluará utilizando el set de prueba para finalmente usar el modelo para predecir valores desconocidos
### Importando paquetes Necesarios:

    import matplotlib.pyplot as plt
    import pandas as pd
    import pylab as pl
    import numpy as np
    %matplotlib inline

### Descargando los Datos:
### Para descargar los datos, usaremos !wget desde IBM Object Storage.

  !wget -O FuelConsumption.csv https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/ML0101ENv3/labs/FuelConsumptionCo2.csv
