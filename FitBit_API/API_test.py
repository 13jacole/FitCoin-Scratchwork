import requests

x = requests.post('https://api.fitbit.com/oauth2/token')

print(x.text)