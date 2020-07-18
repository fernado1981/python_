from ArticulosTienda import ArticulosTienda


# Escribir un programa que cree un diccionario simulando una cesta de la compra.
# El programa debe preguntar el artículo y su precio y añadir el par al diccionario,
# hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra
# y el coste total, con el siguiente formato

class CompraArticuloTienda:
    compra = True

    compras = ArticulosTienda(compra)
    compras.compraArticulo()
    compras.verPrecio()
