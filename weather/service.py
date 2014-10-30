import requests
from settings import Weather_API_Key

class Weather_Underground:
    """Helps access Weather Underground API. An API KEY is required."""
    def __init__(self, key):
        self.key = key
        self.base_url = u'http://api.wunderground.com/api/'

    def show_current_conditions(self):
        url = 'http://api.wunderground.com/api/{0}/conditions/q/DC/Washington.json'.format(Weather_API_Key)
        weather_information = requests.get(url).json()
        return weather_information
   