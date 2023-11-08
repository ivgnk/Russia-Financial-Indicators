'''
Input and visualisation from xlsx
Russia Monetary base in a broad definition
'''

import os
import numpy as np
import pandas as pd
from pandas.api.types import is_string_dtype
import matplotlib.pyplot as plt

the_title = 'Russia Monetary base in a broad definition'
new_col_name = ['Date', 'Monetary base (in a broad definition), billion rubles']

def print_row_col(dat: pd.DataFrame, title: str, view_head_tile: bool = False):
    print()
    print(title)
    print('num rows    = ', dat.shape[0]) #, ' ', dat.axes[0])
    print('num cols = ', dat.shape[1]) #, ' ', dat.axes[1])
    if view_head_tile:
        print(dat.head(7));        print(dat.tail(7))
    print()

#-(1) -- input
curr_dat_dir =  os.getcwd()
main_xls_fname = '2023-11-Russia Monetary base in a broad definition.xlsx'
mb_xlsx = pd.ExcelFile("\\".join([curr_dat_dir, main_xls_fname]))
mb_DataFrame = mb_xlsx.parse()

print_row_col(mb_DataFrame, 'before-'+the_title)

#-(2) -- Data selection and visualization
rows_end = list(range(350, 361))
mb_DataFrame = mb_DataFrame.drop(index=rows_end)  # удаление в конце строк
mb_DataFrame = mb_DataFrame.drop(index=[0, 1, 2, 3])  # удаление строк

# удаление столбцов
cols = np.array(range(2, 9))
mb_DataFrame.drop(mb_DataFrame.columns[cols], axis=1, inplace=True)

# Как переименовать столбцы в Pandas https://www.codecamp.ru/blog/pandas-rename-columns/
mb_DataFrame.columns = new_col_name

# сменить тип ячеек столбца на строку   https://stackoverflow.com/questions/15891038/change-column-type-in-pandas
mb_DataFrame[new_col_name[0]] = mb_DataFrame[new_col_name[0]].astype(str)
#  определить тип ячеек столбца https://stackoverflow.com/questions/22697773/how-to-check-the-dtype-of-a-column-in-python-pandas
# print("is_string_dtype 1 = ",is_string_dtype(mb_DataFrame[new_col_name[0]]))

# Как удалить ненужные части из строк в столбце Python DataFrame
# https://qaa-engineer.ru/kak-udalit-nenuzhnye-chasti-iz-strok-v-stolbcze-python-dataframe/
mb_DataFrame[new_col_name[0]] = mb_DataFrame[new_col_name[0]].str.replace('00:00:00', '')
mb_DataFrame[new_col_name[0]] = mb_DataFrame[new_col_name[0]].map(str.strip)

# сменить тип ячеек столбца со строкового на дату https://stackoverflow.com/questions/17134716/convert-dataframe-column-type-from-string-to-datetime
# mb_DataFrame[new_col_name[0]] = pd.to_datetime(mb_DataFrame[new_col_name[0]], format="%Y-%m-%d")
mb_DataFrame[new_col_name[0]] = pd.to_datetime(mb_DataFrame[new_col_name[0]], format="%Y-%m-%d")
# тип 1 ячейки столбца с датой вручную сменил на оставшийся

x = mb_DataFrame[new_col_name[0]]; y = mb_DataFrame[new_col_name[1]]

plt.subplots(figsize=(10, 8))
plt.title(the_title)
plt.plot(x,y)
plt.grid()
plt.show()
