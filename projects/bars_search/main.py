import os
import json
from geopy import distance
import requests
from flask import Flask
import folium


APIKEY = os.getenv('API')
NUBER_OF_NEAREST_BARS = 5


def extract_file_content(path_to_the_file):
    with open(path_to_the_file, "r", encoding='CP1251') as bars_file:
        bars_file_content = json.loads(bars_file.read())
    return bars_file_content


def fetch_coordinates(apikey, place):
    base_url = "https://geocode-maps.yandex.ru/1.x"
    params = {"geocode": place, "apikey": APIKEY, "format": "json"}
    response = requests.get(base_url, params=params)
    response.raise_for_status()
    places_found = response.json()['response']['GeoObjectCollection']['featureMember']
    most_relevant = places_found[0]
    lon, lat = most_relevant['GeoObject']['Point']['pos'].split(" ")
    return lat, lon


def get_nearest_bar(known_bars):
    return known_bars['distance']


def get_known_bars(bars_file_content, location):
    known_bars = []
    for bar in range(len(bars_file_content)):
        bar_name = bars_file_content[bar]['Name']
        bar_longitude, bar_latitude = bars_file_content[bar]['geoData']['coordinates']
        known_bars.append({
            'title': bar_name,
            'longitude': bar_longitude,
            'latitude': bar_latitude,
            'distance': distance.distance(location, (bar_latitude, bar_longitude))
        })
    return known_bars


def add_place_markers(nearest_known_bars, location):
    map_with_my_location = folium.Map(
      location=location, 
      zoom_start=12,
      tiles='Stamen Terrain'
      )
    folium.Marker(
        location, 
        popup="<b>I'm here</b>", 
        icon=folium.Icon(color='red')
        ).add_to(map_with_my_location)
    for bar in range(len(nearest_known_bars)):
        bar_name = nearest_known_bars[bar]['title']
        bar_coordinates = [
            nearest_known_bars[bar]['latitude'],
            nearest_known_bars[bar]['longitude']
        ]
        folium.Marker(
            location=bar_coordinates,
            popup=bar_name,
            tooltip='Drink me',
            icon=folium.Icon(icon='info-sign', color='green')
            ).add_to(map_with_my_location)
    return map_with_my_location


def show_nearest_bars():
    with open('index.html') as file:
        return file.read()


def main():
    my_location = fetch_coordinates(APIKEY, input('Где вы находитесь? '))
    bars_file_content  = extract_file_content('bars.json')
    known_bars = get_known_bars(bars_file_content, my_location)
    nearest_known_bars = sorted(known_bars, key=get_nearest_bar)[:NUBER_OF_NEAREST_BARS]
    add_place_markers(nearest_known_bars, my_location).save('index.html')

    app = Flask(__name__)
    app.add_url_rule('/', 'Время N!', show_nearest_bars)
    app.run('0.0.0.0')


if __name__ == '__main__':
    main()
