import requests

APIKEY = "f58a6a7a3b81aa9698d51ad854c43102"

MY_LAT = 51.510357
MY_LONG = -0.116773

APIURL = "https://api.openweathermap.org/data/3.0/onecall"
PARAMS = {
    "lat": MY_LAT, "lon": MY_LONG, "appid": APIKEY
}

response = requests.get(url=APIURL, params=PARAMS)
response.raise_for_status()
print(response.json())
