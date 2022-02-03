from datetime import datetime

import os
import requests

API_KEY = os.getenv('API_KEY', '5ca4a16f81c524ddb70479c12f12708d')
MANILA_LAT = 14.6059661
MANILA_LON = 121.0292042
BASE_URL= 'https://api.openweathermap.org/data/2.5/onecall?'
PARAMS = f'lat={MANILA_LAT}&lon={MANILA_LON}&appid={API_KEY}&units=metric'


if __name__ == '__main__':
    response = requests.get(f'{BASE_URL}{PARAMS}')
    print('Weather Forecast:')
    for data in response.json()['daily']:
        day = datetime.utcfromtimestamp(data['dt'])
        day_formatted = day.strftime('%a, %d %b %Y')
        temperature = data['temp']['max']
        degree_sign = u'\N{DEGREE SIGN}'
        print(f'{day_formatted}: {temperature}{degree_sign}C')
