import pandas as pd 
paath_file = './supermarket_sales.xlsx'
sheet = 'Sheet1'

df = pd.read_excel(paath_file, sheet_name=sheet)
data = df.to_dict(orient='records')

# contador = 0

idBuscar = '750-67-8428'
for registro in data:
    if registro['Invoice ID'] == idBuscar:
        print(registro)
        print('')
        # contador += 1