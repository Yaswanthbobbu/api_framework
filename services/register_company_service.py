import email
import json
import requests
from config import *
from services.base_service import BaseClient


# from utils.service_requests import APIRequest


class RegisterCompany(BaseClient):
    def __init__(self):
        super().__init__()
        self.base_url = base_url
        # self.request = APIRequest()

    def register_company(self, company_payload):
        url = base_url + register_company_endpoint
        return requests.post(
            url, json.dumps(company_payload), self.headers, verify=False)

    def user_login(self, login_payload):
        url = base_url + login_endpoint
        return requests.post(url, json.dumps(login_payload), self.headers, verify=False)

    def verify_user(self, payload):
        url = base_url + verify_user_endpoint
        return requests.post(
            url, json.dumps(payload), self.headers, verify=False)

    def create_user(self, create_user_payload):
        url = base_url + create_user_endpoint
        headers = self.headers_with_token
        return requests.post(
            url, json.dumps(create_user_payload), headers=headers, verify=False)

    def change_user_password(self, user_id: None, change_password, admin: bool):
        if user_id:
            url = f"{base_url + change_user_password_endpoint}/{user_id}"
        else:
            url = f"{base_url + change_user_password_endpoint}"
        headers = self.headers_with_token
        payload = change_password
        payload['admin'] = admin
        return requests.patch(url, json.dumps(change_password), headers=headers, verify=False)

    def change_user_email(self, user_id: None, change_email):
        if user_id:
            url = f"{base_url + change_user_email_endpoint}/{user_id}"
        else:
            url = f"{base_url + change_user_email_endpoint}"
        headers = self.headers_with_token
        return requests.patch(url, json.dumps(change_email), headers=headers, verify=False)

    def refresh_access_token(self):
        url = base_url + refresh_access_token_endpoint
        headers = self.headers_with_token
        return requests.post(url, json.dumps({}), headers=headers, verify=False)

    def user_logout(self):
        url = base_url + logout_endpoint
        headers = self.headers_with_token
        return requests.post(url, json.dumps({}), headers=headers, verify=False)

    def force_logout(self, user_id):
        url = f"{base_url + force_logout_endpoint}/{user_id}"
        headers = self.headers_with_token
        return requests.post(url, json.dumps({}), headers=headers, verify=False)

    def delete_user(self, user_id):
        url = f"{base_url + delete_user_endpoint}/{user_id}"
        headers = self.headers_with_token
        return requests.delete(url, headers=headers, verify=False)
