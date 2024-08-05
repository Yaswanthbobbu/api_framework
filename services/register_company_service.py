import json
import requests
from config import *
from env import *
from services.base_service import BaseClient
from utils.service_requests import APIRequest


class RegisterCompany(BaseClient):
    def register_company(self, company_payload):
        url = base_url + register_company_endpoint
        return requests.post(
            url, json.dumps(company_payload), self.headers)

    def user_login(self):
        url = base_url + login_endpoint
        login_payload = {
            "email": EMAIL,
            "password": PASSWORD}
        return requests.post(url, json=login_payload, verify=False)

    def verify_user(self, payload):
        url = base_url + verify_user_endpoint
        return requests.post(
            url, json.dumps(payload), self.headers)

    def create_user(self, create_user_payload):
        url = base_url + create_user_endpoint
        print(self.headers_with_token)
        response = requests.post(
            url, json.dumps(create_user_payload), self.headers_with_token, verify=False)
        return requests.post(
            url, json.dumps(create_user_payload), self.headers_with_token, verify=False)

    def change_user_password(self, user_id, payload):
        url = f"{base_url + change_user_password_endpoint}/{user_id}"
        return requests.patch(url, json.dumps(payload))

    def change_user_email(self, user_id, payload):
        url = f"{base_url + change_user_email_endpoint}/{user_id}"
        return requests.patch(url, json.dumps(payload))

    def refresh_access_token(self):
        url = base_url + refresh_access_token_endpoint
        return requests.post(url, json.dumps({}), self.headers_with_token)

    def user_logout(self):
        url = base_url + logout_endpoint
        return requests.post(url, json.dumps({}), self.headers)

    def force_logout(self, user_id):
        url = f"{base_url + force_logout_endpoint}/{user_id}"
        return requests.post(url, json.dumps({}), self.headers)

    def delete_user(self, user_id):
        url = f"{base_url}/{user_id}"
        return requests.delete(url)
