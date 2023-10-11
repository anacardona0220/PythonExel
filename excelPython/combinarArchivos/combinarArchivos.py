import pandas as pd 

hoja1 = pd.read_excel('./pruebaPy1.xlsx', sheet_name='Hoja 1')
hoja2 = pd.read_excel('./pruebaPy1.xlsx', sheet_name='Hoja 2')

valuesUnidos1 = hoja1[['Nombre', 'Edad', 'Peso', 'telefono']]
valuesUnidos2 = hoja1[['email']]

dataframes = [valuesUnidos1, valuesUnidos2]

 
print(dataframes)