import json
import pytest
from pathlib import Path
from library.utils import *
from config.endpoints import *
from library.utils import setup_logger
logger = setup_logger(__name__)  # Set up the logger


@pytest.fixture
def client_payload():
    payload_path = Path(__file__).parent.parent / "data" / "client_payload.json"
    with open(payload_path, "r") as file:
        payload = json.load(file)
    return payload


@pytest.fixture
def update_client_payload():
    payload_path = Path(__file__).parent.parent / "data" / "update_client_payload.json"
    with open(payload_path, "r") as file:
        payload = json.load(file)
    return payload


@pytest.fixture
def client_id():
    return client_id


def test_create_client(client_payload, client_id):
    access_token = get_access_token()
    currUser = access_token.split(';')[4]
    headers = {"accesstoken": f"{access_token}", "currUser": f"{currUser}", "Content-Type": "application/json"}
    response = make_request("POST", CREATE_CLIENT_ENDPOINT, headers=headers, payload=client_payload, verify=False)
    if response.status_code == 201:
        client_id = response.json().get("id")
        logger.info("Client created successfully with ID: %s", client_id)
        # yield client_id

    else:
        logger.error("Failed to create new client: %s", response.status_code)
        pytest.fail("Failed to create new client")


@pytest.mark.skip
def test_fetch_client(client_id):
    access_token = get_access_token()
    currUser = access_token.split(';')[4]
    headers = {"accesstoken": f"{access_token}", "currUser": f"{currUser}", "Content-Type": "application/json"}
    response = make_request("GET", f"{FETCH_CLIENT_ENDPOINT}/{client_id}", headers=headers, verify=False)
    if response.status_code == 200:
        logger.info("Client fetched successfully: %s", client_id)
    else:
        logger.error("Unable to fetch client: %s", response.status_code)
        pytest.fail("Unable to fetch client")


@pytest.mark.skip
def test_update_client(client_id, update_client_payload):
    access_token = get_access_token()
    currUser = access_token.split(';')[4]
    headers = {"accesstoken": f"{access_token}", "currUser": f"{currUser}", "Content-Type": "application/json"}
    response = make_request("PATCH", f"{UPDATE_CLIENT_ENDPOINT}/{client_id}", headers=headers,
                            payload=update_client_payload, verify=False)
    if response.status_code == 200:
        logger.info("Updated the client successfully: %s", client_id)
    else:
        logger.error("Unable to update the client: %s", response.status_code)
        pytest.fail("Unable to update the client")
