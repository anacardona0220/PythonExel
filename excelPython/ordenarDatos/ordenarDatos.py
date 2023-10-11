import pandas as pd
from openpyxl import load_workbook
import json
from datetime import datetime

fileExcel = pd.read_excel('./supermarket_sales.xlsx', sheet_name='Sheet1')
data = fileExcel.to_dict(orient='records')

data = sorted(data, key=lambda x: x['Total'], reverse=True)
# ----------# Convertir las fechas a strings
for registro in data:
    registro['Date'] = registro['Date'].strftime('%Y-%m-%d')
    registro['Time'] = registro['Time'].strftime('%H:%M:%S')

contador = 0 
for registro in data:
    # Imprimir los campos 'Invoice ID', 'Product line' y 'Total'
    
    if contador < 2:
        
        print('Invoice ID:', registro['Invoice ID'])
        print('Product line:', registro['Product line'])
        print('Total:', registro['Total'])
        print('//-----------------//')
        contador += 1
# print(archivo_excel[['Gender', 'Product line', 'Total']])
# def sort_item(sheet):
#     return(sheet[1])
 
# sheet.sort(keys=sort_item)
# print(sheet)



# for data in sheet.iter_rows(max_row=10):
#     print(data[0].value, data[1].value, data[2].value)
    
     
    
     
 