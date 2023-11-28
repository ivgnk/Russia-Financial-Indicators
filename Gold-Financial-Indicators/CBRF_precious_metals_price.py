'''
Data from https://mfd.ru/centrobank/preciousmetals/
https://mfd.ru/centrobank/preciousmetals/?left=0&right=-1&from=25.03.1997&till=28.11.2023

another Gold price in https://ru.tradingview.com/symbols/XAUUSD/
'''
import csv

fn = 'mfdexport_precious_metals_price.csv'

# https://docs.python.org/3/library/csv.html
print()
with open(fn, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(', '.join(row))


