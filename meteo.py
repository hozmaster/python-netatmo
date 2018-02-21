# This code sample uses requests (HTTP library)
import requests
from pprint import pprint
import json
import os.path

json_file = 'config.json'
data = None
if os.path.isfile(json_file):
    data = json.load(open(json_file))

    if data is not None:
        pprint(data)

        username = data['credentials']['username']
        password = data['credentials']['password']

        if len(password) == 0:
            print('No password given. exit')
            exit(255)

        weather = data['weather']

        payload = {'grant_type': 'password',
                   'username': username,
                   'password': password,
                   'client_id': weather['api']['client_id'],
                   'client_secret': weather['api']['client_secret'],
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
        #     'device_id': '70:ee:XX:XX:XX:XX'
        # }
        # response = requests.post("https://api.netatmo.com/api/getstationsdata", params=params)
        # response.raise_for_status()
        # data = response.json()["body"]
        # print (data)

    # except requests.exceptions.HTTPError as error:
    #     print(error.response.status_code, error.response.text)
else:
    print('json file is not exists. Create it and try again.')
