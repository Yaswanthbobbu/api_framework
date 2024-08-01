import json
from api_framework.services.base_service import BaseClient
from config.endpoints import BASE_URL
from api_framework.utils.service import APIRequest


class RegisterCompany(BaseClient):
    def __init__(self):
        super().__init__()
        self.base_url = BASE_URL
        self.request = APIRequest()

    def register_company(self, company_payload):
        return self.request.post_request(
            self.base_url, json.dumps(company_payload), self.headers
        )

    def create_user(self, payload):
        return self.request.post_request(
            self.base_url, json.dumps(payload), self.headers
        )

    def get_booking(self, booking_id):
        url = f"{BASE_URL}/{booking_id}"
        return self.request.get_request(url, self.headers)

    def update_booking(self, booking_id, payload):
        url = f"{BASE_URL}/{booking_id}"
        return self.request.put_request(
            url, json.dumps(payload), self.headers_with_basic_auth
        )

    def delete_user(self, user_id):
        url = f"{BASE_URL}/{user_id}"
        return self.request.delete_request(url, self.headers_with_basic_auth)