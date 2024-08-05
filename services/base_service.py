import os
import json
import requests
from config import *
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class BaseClient:
    def __init__(self):
        access_token, currUser = self.auth_service(os.getenv('EMAIL'), os.getenv('PASSWORD'))
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"}
        self.headers_with_token = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "currUser": currUser,
            "accessToken": access_token}

    @staticmethod
    def auth_service(username, password):
        url = base_url + login_endpoint
        login_payload = {
            "email": username,
            "password": password}
        response = requests.post(url, json.dumps(login_payload), verify=False)
        token = response.headers['Authorization']
        if not token:
            raise ValueError('Authorization header missing in the response')
        access_token = token.split(';')[0]
        currUser = token.split(';')[4]
        return f"{access_token}", currUser
