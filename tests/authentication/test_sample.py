import json

import pytest
from pathlib import Path

from config.endpoints import CREATE_USER_ENDPOINT
from library.utils import *
from library.utils import setup_logger
logger = setup_logger(__name__)


def test_login():
    logger.info("User tries to Login")
    access_token = get_access_token()
    if access_token:
        logger.info("Login is successful")
    else:
        logger.error("Login is Unsuccessful")


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