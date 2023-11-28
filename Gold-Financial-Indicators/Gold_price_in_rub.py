'''
Gold price in russian rubles
'''

import numpy as np
import matplotlib.pyplot as plt

st_r  = 80; en_r = 120; step_r = 0.1
st_g = 1000; en_g = 3000

usd_rub = np.arange(st_r, en_r+step_r, step_r); len_dr = len(usd_rub); print(f'{len_dr=}')
gld_usd = np.arange(st_g, en_g, 1); len_gd = len(gld_usd); print(f'{len_gd=}')

price_in_rub = np.zeros(shape = (len_gd, len_dr))
z = np.outer(gld_usd, usd_rub )

# print(np.shape(z))
# print(np.shape(price_in_rub))
print('min = ',np.min(z))
print('max = ',np.max(z))

eq_ = True
for i in range(len_gd):
    for j in range(len_dr):
        price_in_rub[i,j] = gld_usd[i]*usd_rub[j]
        eq_ = eq_ and abs(price_in_rub[i,j] - z[i,j])<1e-10
        # print(price_in_rub[i,j],'   ', z[i,j],'   ',eq_ )

print(f'{eq_=}')

prices_in_28_11_2023_rub= 88.7
prices_in_28_11_2023_dlr =2016.5

fig = plt.figure(figsize=(10,8))
plt.suptitle('Gold price in russian rubles')
plt.xlabel("Rubles per dollar")
plt.ylabel("Dollars per Troy ounce of gold")
#--- for contour levels
# usd_rub2 = np.arange(st_r, en_r, 20); gld_usd2 = np.arange(1200, 2200, 200)
# z2 = np.outer(gld_usd2, usd_rub2)
# lvl = np.sort(np.array(list(set(np.ravel(z2)))))
# print(f'{lvl=}')
lvl = np.arange(50000, 410000, 20000)
#--- for contour levels
curves1 = plt.contourf(usd_rub, gld_usd,  z, lvl)
curves2 =plt.contour( usd_rub, gld_usd,  z, lvl, colors = 'k')
plt.plot(prices_in_28_11_2023_rub, prices_in_28_11_2023_dlr, 'ro', label='prices in 28-11-2023')
plt.clabel(curves2, fontsize=10, colors = 'k')
fig.colorbar(curves1)

plt.legend(loc='right')
plt.show()


