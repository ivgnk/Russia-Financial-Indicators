'''
Data from https://mfd.ru/centrobank/preciousmetals/
https://mfd.ru/centrobank/preciousmetals/?left=0&right=-1&from=25.03.1997&till=28.11.2023
https://cbr.ru/hd_base/metall/metall_base_new/

another Gold price in https://ru.tradingview.com/symbols/XAUUSD/
'''
import csv
import numpy as np
import copy
import datetime
import matplotlib.pyplot as plt

fname = 'mfdexport_precious_metals_price.csv'

def text_file_num_lines(fname:str) -> int:
    """
    Определяет число строк в текстовом файле
    www.geeksforgeeks.org/count-number-of-lines-in-a-text-file-in-python
    """
    with open(fname, 'r') as fp:
        return len(fp.readlines())

print()
# https://docs.python.org/3/library/csv.html          use csv instead of pandas
nlin = text_file_num_lines(fname)
date = np.zeros(nlin - 1, dtype=object); gold = np.zeros(nlin - 1, dtype=float)
silver = copy.deepcopy(gold); platinum =  copy.deepcopy(gold); palladium = copy.deepcopy(gold)
# print(type(gold), type(silver), type(platinum), type(palladium))

with (open(fname, newline='', encoding='utf-8') as csvfile):
    the_reader = csv.reader(csvfile, delimiter=';', quotechar='|')
    i = 0
    for i,row in enumerate(the_reader):
        nrow = [row_el.replace(',', '.') for row_el in row]
        if i == 0:
            # print(f'{i} {type(row[0])}  {type(row[1])}  {type(row[2])} {type(row[3])} {type(row[4])}')
            print(f'        {row[0]:10}  {row[1]:10}  {row[2]} {row[3]} {row[4]}')
        else:
            # https://stackoverflow.com/questions/15557828/convert-string-to-date-type-python
            s = nrow[0].split()[0]
            date[i - 1] = datetime.datetime.strptime(s, '%d.%m.%Y').date()
            gold[i-1] = float(nrow[1])
            silver[i-1] = float(nrow[2])
            platinum[i-1] = float(nrow[3])
            palladium[i-1] = float(nrow[4])
            print(f'{i-1:5} {date[i-1]}  {gold[i-1]:8}  {silver[i-1]:8} {platinum[i-1]:8} {palladium[i-1]:8}')

#----- deniminate parice before 1998-01-05
    d_obj = datetime.datetime.strptime('05.01.1998', '%d.%m.%Y').date()
    for i, date_ in enumerate(date):
        if date_< d_obj:
            gold[i] = gold[i-1]/1000
            silver[i] = silver[i-1]/1000
            platinum[i] = platinum[i]/1000
            palladium[i] = palladium[i]/1000

#----- Graph part
plt.plot(date, gold,label='gold')
plt.plot(date, silver,label='silver')
plt.plot(date, platinum,label='platinum')
plt.plot(date, palladium,label='palladium')
plt.suptitle('Central Bank of the Russian Federation Registration prices for refined precious metals, rubles per gram')
plt.xlabel('year')
plt.ylabel('rubles, in 1998 ruble')
plt.grid()
plt.legend()
plt.show()