import pytest
from library.utils import get_access_token, make_request
from config.endpoints import *
from library.utils import setup_logger
logger = setup_logger(__name__)


def test_refresh_token():
    access_token = get_access_token()
    headers = {"Authorization": f"Bearer {access_token}"}
    response = make_request("POST", REFRESH_ACCESS_TOKEN_ENDPOINT, headers=headers)
    if response.status_code == 201:
        logger.info("Refresh Access token is Successful")
    else:
        logger.error("Refresh Access token is Unsuccessful: %s", response.status_code)


def test_logout():
    access_token = get_access_token()
    headers = {"Authorization": f"Bearer {access_token}"}
    response = make_request("POST", LOGOUT_ENDPOINT, headers=headers)
    if response.status_code == 200:
        logger.info("User Logged out Successfully")
    else:
        logger.error("Logout Unsuccessful: %s", response.status_code)


def test_force_logout():
    access_token = get_access_token()
    headers = {"Authorization": f"Bearer {access_token}"}
    response = make_request("POST", FORCE_LOGOUT_ENDPOINT, headers=headers)
    if response.status_code == 200:
        logger.info("Forced log out successful")
    else:
        logger.error("Force logout failed: %s", response.status_code)


@pytest.mark.wip
def test_delete_user():
    access_token = get_access_token()
    headers = {"Authorization": f"Bearer {access_token}"}
    payload = {"email": "employee1@gmail.com"}
    response = make_request("DELETE", DELETE_USER_ENDPOINT, headers=headers, payload=payload, verify=False)
    if response.status_code == 200:
        logger.info("User deleted successfully")
    else:
        logger.error("Unable to delete the user: %s", response.status_code)
