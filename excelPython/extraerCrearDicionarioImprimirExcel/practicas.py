# import pandas as pd
# import json
# # -----------Cargar los datos de la hoja en un DataFrame
# # df = pd.read_excel('./pruebaPy1.xlsx', sheet_name='Hoja 1', usecols=['Nombre', 'Edad', 'Peso', 'Telefono'])

# # ----------# Convertir los datos en un diccionario
# # datos_dict = df.set_index('Nombre')[['Edad', 'Peso', 'Telefono']].to_dict('index')

# # # Imprimir el diccionario
# # print(datos_dict)




# # ------------Especificar el nombre de la hoja de Excel que contiene los datos


# -------------# Cargar los datos del archivo Excel en un DataFrame
# df = pd.read_excel('./Copia de supermarket_salesb (6).xlsx', sheet_name='Sheet1')

# -------------# Convertir los datos del DataFrame en un diccionario
# datos_dict = df.to_dict(orient='records')

# ------------# Imprimir el diccionario ordenado
# # print(json.dumps(datos_dict, indent=4, sort_keys=True))
# print(json.dumps(datos_dict, indent=4))
 
# import pandas as pd
# import json


# df = pd.read_excel('./Copia de supermarket_salesb (6).xlsx', sheet_name='Sheet1')
# datos_dict = df.to_dict(orient='records')
# print(json.dumps(datos_dict, indent=4))

import pandas as pd
import json
from datetime import datetime

# df = pd.read_excel('./supermarket_sales.xlsx', sheet_name='Sheet1')
df = pd.read_excel('./pruebaPy1.xlsx', sheet_name='Hoja 1')
email = pd.read_excel('./pruebaPy1.xlsx', sheet_name='Hoja 2')
datos_dict = df.to_dict(orient='records')

# ----------# Convertir las fechas a strings
# for registro in datos_dict:
#     registro['Date'] = registro['Date'].strftime('%Y-%m-%d')
#     registro['Time'] = registro['Time'].strftime('%H:%M:%S')

print(json.dumps(datos_dict, indent=4))
print(len(datos_dict))


persona_mayor_edad = None
edad_mayor = 0

for persona in datos_dict:
    if persona['Edad'] > edad_mayor:
        edad_mayor = persona['Edad']
        persona_mayor_edad = persona

print(f"La persona de mayor edad es {persona_mayor_edad['Nombre']} con {edad_mayor} años.")


 

 
 