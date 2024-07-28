from library.utils import get_access_token, make_request
from config.endpoints import LOGOUT_ENDPOINT, FORCE_LOGOUT_ENDPOINT


def test_login():
    access_token = get_access_token()
    if access_token:
        return f"\nLogin successful. Access token:", {access_token}
    else:
        print("\nLogin failed. Access token not found in the response.")

# def test_verify_user():
#     access_token = get_access_token()
#     headers = {"Authorization": f"Bearer {access_token}"}
#     response = make_request("POST", LOGOUT_ENDPOINT, headers=headers)
#     assert response.status_code == 200, f'\nLogin failed. Status code: {response.status_code}'

# def test_logout():
#     access_token = get_access_token()
#     headers = {"Authorization": f"Bearer {access_token}"}
#     response = make_request("POST", LOGOUT_ENDPOINT, headers=headers)
#     assert response.status_code == 200, f'\nLogin failed. Status code: {response.status_code}'
#
#
# def test_force_logout():
#     access_token = get_access_token()
#     headers = {"Authorization": f"Bearer {access_token}"}
#     response = make_request("POST", FORCE_LOGOUT_ENDPOINT, headers=headers)
#     assert response.status_code == 200, f"\nForce logout failed. Status code: {response.status_code}"
