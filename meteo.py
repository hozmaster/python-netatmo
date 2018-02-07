# This code sample uses requests (HTTP library)
# import requests
from pprint import pprint
import json

payload = {'grant_type': 'password',
           'username': '',
           'password': '',
           'client_id':"5a356b7d8c04c44aa48b487f",
           'client_secret': "XlcZoyrevno5paVeN3EHVQCFwlKTcKgT9byPP",
           'scope': 'read_station'}
# try:

data = json.load(open('config.json'))

if data is not None:
    pprint(data)

    username = data['credentials']['username']
    print(username)

    password = data['credentials']['password']
    print(password)

    netatmo = data['netatmo']

    payload = {'grant_type': 'password',
               'username': username,
               'password': password,
               'client_id': netatmo['api']['client_id'],
               'client_secret': netatmo['api']['client_secret'],
               'scope': 'read_station'}

    print(payload)

    # response = requests.post("https://api.netatmo.com/oauth2/token", data=payload)
    # response.raise_for_status()
    # access_token=response.json()["access_token"]
    # refresh_token=response.json()["refresh_token"]
    # scope=response.json()["scope"]
    #
    # print("Your access token is:", access_token)
    # print("Your refresh token is:", refresh_token)
    # print("Your scopes are:", scope)
    #
    # params = {
    #     'access_token': access_token,
    #     'device_id': '70:ee:50:2b:2e:3a'
    # }
    # response = requests.post("https://api.netatmo.com/api/getstationsdata", params=params)
    # response.raise_for_status()
    # data = response.json()["body"]
    # print (data)

# except requests.exceptions.HTTPError as error:
#     print(error.response.status_code, error.response.text)