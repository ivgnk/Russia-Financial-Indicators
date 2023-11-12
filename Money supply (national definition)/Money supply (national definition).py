'''
Input and visualisation from xlsx
Money supply (national definition): monetary aggregates M0, M1, M2
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial
from scipy.optimize import curve_fit

the_title = 'Russia Money supply'
degree = 9

def print_row_col(dat: pd.DataFrame, title: str, view_head_tile: bool = False):
    print();     print(title)
    print('num rows    = ', dat.shape[0]); print('num cols = ', dat.shape[1])
    if view_head_tile:
        print(dat.head(7));        print(dat.tail(7))
    print()

# def interp_exp(x, y):
#     llen = len(x); new_x = np.arange(llen)
#     [a, b], res1 = curve_fit(lambda x1, a, b: a*np.exp(b * x1), x, y)
#     return a * np.exp(b * x)

def interp_poly(x, y):
    llen = len(x); new_x = np.arange(llen)
    global degree
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.krogh_interpolate.html#scipy.interpolate.krogh_interpolate
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.KroghInterpolator.html#scipy.interpolate.KroghInterpolator
    # poly = interpolate.KroghInterpolator(new_x, y) - very bad, unstable

    # https://fadeevlecturer.github.io/python_lectures/notebooks/scipy/interpolation_approx.html
    approximation = Polynomial.fit(new_x, y, degree)
    y_poly = approximation(new_x)
    print(f'{approximation=}')
    print(f'{y_poly=}')
    return y_poly

#-(1) -- input
main_xls_fname = the_title+'.xlsx'
m_DataFrame = pd.read_excel(main_xls_fname, sheet_name='Data')
print_row_col(m_DataFrame, 'before-' + the_title, True)
print(f'\n{m_DataFrame.columns=}\n')

#-(2) -- columns name
# for i,col_ in enumerate(m_DataFrame.columns): print(i,'  ',col_); print('\n')
# https://www.geeksforgeeks.org/how-to-get-column-names-in-pandas-dataframe/
col_name = list(m_DataFrame.columns)
x = m_DataFrame[col_name[0]]
m0 = m_DataFrame[col_name[1]]; m1 = m_DataFrame[col_name[2]]; m2 = m_DataFrame[col_name[3]]
x_1993 = m_DataFrame[col_name[4]]
m2_1993 = m_DataFrame[col_name[5]]
m2_1993_cash = m_DataFrame[col_name[6]]
m2_1993_noncash = m_DataFrame[col_name[7]]
m2_1993_appr = interp_poly(x, m2_1993)
# m2_1993_appr = interp_exp(x, m2_1993)

fig, ax = plt.subplots(figsize=(10, 8))
plt.title(the_title)
plt.plot(x,m0,label=col_name[1]); plt.plot(x,m1,label=col_name[2]);
plt.plot(x,m2,label=col_name[3])
# geeksforgeeks.org/linestyles-in-matplotlib-python/
plt.plot(x_1993,m2_1993,label=col_name[5], linestyle='dotted')
plt.plot(x_1993,m2_1993_cash,label=col_name[6], linestyle='dotted')
plt.plot(x_1993,m2_1993_noncash,label=col_name[7], linestyle='dotted')

plt.plot(x_1993,m2_1993_appr,label=col_name[7]+' appr, degree='+str(degree), linewidth=3, linestyle='--')


plt.xlabel('Date'); plt.ylabel('Monetary aggregates, bn rub');
plt.legend(); plt.grid()
plt.show()