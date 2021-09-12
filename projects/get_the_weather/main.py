import requests


places = ['Сан-Франциско', 'Лондон', 'аэропорт Шереметьево', 'Череповец']
payload = {'lang': 'ru', 'm': '', 'q': '', 'n': '', 'T': ''}


def get_weather(places, params, url_template='http://wttr.in/{}'):
    weather = ''
    for place in places:
        url = url_template.format(place)
        response = requests.get(url, params=params)
        response.raise_for_status()
        weather = '{0}\n{1}'.format(weather, response.text)
    return weather


if __name__ == '__main__':
    print(get_weather(places, payload))
