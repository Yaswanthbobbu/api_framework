import json
import pytest
from pathlib import Path
from library.utils import *
from config.endpoints import *
from library.utils import setup_logger
logger = setup_logger(__name__)  # Set up the logger


@pytest.fixture
def project_payload():
    payload_path = Path(__file__).parent.parent / "data" / "project_payload.json"
    with open(payload_path, "r") as file:
        payload = json.load(file)
    return payload


@pytest.fixture
def update_project_payload():
    payload_path = Path(__file__).parent.parent / "data" / "update_project_payload.json"
    with open(payload_path, "r") as file:
        payload = json.load(file)
    return payload


@pytest.fixture
def project_id():
    return project_id


def test_create_project(project_payload, project_id):
    access_token = get_access_token()
    currUser = access_token.split(';')[4]
    headers = {"accesstoken": f"{access_token}", "currUser": f"{currUser}", "Content-Type": "application/json"}
    response = make_request("POST", CREATE_PROJECT_ENDPOINT, headers=headers, payload=project_payload, verify=False)
    if response.status_code == 201:
        project_id = response.json().get("id")
        logger.info("Project created successfully with ID: %s", project_id)
        # yield project_id

    else:
        logger.error("Failed to create new project: %s", response.status_code)
        pytest.fail("Failed to create new project")


def test_fetch_project(project_id):
    access_token = get_access_token()
    currUser = access_token.split(';')[4]
    headers = {"accesstoken": f"{access_token}", "currUser": f"{currUser}", "Content-Type": "application/json"}
    response = make_request("GET", f"{FETCH_PROJECT_ENDPOINT}/{project_id}", headers=headers, verify=False)
    if response.status_code == 200:
        logger.info("Project fetched successfully: %s", project_id)
    else:
        logger.error("Unable to fetch project: %s", response.status_code)
        pytest.fail("Unable to fetch project")


def test_update_project(project_id, update_project_payload):
    access_token = get_access_token()
    currUser = access_token.split(';')[4]
    headers = {"accesstoken": f"{access_token}", "currUser": f"{currUser}", "Content-Type": "application/json"}
    response = make_request("PATCH", f"{UPDATE_PROJECT_ENDPOINT}/{project_id}", headers=headers,
                            payload=update_project_payload, verify=False)
    if response.status_code == 200:
        logger.info("Updated the project successfully: %s", project_id)
    else:
        logger.error("Unable to update the project: %s", response.status_code)
        pytest.fail("Unable to update the project")
