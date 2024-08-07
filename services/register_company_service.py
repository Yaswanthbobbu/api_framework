import json
import requests
from config import *
from services.base_service import BaseClient, APIResponse


class RegisterCompany(BaseClient):
    def __init__(self):
        super().__init__()
        self.base_url = base_url
        self.response = APIResponse

    def register_company(self, company_payload):
        url = base_url + register_company_endpoint
        response = requests.post(url, json.dumps(company_payload), self.headers, verify=False)
        return self.response.get_responses(response)

    def verify_user(self, verify_user):
        url = base_url + verify_user_endpoint
        response = requests.post(url, json.dumps(verify_user), self.headers, verify=False)
        return self.response.get_responses(response)

    def admin_login(self, admin_payload):
        url = base_url + login_endpoint
        response = requests.post(url, json.dumps(admin_payload), self.headers, verify=False)
        return self.response.get_responses(response)

    def create_user(self, create_user_payload):
        url = base_url + create_user_endpoint
        headers = self.headers_with_token()
        response = requests.post(url, json.dumps(create_user_payload), headers=headers, verify=False)
        return self.response.get_responses(response)

    def user_login(self, login_payload):
        url = base_url + login_endpoint
        response = requests.post(url, json.dumps(login_payload), self.headers, verify=False)
        return self.response.get_responses(response)

    def change_user_password(self, change_password, admin: bool):
        url = f"{base_url + change_user_password_endpoint}/{admin}"
        headers = self.headers_with_token()
        response = requests.patch(url, json.dumps(change_password), headers=headers, verify=False)
        return self.response.get_responses(response)

    def change_user_email(self, change_email, admin: bool):
        url = f"{base_url + change_user_email_endpoint}/{admin}"
        headers = self.headers_with_token()
        try:
            response = requests.patch(url, json.dumps(change_email), headers=headers, verify=False)
            response_json = response.json()
        except requests.exceptions.JSONDecodeError:
            response_json = {"error": "Invalid JSON response", "text": response.text}
        return response, response_json

    def refresh_access_token(self):
        url = base_url + refresh_access_token_endpoint
        headers = self.headers_with_token()
        response = requests.post(url, json.dumps({}), headers=headers, verify=False)
        return self.response.get_responses(response)

    def user_logout(self):
        url = base_url + logout_endpoint
        headers = self.headers_with_token()
        response = requests.post(url, json.dumps({}), headers=headers, verify=False)
        return self.response.get_responses(response)

    def force_logout(self, user_id):
        url = f"{base_url + force_logout_endpoint}/{user_id}"
        headers = self.headers_with_token()
        response = requests.post(url, json.dumps({}), headers=headers, verify=False)
        return self.response.get_responses(response)

    def delete_user(self, user_id):
        url = f"{base_url + delete_user_endpoint}/{user_id}"
        headers = self.headers_with_token()
        response = requests.delete(url, headers=headers, verify=False)
        return self.response.get_responses(response)
