import pandas as pd
import matplotlib.pyplot as plt
from pywaffle import Waffle

# creation of a dataframe
data = {'phone': ['Xiaomi', 'Samsung',
                  'Apple', 'Nokia', 'Realme'],
        'stock': [44, 12, 8, 5, 3]
        }

df = pd.DataFrame(data)

# To plot the waffle Chart
fig = plt.figure(
    FigureClass=Waffle,
    rows=5,
    values=df.stock,
    labels=list(df.phone)
)
plt.show()