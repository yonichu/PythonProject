import requests
import pytest

API_KEY = "1ba06f056aec6fbe252352ae07e9e7f4"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

#test to check if the API call was successful - aka it had status code 200
def test_get_status_code_200_for_London_city():
    response = requests.get(f"{BASE_URL}?appid={API_KEY}&q=London")
    assert response.status_code == 200

