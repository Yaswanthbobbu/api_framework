import json
import requests
from config import *
from services.register_company_service import RegisterCompany


class Client(RegisterCompany):
    def create_client(self, create_client_payload):
        url = base_url + create_client_endpoint
        headers = self.headers_with_token()
        response = requests.post(url, json.dumps(create_client_payload), headers=headers, verify=False)
        return self.response.get_responses(response)

    def fetch_client(self, client_id):
        url = f"{base_url + fetch_client_endpoint}/{client_id}"
        headers = self.headers_with_token()
        response = requests.get(url, headers=headers, verify=False)
        return self.response.get_responses(response)

    def update_client(self, client_id, payload):
        url = f"{base_url + update_client_endpoint}/{client_id}"
        headers = self.headers_with_token()
        response = requests.patch(url, json.dumps(payload), headers=headers, verify=False)
        return self.response.get_responses(response)

    def upload_client_file(self, client_id, file_path, upload_client_file_payload= None):
        url = f"{base_url + upload_client_file_endpoint}/{client_id}"
        headers = self.headers_with_token()
        files = {'file': open(file_path, 'rb')}
        data = upload_client_file_payload if upload_client_file_payload else {}
        response = requests.post(url, headers=headers, files=files, data=data, verify=False)
        files['file'].close()
        # with open(file_path, 'rb') as file:
        #     files = {'file': (file_path, file)}
        #     response = requests.post(url, data=upload_client_file_payload, headers=headers, files=files, verify=False)
        return self.response.get_responses(response)

    def fetch_client_files(self, client_id, fetch_client_files):
        url = f"{base_url + upload_client_file_endpoint}/{client_id}"
        headers = self.headers_with_token()
        params = fetch_client_files if fetch_client_files else {}
        response = requests.get(url, params=params, headers=headers, verify=False)
        return self.response.get_responses(response)
