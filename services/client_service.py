import json
from config import *
from services.register_company_service import RegisterCompany


class Client(RegisterCompany):
    def create_client(self, create_client_payload):
        url = base_url + create_client_endpoint
        return self.request.post_request(
            url, json.dumps(create_client_payload), self.headers_with_token)

    def fetch_client(self, client_id):
        url = f"{base_url + fetch_client_endpoint}/{client_id}"
        return self.request.get_request(url, self.headers_with_token)

    def update_client(self, client_id, payload):
        url = f"{base_url + update_client_endpoint}/{client_id}"
        return self.request.patch_request(
            url, json.dumps(payload), self.headers_with_token)

    def upload_client_file(self, client_id, upload_client_file_payload):
        url = f"{base_url + upload_client_file_endpoint}/{client_id}"
        return self.request.post_request(
            url, json.dumps(upload_client_file_payload), self.headers_with_token)

    def fetch_client_files(self, client_id, fetch_client_files_payload):
        url = f"{base_url + upload_client_file_endpoint}/{client_id}"
        return self.request.get_request(
            url, json.dumps(fetch_client_files_payload), self.headers_with_token)
