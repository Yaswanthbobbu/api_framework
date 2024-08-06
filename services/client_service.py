import json
import requests
from config import *
from services.register_company_service import RegisterCompany


class Client(RegisterCompany):
    def create_client(self, create_client_payload):
        url = base_url + create_client_endpoint
        headers = self.headers_with_token()
        response = requests.post(url, json.dumps(create_client_payload), headers=headers)
        return self.response.get_responses(response)

    def fetch_client(self, client_id):
        url = f"{base_url + fetch_client_endpoint}/{client_id}"
        headers = self.headers_with_token()
        response = requests.get(url, headers=headers)
        return self.response.get_responses(response)

    def update_client(self, client_id, payload):
        url = f"{base_url + update_client_endpoint}/{client_id}"
        headers = self.headers_with_token()
        response = requests.patch(url, json.dumps(payload), headers=headers)
        return self.response.get_responses(response)

    def upload_client_file(self, client_id, upload_client_file_payload):
        url = f"{base_url + upload_client_file_endpoint}/{client_id}"
        headers = self.headers_with_token()
        response = requests.post(url, json.dumps(upload_client_file_payload), headers=headers)
        return self.response.get_responses(response)

    def fetch_client_files(self, client_id, fetch_client_files_payload):
        url = f"{base_url + upload_client_file_endpoint}/{client_id}"
        headers = self.headers_with_token()
        response = requests.get(url, json.dumps(fetch_client_files_payload), headers=headers)
        return self.response.get_responses(response)
