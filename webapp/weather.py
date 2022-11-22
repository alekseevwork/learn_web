import logging
import requests

from flask import current_app

logging.basicConfig(filename='bot.log', level=logging.INFO)

def weather_by_city(city_name):
    weather_url = current_app.config['WEATHER_URL']
    params = {
        "key": current_app.config['WEATHER_API_KEY'],
        "q": city_name,
        "format": "json",
        "num_of_days": 1,
        "lang": "ru"
    }
    try:
        result = requests.get(weather_url, params=params)
        result.raise_for_status()
        weather = result.json()
        if 'data' in weather:
            if 'current_condition' in weather['data']:
                try:
                    return weather['data']['current_condition'][0]
                except IndexError:
                    logging.info('IndexError')
                    return False
                except TypeError:
                    logging.info('TypeError')
                    return False
        return False
    except (requests.RequestException, ValueError):
        logging.info('Connected error')
        return False

if __name__ == '__main__':
    weather = weather_by_city('Kaliningrad, Russia')
    print(weather)
    