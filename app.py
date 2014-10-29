from flask import Flask, render_template
from settings import API_Key, Weather_API_Key
from wmata.service import WMATA
from weather.service import Weather_Underground
from wmata.models import Train
from weather.models import Weather 
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

# def show_current_conditions():
# 	url = 'http://api.wunderground.com/api/{0}/conditions/q/DC/Washington.json'.format(Weather_API_Key)
# 	weather_information = requests.get(url).json()
# 	current = weather_information.get('current_observation')
# 	list_of_weather_items = []
# 	temp = current.get('temp_f')
# 	list_of_weather_items.append(temp)
# 	condition = current.get('weather')
# 	list_of_weather_items.append(condition)
# 	icon_url = current.get('icon_url')
# 	list_of_weather_items.append(icon_url)
# 	return list_of_weather_items


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

weather_information = Weather_Underground(Weather_API_Key)

@app.route('/weather')
def show_current_conditions():
	weather = weather_information.show_current_conditions()
	current_observation = weather.get('current_observation')
	temperature = current_observation.get('temp_f')
	weather = current_observation.get('weather')
	return str(temperature), weather

port = os.getenv('VCAP_APP_PORT', '5000')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=int(port), debug=True)


