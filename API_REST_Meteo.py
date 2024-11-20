import requests

def get_temperature(city_name):
    url = f"https://api.open-meteo.com/v1/forecast?latitude=43.8808&longitude=11.0986&current=temperature_2m"
    response = requests.get(url)
    data = response.json()
    temperature = data['current']['temperature_2m']
    return temperature

city_name = "Prato"
temperature = get_temperature(city_name)

print(f"La temperatura attuale a {city_name} è {temperature}°C.")
