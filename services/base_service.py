import os
import requests
from config import *
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class BaseClient:
    def __init__(self):
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"}

    def headers_with_token(self):
        access_token, currUser, refresh_token = self.auth_service(os.getenv('EMAIL'), os.getenv('PASSWORD'))
        headers_dict = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "currUser": currUser,
            "accessToken": access_token,
            "refreshToken": refresh_token
        }
        return headers_dict

    def make_request(self, method, endpoint, data=None):
        url = base_url + endpoint
        headers = self.headers_with_token()
        response = requests.request(
            method,
            url,
            json=data,
            headers=headers,
            verify=False
        )
        return response

    @staticmethod
    def auth_service(username, password):
        url = base_url + login_endpoint
        login_payload = {
            "email": username,
            "password": password}
        try:
            response = requests.post(url, json=login_payload, verify=False)
            response.raise_for_status()  # This will raise an HTTPError for bad responses (4xx and 5xx)
        except requests.exceptions.HTTPError as http_err:
            if response.status_code == 500:
                print("500 Internal Server Error: Stopping execution")
                raise Exception(response.text)
            else:
                print(f"HTTP error occurred: {http_err}")
                raise
        except Exception as err:
            print(f"An error occurred: {err}")
            raise
        token = response.headers['Authorization']
        if not token:
            raise ValueError('Authorization header missing in the response')

        tokens = token.split(';')
        if len(tokens) < 5:
            raise ValueError('Invalid token format in the Authorization header')

        access_token = token.split(';')[0]
        refresh_token = token.split(';')[1]
        # ID_token = token.split(';')[2]
        # expiresIn = token.split(';')[3]
        currUser = token.split(';')[4]
        return f"{access_token}", currUser, refresh_token
