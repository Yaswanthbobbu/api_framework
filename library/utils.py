import requests
from config.endpoints import BASE_URL, LOGIN_ENDPOINT
from config.config import EMAIL, PASSWORD


def get_access_token():
    login_url = BASE_URL + LOGIN_ENDPOINT
    login_payload = {
        "email": EMAIL,
        "password": PASSWORD
    }
    response = requests.post(login_url, json=login_payload, verify=False)
    if response.status_code == 200:
        tokens = response.json()
        return tokens.get("access_token")
    else:
        raise Exception("Login failed. Status code:", response.status_code)


def make_request(method, endpoint, headers=None, payload=None, verify=False):
    url = BASE_URL + endpoint
    response = requests.request(method, url, headers=headers, json=payload, verify=verify)
    return response
