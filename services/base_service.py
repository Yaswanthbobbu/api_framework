import json

import requests
from config import *
from env import *


class BaseClient:
    def __init__(self):
        # access_token, currUser = self.basic_auth()  #  os.environ.get('EMAIL'), os.environ.get('PASSWORD')
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"}
        self.headers_with_token = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "currUser": self.basic_auth()[1],
            "accessToken": self.basic_auth()[0]}

    @staticmethod
    def basic_auth():
        url = base_url + login_endpoint
        login_payload = {
            "email": EMAIL,
            "password": PASSWORD}
        response = requests.post(url, json.dumps(login_payload), verify=False)
        token = response.headers['Authorization']
        if not token:
            raise ValueError('Authorization header missing in the response')
        access_token = token.split(';')[0]
        currUser = token.split(';')[4]
        return [f"{access_token}", currUser]
