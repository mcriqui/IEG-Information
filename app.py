from flask import Flask, render_template
from settings import API_Key, Weather_API_Key
from wmata.service import WMATA
from weather.service import Weather_Underground
from wmata.models import Train
from weather.models import Weather 
from metro_incidents.models import metro_incidents
from metro_incidents.service import metro_incidents
import requests 
import os


app = Flask(__name__)

service = WMATA(API_Key)

def get_info_for_one_metro_center_lower():
	data = service.station_predictions('C01')
	list_of_trains = []
	for item in data.get('Trains')[:3]:
		item_train_instance = Train(item)
		list_of_trains.append(item_train_instance)
	return list_of_trains

def get_info_for_one_metro_center_upper():
	mc_upper_data = service.station_predictions('A01')
	mc_upper_list_of_trains = []
	for item in mc_upper_data.get('Trains')[:3]:
		mc_upper_item_train_instance = Train(item)
		mc_upper_list_of_trains.append(mc_upper_item_train_instance)
	return mc_upper_list_of_trains 

def get_info_for_one_mcpherson():
	mcpherson_data = service.station_predictions('C02')
	mcpherson_list_of_trains = []
	for item in mcpherson_data.get('Trains')[:3]:
		mcpherson_item_train_instance = Train(item)
		mcpherson_list_of_trains.append(mcpherson_item_train_instance)
	return mcpherson_list_of_trains

weather_information = Weather_Underground(Weather_API_Key)

incident_information = metro_incidents(API_Key)

def get_incident_information():
	incident_data = incident_information.get_incidents()
	incident_list = []

@app.route('/')
def show_metro_times():
	metro_center_lower = get_info_for_one_metro_center_lower()
	metro_center_upper = get_info_for_one_metro_center_upper()
	mcpherson_square = get_info_for_one_mcpherson()
	weather = weather_information.show_current_conditions()
	current_observation = weather.get('current_observation')
	temperature = current_observation.get('temp_f')
	weather = current_observation.get('weather')
	icon_url = current_observation.get('icon_url')
	return render_template('trains.html', metro_center_lower=metro_center_lower, metro_center_upper=metro_center_upper, mcpherson_square=mcpherson_square, weather=weather, temperature=temperature, icon_url=icon_url)





port = os.getenv('VCAP_APP_PORT', '5000')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=int(port), debug=True)

