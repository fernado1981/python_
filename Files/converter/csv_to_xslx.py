import pandas as pd

read_file = pd.read_csv ('../asociacion.csv')
read_file.to_excel ('../aso.xlsx', index = None, header=True)