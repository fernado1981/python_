# importamos figurecanvas
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
# importamos Figure artist
from matplotlib.figure import Figure

fig = Figure()
canvas = FigureCanvas(fig)

# creamos un random de 10000 numeros usando numpy
import numpy as np

x = np.random.randn(10000)
# creamos axes artist (1 columna, 1 fila 1º celda)
ax = fig.add_subplot(111)
# creamos histograma de 10000 numeros
ax.hist(x, 100)
# añadimos el titulo y la salvamos
ax.set_title('Normal distribution with $\mu=0, \sigma=1$')
fig.savefig('matplotlib_histogram.png')
