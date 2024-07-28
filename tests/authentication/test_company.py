from library.utils import make_request, get_access_token
from config.endpoints import REGISTER_COMPANY_ENDPOINT


def test_register_company():
    access_token = get_access_token()
    headers = {"Authorization": f"Bearer {access_token}"}
    payload = {
        "userData": {
            "username": "Firstapitester",
            "password": "SecureP@ssw0rd!",
            "email": "firstapitester@gmail.com",
            "firstName": "First",
            "lastName": "User",
            "userType": "admin",
            "title": "Administrator",
            "fullName": "First User"
        },
        "companyData": {
            "companyName": "New API Test Company",
            "companyEmail": "firstapitester@gmail.com",
            "address": {
                "street": "123 Main St",
                "city": "Testtown",
                "state": "Teststate",
                "zipcode": "12345",
                "country": "Test Country"
            }
        }
    }
    response = make_request("POST", REGISTER_COMPANY_ENDPOINT, payload=payload, headers=headers)
    assert response.status_code == 201
