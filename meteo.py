# This code sample uses requests (HTTP library)
import requests
from pprint import pprint
import json
import os.path

class NetAtmoWeather:

    def __init__(self):
        self.json_file = 'config.json'
        self.data = None

    def print_settings(self):
        weather = self.data['weather']
        if weather is not None:
            print(self.data)
        else:
            print("no payload found")

    def read_settings(self):

        if os.path.isfile(self.json_file):
            self.data = json.load(open(self.json_file))

        #
        # username = data['credentials']['username']
        #
        # if len(password) == 0:
        #     password = input('Enter your password to service: ')
        #     print('No password given. exit')
        #     exit(255)
        #


        # payload = {'grant_type': 'password',
        #            'username': username,
        #            'password': password,
        #            'client_id': weather['api']['client_id'],
        #            'client_secret': weather['api']['client_secret'],
        #            'scope': 'read_station'}
        #
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
        #     'device_id': '70:ee:XX:XX:XX:XX'
        # }
        # response = requests.post("https://api.netatmo.com/api/getstationsdata", params=params)
        # response.raise_for_status()
        # data = response.json()["body"]
        # print (data)

        #     # except requests.exceptions.HTTPError as error:
        #     #     print(error.response.status_code, error.response.text)
        # else:
        #     print('json file is not exists. Create it and try again.')


atmos = NetAtmoWeather ()
atmos.read_settings()
atmos.print_settings()