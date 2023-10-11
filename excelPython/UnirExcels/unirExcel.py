import pandas as pd
import glob
import openpyxl
from tkinter import filedialog


folder_selected = filedialog.askdirectory()
if not folder_selected:
    exit()
    
print(folder_selected)


files_list = glob.glob(folder_selected + "/*.xlsx")
excel_list = []

for file in files_list:
    excel_list.append(pd.read_excel(file))
    



exel_merged = pd.DataFrame()

for exel_file in excel_list:
    exel_merged = pd.concat([exel_merged, pd.DataFrame.from_records(exel_file)], ignore_index= False)
    
exel_merged.to_excel("consolidated_file.xlsx")

# Listar contenido
for index, l in enumerate(excel_list):
    print(index, l)



fdf