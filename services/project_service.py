import json
import requests
from config import *
from services.register_company_service import RegisterCompany


class Project(RegisterCompany):
    def create_project(self, create_project_payload):
        url = base_url + create_project_endpoint
        headers = self.headers_with_token()
        response = requests.post(url, json.dumps(create_project_payload), headers=headers)
        return self.response.get_responses(response)

    def fetch_project(self, project_id):
        url = f"{base_url + fetch_project_endpoint}/{project_id}"
        response = requests.get(url, self.headers_with_token)
        return self.response.get_responses(response)

    def update_project(self, project_id, payload):
        url = f"{base_url + update_project_endpoint}/{project_id}"
        headers = self.headers_with_token()
        response = requests.patch(url, json.dumps(payload), headers=headers)
        return self.response.get_responses(response)

    def upload_project_file(self, project_id, upload_project_file_payload):
        url = f"{base_url + upload_project_file_endpoint}/{project_id}"
        headers = self.headers_with_token()
        response = requests.post(url, json.dumps(upload_project_file_payload), headers=headers)
        return self.response.get_responses(response)
