import matplotlib.pyplot as plt
from pywaffle import Waffle

# exemplo de Waffle
fig = plt.figure(
    FigureClass=Waffle,
    rows=4,
    columns=10,
    values={'Bolacha': 33,
            'Biscoito': 48,
            'Salgadinho': 19},
    legend={'loc': 'upper left',
            'bbox_to_anchor': (1.1, 1)}
)

fig.set_tight_layout(False)
plt.show()
