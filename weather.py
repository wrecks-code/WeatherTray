import json
import requests

API_KEY = "688bfc5f4efd5f0a757c587bc51bb74d"
CITY = "Filderstadt"
COMPLETE_URL = (
    f"http://api.openweathermap.org/data/2.5/weather?appid={API_KEY}&q={CITY}"
)

TEMP_KEY = "temperature"
DESCRIPTION_KEY = "description"


def get_weather() -> dict:
    response = requests.get(COMPLETE_URL, timeout=5)
    response_value = response.json()

    if response_value["cod"] == "404":
        return {TEMP_KEY: 100, DESCRIPTION_KEY: "City not found"}

    data_dict = json.loads(json.dumps(response_value))

    print (f"Weather {data_dict["weather"][0]["main"]}")

    main_value = response_value["main"]
    weather_value = response_value["weather"]
    temp_value = int(main_value["temp"] - 273.15)

    return {TEMP_KEY: temp_value, DESCRIPTION_KEY: weather_value[0]["description"]}
