import pytest
import requests
from API_Endpoints.BookingEndpoints import BookingEndpoints
from Utilities.CustomLogger import LogGen
from Utilities.ReadEnv import ReadEnvvalue


@pytest.fixture(scope="session")
def base_url():
    return "https://restful-booker.herokuapp.com"


@pytest.fixture(scope="function")
def booking_client(base_url):
    return BookingEndpoints(base_url)


@pytest.fixture(scope="session")
def secure_token(base_url):
    url = f"{base_url}/auth"
    payload ={
        "username": "admin",
        "password": "password123"
    }
    headres = {"Content_Type": "application/json"}
    response = requests.post(url, json=payload, headers=headres)

    return response.json().get("token")