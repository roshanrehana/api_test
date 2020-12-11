import requests
import pytest
from datetime import datetime

url="https://data.weather.gov.hk/weatherAPI/opendata/weather.php"
params={'dataType':"rhrread"}

def poll(url,params):
    try:
        response = requests.get(url,params)
        # print(response.text)
        # print(response.headers)
    except FileNotFoundError as e:
        raise e
    else:
        resp = response.json()
        # resp = {1:1,2:3}
        print(resp.values())
        return response

poll(url,params)

# Using pytest fixtures allows you to plugin these methods directly into the test methods below as required
@pytest.fixture
def response():
    return poll(url,params)

@pytest.fixture
def get_curr_date():
    return datetime

# Below are our test methods covering different scenarios
def test_api_response(response):
    # Test the http response
    assert response.status_code == 200, "No valid response received"

def test_response_time(response):
    # Test whether the response is taking less than a second to come back
    assert response.elapsed.total_seconds() < 1, "Took more than a second for the response to come back"

def test_update_time(response,get_curr_date):
    # Test whether we are getting the latest hourly updates
    response_body = response.json()
    curr_date=get_curr_date.now().date()
    curr_hour=get_curr_date.now().hour
    curr_dt_time=str(curr_date)+"T"+str(curr_hour)
    assert str(response_body['updateTime']).startswith(curr_dt_time), "Last update is outdated"

def test_temperature_exists(response):
    # Test whether the values on temperatures are not empty
    response_body = response.json()
    assert response_body['temperature'].values != None, "Temperature is missing in response"

