import requests
import time

url = "http://127.0.0.1:5000/weather"

while True:
    response = requests.get( url )

    if response.status_code == 200:
        data = response.json()

        temperatur = data["temperature_2m"]
        wind = data["wind_speed_10m"]
        feuchtigkeit = data["relative_humidity_2m"]

        print('Aktuelles Wetter in Köln:')
        print("Temperatur:", temperatur, "°C")
        print("Windgeschwindigkeit:", wind, "km/h")
        print("Luftfeuchtigkeit:", feuchtigkeit, "%")
        print()

    else:
        print("Fehler beim Abrufen der Daten:", response.status_code)

    time.sleep(10)
    