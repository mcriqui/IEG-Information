import requests


class WMATA:
    """Helps access the WMATA API. An API KEY is required"""
    def __init__(self, key):
        self.key = key
        self.base_url = u'http://api.wmata.com/'

    def station_predictions(self, station_id):
        """Get train predictions for a station. Provide a station_id
            arguments: station_id
        """
        prediction_url = u'{0}StationPrediction.svc/json/GetPrediction/{1}?api_key={2}'.format(self.base_url, station_id, self.key)
        resp = requests.get(prediction_url)
        if resp.ok:
            return resp.json()
        else:
            return None

class Weather_Underground:
    """Helps access Weather Underground API. An API KEY is required."""
    def __init__(self, key):
        self.key = key
        self.base_url = 'http://api.wunderground.com/api/'

    def current_conditions(self):
        condition_url = '{0}{1}/conditions/q/DC/Washington.json'.format(self.base_url, self.key)
        weather_response = requests.get(condition_url)
        if weather_response.ok:
            return weather_response.json()
        else:
            return None
        