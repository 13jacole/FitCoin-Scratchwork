import requests

from FitBit_API_Keys import *

x = requests.post('https://api.fitbit.com/oauth2/authorize')

print(x.text)