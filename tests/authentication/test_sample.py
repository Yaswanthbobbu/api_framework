import json
import pytest
from pathlib import Path

from config.endpoints import *
from library.utils import *
from library.utils import setup_logger

logger = setup_logger(__name__)


def test_login():
    logger.info("User tries to Login: %s", BASE_URL + CREATE_USER_ENDPOINT)
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
    try:
        access_token = get_access_token()
        currUser = access_token.split(';')[4]
        newaccess_token = access_token.split(';')[0]
        headers = {"accessToken": f"{newaccess_token}", "currUser": f"{currUser}", "Content-Type": "application/json"}
        response = make_request("POST", CREATE_USER_ENDPOINT, headers=headers, payload=create_user_payload,
                                verify=False)
        logger.info("Request Headers: %s", headers)
        logger.info("Request Payload: %s", create_user_payload)
        logger.info("Response Status Code: %s", response.status_code)
        logger.info("Response Content: %s", response.content)
        # logger.info("Response Content: %s", response.json())
        if response.status_code == 201:
            logger.info("Creation of new user is Successful")
        else:
            logger.error("Failed to create new user")
    except Exception as error:
        raise f"api error: {error}"
