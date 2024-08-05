import json
from config import *
from services.register_company_service import RegisterCompany


class Project(RegisterCompany):
    def create_project(self, create_project_payload):
        url = base_url + create_project_endpoint
        return self.request.post_request(
            url, json.dumps(create_project_payload), self.headers_with_token)

    def fetch_project(self, project_id):
        url = f"{base_url + fetch_project_endpoint}/{project_id}"
        return self.request.get_request(url, self.headers_with_token)

    def update_project(self, project_id, payload):
        url = f"{base_url + update_project_endpoint}/{project_id}"
        return self.request.patch_request(
            url, json.dumps(payload), self.headers_with_token)

    def upload_project_file(self, project_id, upload_project_file_payload):
        url = f"{base_url + upload_project_file_endpoint}/{project_id}"
        return self.request.post_request(
            url, json.dumps(upload_project_file_payload), self.headers_with_token)
