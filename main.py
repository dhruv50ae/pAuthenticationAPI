import requests

APIKEY = "f58a6a7a3b81aa9698d51ad854c43102"
APIURL = "https://api.openweathermap.org/data/2.5/weather"

PARAMS = {
    "q": "Leicester,UK", "appid": APIKEY
}

willRain = False

response = requests.get(url=APIURL, params=PARAMS)
response.raise_for_status()
weatherData = response.json()
conditionCode = weatherData["weather"][0]["id"]

if int(conditionCode) < 700:
    willRain = True
if willRain:
    print("It will rain, bring an umbrella")