import json
import pytest
from pathlib import Path
from library.utils import *
from config.endpoints import *
from library.utils import setup_logger

logger = setup_logger(__name__)  # Set up the logger


@pytest.fixture
def company_payload():
    payload_path = Path(__file__).parent.parent / "data" / "company_payload.json"
    with open(payload_path, "r") as file:
        payload = json.load(file)
    return payload


def test_register_company(company_payload):
    access_token = get_access_token()
    headers = {"Authorization": f"Bearer {access_token}"}
    response = make_request("POST", REGISTER_COMPANY_ENDPOINT, payload=company_payload, headers=headers)
    if response.status_code == 200:
        logger.info("Successfully registered the company")
    else:
        logger.error("Error in registering company: %s", response.json())


@pytest.mark.skip
def test_verify_user():
    access_token = get_access_token()
    headers = {"Authorization": f"Bearer {access_token}"}
    response = make_request("POST", LOGOUT_ENDPOINT, headers=headers)
    if response.status_code == 200:
        logger.info("User is Verified")
    else:
        logger.error("User verification unsuccessful: %s", response.status_code)


def test_login():
    access_token = get_access_token()
    if access_token:
        logger.info("Login is Successful: %s", access_token)
    else:
        logger.error("Login is Unsuccessful, access token not found in the response.")


@pytest.fixture
def create_user_payload():
    payload_path = Path(__file__).parent.parent / "data" / "create_user.json"
    with open(payload_path, "r") as file:
        payload = json.load(file)
    return payload


def test_create_user(create_user_payload):
    access_token = get_access_token()
    headers = {"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"}
    response = make_request("POST", CREATE_USER_ENDPOINT, headers=headers, payload=create_user_payload, verify=False)
    if response.status_code == 201:
        logger.info("Creation of new user is Successful")
    else:
        logger.error("Failed to create new user: %s", response.status_code)


def test_change_email():
    access_token = get_access_token()
    headers = {"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"}
    payload = {"newEmail": "user@example.com", "userToChangeID": "string"}
    response = make_request("PATCH", CHANGE_USER_EMAIL_ENDPOINT, headers=headers, payload=payload)
    if response.status_code == 201:
        logger.info("Creation of new user is Successful")
    else:
        logger.error("Failed to create new user: %s", response.status_code)


def test_change_password():
    access_token = get_access_token()
    headers = {"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"}
    payload = {"currPassword": "string", "newPassword": "string", "userToChangeID": "string"}
    response = make_request("PATCH", CHANGE_USER_PASSWORD_ENDPOINT, headers=headers, payload=payload)
    if response.status_code == 201:
        logger.info("Creation of new user is Successful")
    else:
        logger.error("Failed to create new user: %s", response.status_code)
