# This code sample uses requests (HTTP library)
import requests
import re
from pprint import pprint
import getpass
import sys
import json
import os.path


class NetAtmoWeather:

    def __init__(self):
        self.json_file = 'config.json'
        self.data = None

    def prompt(self, message, error_message, isvalid):
        # """Prompt for input given a message and return that value after verifying the input.
        #
        # Keyword arguments:
        # message -- the message to display when asking the user for the value
        # error_message -- the message to display when the value fails validation
        # isvalid -- a function that returns True if the value given by the user is valid
        # """
        res = None
        while res is None:
            res = getpass.getpass(str(message) + ': ')

            if not isvalid(res):
                print(str(error_message))
                res = None
        return res

    def print_settings(self):
        weather = self.data['weather']
        if weather is not None:
            print(self.data)
        else:
            print("no payload found")

    def make_device_id (self, serial_number):

        type = serial_number[0]

        if type is 'h':
            device_cat = '02'

        else:
            device_cat = '03'

        tuple = re.findall('..', serial_number[1:])
        mac = device_cat + ":00:00:"+":".join(tuple)

        return mac

    def read_settings(self):

        if os.path.isfile(self.json_file):
            self.data = json.load(open(self.json_file))

    def get_weather_data(self):
        self.read_settings()

        if len(self.data['credentials']['password']) == 0:
            self.data['credentials']['password'] = self.prompt(
                message="Enter the password",
                error_message="The password must not be less than 8 chars",
                isvalid=lambda v: len(v) >= 8)

        weather = self.data['weather']

        if self.data['credentials']['password'] is not None:

            payload = dict(grant_type='password', username=self.data['credentials']['username'],
                           password=self.data['credentials']['password'], client_id=weather['api']['client_id'],
                           client_secret=weather['api']['client_secret'], scope='read_station')

            response = requests.post("https://api.netatmo.com/oauth2/token", payload)

            access_token = response.json()["access_token"]

            modules = self.data['weather']['modules']
            device_id = self.make_device_id(modules[0]['serial_number'])

            params = {
                'access_token': access_token,
                'module_id': device_id
            }

            try:
                response = requests.post("https://api.netatmo.com/api/getstationsdata", params=params)
                response.raise_for_status()
                data = response.json()["body"]

            except requests.exceptions.HTTPError as error:
                print(error.response.status_code, error.response.text)

        sys.exit(0)


atmos = NetAtmoWeather ()
atmos.get_weather_data()
