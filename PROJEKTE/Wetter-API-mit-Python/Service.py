#importiere die benötigten Module
import requests
from flask import Flask, jsonify

#Erstelle eine Flask 
app = Flask(__name__)


#Definiere einen Endpunkt (/weather), der Wetterdaten zurückgibt
@app.route('/weather', methods=['GET'])
def weather():
    #URL zur Wetter-API mit festen Koordinaten (hier: Köln)
    url = "https://api.open-meteo.com/v1/forecast?latitude=50.94&longitude=6.96&current=temperature_2m,wind_speed_10m,relative_humidity_2m"
    #Sende eine GET-Anfrage an die API
    response = requests.get( url )

    #Wenn die Anfrage erfolgreich war (Statuscode 200)
    if response.status_code == 200:
        data = response.json()
        return jsonify(data["current"])
    
    #Wenn die API-Anfrage fehl 
    else:
        return jsonify({"error": "Fehler beim Abrufen der Wetterdaten"}), 500
    
if __name__ == '__main__':
    app.run(debug=True)