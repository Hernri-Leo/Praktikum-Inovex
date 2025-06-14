<p align="center">
  <img src="https://github.com/Hernri-Leo/Praktikum-Inovex/blob/main/assets/inovex-logo.png" alt="inovex-logo" />
</p>

# 📝 Praktikumsbericht – Inovex

Willkommen zu meinem Praktikumsbericht bei **inovex**. Hier dokumentiere ich täglich meine Aufgaben, verwendeten Technologien und Lernfortschritte.

---

## 📅 Mittwoch, 11. Juni 2025

<details>
<summary><strong>Klicken zum Aufklappen</strong></summary>

| Uhrzeit      | Tätigkeit                                                   | Tools/Technologien     |
|--------------|-------------------------------------------------------------|-------------------------|
| 09:00–09:30  | Rundgang durch die Räumlichkeiten                           | —                       |
| 09:30–10:00  | Vorstellung der Projekte                                     | —                       |
| 10:00–10:30  | Einführung in GitHub                                         | GitHub                  |
| 10:30–11:00  | Projektstart: Microbit Car                                   | Chrome                  |
| 11:00–11:30  | GitHub-Bericht schreiben                                     | Chrome                  |
| 11:30–12:00  | Arbeiten am Microbit-Projekt & GitHub                        | Chrome                  |
| 12:00–12:30  | Weiterarbeit am Microbit Car                                 | Chrome                  |
| 12:30–13:00  | **Mittagspause**                                             | —                       |
| 13:00–13:30  | Einführung: [Leuchtkäfer (Glowbug)](https://python-online.ch/index.php?inhalt_links=robotik/navigation.inc.php&inhalt_mitte=robotik/mb/crashCourse.inc.php) – Python | Chrome                  |
| 13:30–14:00  | Besprechung, Git                                             | Git                     |
| 14:00–14:30  | Microbit: Musik & Sounds                                     | Chrome                  |
| 14:30–16:30  | Arbeiten mit [CoDrone EDU](https://www.robolink.com/products/codrone-edu) | Chrome              |
| 16:30–18:00  | Weiterentwicklung Microbit Car                               | Chrome                  |

</details>

---

## 📅 Donnerstag, 12. Juni 2025

<details>
<summary><strong>Klicken zum Aufklappen</strong></summary>

| Uhrzeit      | Tätigkeit                                | Tools/Technologien        |
|--------------|------------------------------------------|----------------------------|
| 09:00–09:30  | Projekt: Wetter-API mit Python            | Chrome                     |
| 09:30–10:30  | Einrichtung: Visual Studio Code & Python  | VS Code, Python            |
| 10:30–11:30  | Erstes API-Testing mit Postman            | Postman, Python            |
| 11:30–12:00  | Weiterarbeit am Code                      | Visual Studio Code         |
| 12:00–13:00  | **Mittagspause**                          | —                          |
| 13:00–15:00  | Projektarbeit: Wetter-API mit Python      | Python                     |
| 15:00–15:30  | Besprechung: API-Aufbau und Feedback      | GitHub, Python             |
| 15:30–18:30  | Weiterentwicklung: Microbit Car Steuerung | Microbit, Python, Chrome   |

</details>

---

## 📅 Freitag, 13. Juni 2025

<details>
<summary><strong>Klicken zum Aufklappen</strong></summary>

| Uhrzeit      | Tätigkeit                                        | Tools/Technologien       |
|--------------|--------------------------------------------------|---------------------------|
| 09:00–09:30  | Tagesplanung & Mini-Standup mit Betreuer         | —                         |
| 09:30–10:15  | Testlauf: IR-Fernbedienung für Microbit Car      | Microbit, MakeCode        |
| 10:15–11:00  | Fehlerbehebung: Reaktionsverzögerung beim IR-Code| Python, Microbit          |
| 11:00–12:00  | Projektarbeit: Bewegungsfunktionen erweitern     | MakeCode, Microbit        |
| 12:00–13:00  | **Mittagspause**                                 | —                         |
| 13:00–13:45  | Kurzeinführung: Git Branches & Pull Requests     | Git, GitHub               |
| 13:45–14:00  | Code-Review mit Teammitglied (Feedbackrunde)     | GitHub                    |
| 14:00–14:15  | Bericht bearbeiten                               | GitHub                    |
| 14:15–15:15  | Microbit Car: Neue Steuerfunktionen mit Sound    | MakeCode, Microbit        |
| 15:15–15:45  | Besprechung: Wochen-Review & Praktikumsfeedback  | —                         |
| 15:45–16:45  | Endtest: Microbit Car mit Fernbedienung          | Microbit, Chrome          |
| 16:45–17:00  | Aufräumen & Abschlussbericht schreiben           | GitHub                    |

</details>

---

## 🔧 Verwendete Tools & Technologien

> [!TIP]
> - **Python**, **Flask**, **requests**
> - **Git**, **GitHub**
> - **Visual Studio Code**, **Mu Editor**
> - **Microbit**, **MakeCode**, **CoDrone EDU**
> - **Chrome**, **Postman**

---

## 📌 Hinweise

> [!NOTE]
> - Die Dokumentation wurde täglich aktualisiert.

---

## Meine WetterAPI

```python
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
```
---

```python

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

```

---

