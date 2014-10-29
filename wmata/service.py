
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

        