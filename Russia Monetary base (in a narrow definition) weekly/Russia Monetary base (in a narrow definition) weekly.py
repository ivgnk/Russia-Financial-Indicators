'''
Input and visualisation from xlsx
Russia Monetary base (in a narrow definition) weekly
'''

import pandas as pd
import matplotlib.pyplot as plt

the_title = 'Russia Monetary base (in a narrow definition) weekly'

def print_row_col(dat: pd.DataFrame, title: str, view_head_tile: bool = False):
    print()
    print(title)
    print('num rows    = ', dat.shape[0]) #, ' ', dat.axes[0])
    print('num cols = ', dat.shape[1]) #, ' ', dat.axes[1])
    if view_head_tile:
        print(dat.head(7));        print(dat.tail(7))
    print()

#-(1) -- input
main_xls_fname = the_title+'.xlsx'
mb_DataFrame = pd.read_excel(main_xls_fname, sheet_name='Data')
print_row_col(mb_DataFrame, 'before-'+the_title, True)
print(mb_DataFrame.columns)

#-(2) -- columns name
print('col1 = ', mb_DataFrame.columns[0])
print('col2 = ', mb_DataFrame.columns[1])
col_name = [mb_DataFrame.columns[0], mb_DataFrame.columns[1]]
#-(3) -- 1 col to date
mb_DataFrame[col_name[0]] = mb_DataFrame[col_name[0]].astype(str)
# сменить тип ячеек столбца со строкового на дату https://stackoverflow.com/questions/17134716/convert-dataframe-column-type-from-string-to-datetime
mb_DataFrame[col_name[0]] = pd.to_datetime(mb_DataFrame[col_name[0]], format="%Y-%m-%d")
x = mb_DataFrame[col_name[0]]
y = mb_DataFrame[col_name[1]]

fig, ax = plt.subplots(figsize=(10, 8))
plt.title(the_title)
plt.plot(x,y)
plt.xlabel(col_name[0]); plt.ylabel(col_name[1])
plt.grid()
plt.show()