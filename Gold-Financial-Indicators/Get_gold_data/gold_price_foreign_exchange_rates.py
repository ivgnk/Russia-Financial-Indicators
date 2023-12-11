'''
on the base of https://gist.github.com/StevenTso/557306aa74a40ef1ec5a75856e54aa74

get gold & silver price from https://metalpriceapi.com
https://metalpriceapi.com/documentation
https://metalpriceapi.com/dashboard
'''

import requests

api_key_fn = 'metalpriceapi_com_api_key.txt'

# https://pythonru.com/osnovy/fajly-v-python-vvod-vyvod
with open(api_key_fn,'r') as f:
    api_key_my = f.readline()
print(api_key_my)

# get price in USD
url = 'https://api.metalpriceapi.com/v1/latest?api_key='+api_key_my+'&base=USD&currencies=XAU'

r = requests.get(url)
gold_dict = r.json()
print(gold_dict)
rate = gold_dict["rates"]["XAU"]
gold_price = 1/rate
print(gold_price)