
[Api_Post](READMEPOST.md) | [Api_Get](READMEGET.md)  | [Tuple_Set](READMETupleSet.md) | [lista_array](READMELIST.md) | [Diccionario](READMEDIC.md) | [Lectura y escritura de ficheros](files.md) | [numpy](numpy.md)


[Selenium](Selenium/README.md)


# Numpy
Es una biblioteca para crear vectores y matrices grandes multidimensionales, junto con una gran colección de funciones matemáticas de alto nivel para operar con ellas.

### importar numpy:
    import numpy as np

### convertir una lista a un arreglo numpy:
    import numpy as np
    a=np.array([1,2,3,4,5])
    
### type(), obtiene el tipo <numpy.ndarray>:
    type(a)
    
### dtype, obtener el tipo de datos del arreglo:
    a.dtype
    
### mean(), obtener la media del arreglo:
    mean_a=a.mean()
    mean_a
  
## CREAR y TRAZAR FUNCIONES:
### crear un vector con cuatro puntos equidistanciados, desde 0 hasta 2:
    np.linspace(0,2,4)

### crear la funcion y=sin(x)+2 , uando la matriz numpy x
    x=np.linspace(0.2*np.pi,100)
    y=np.sin(x)
    
### matplotlib.pylot, Trazar la solucion:
    import matplotlib.pylot as plt
    %matplotlib inline
    plt.plot(x,y)
