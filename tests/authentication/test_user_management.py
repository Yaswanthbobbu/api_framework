from library.utils import get_access_token, make_request
from config.endpoints import CREATE_USER_ENDPOINT, DELETE_USER_ENDPOINT


def test_create_user():
    access_token = get_access_token()
    headers = {"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"}
    payload = {
        "email": "employee1@gmail.com",
        "password": "SecureP@ssw0rd!",
        "userType": "general",
        "title": "Employee",
        "fullName": "First Employee",
        "phoneNumber": "123456789",
        "isActive": True,
        "isVerified": True
    }
    response = make_request("POST", CREATE_USER_ENDPOINT, headers=headers, payload=payload, verify=False)
    assert response.status_code == 201, f'"Failed to create new user. \nStatus code:", {response.status_code}'


def test_delete_user():
    access_token = get_access_token()
    headers = {"Authorization": f"Bearer {access_token}"}
    payload = {"email": "employee1@gmail.com"}
    response = make_request("DELETE", DELETE_USER_ENDPOINT, headers=headers, payload=payload, verify=False)
    assert response.status_code == 200
