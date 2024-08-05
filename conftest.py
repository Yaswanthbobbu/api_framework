import os

import pytest
import logging
from datetime import datetime

from utils.file_reader import *


@pytest.fixture(scope="session")
def context():
    return {}


@pytest.fixture(scope="session")
def setup_logger():
    log_folder = r"./logs"
    os.makedirs(log_folder, exist_ok=True)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(os.path.join(log_folder, "api_testing.log")),
        ],
    )
    logger = logging.getLogger("api_testing")
    return logger


@pytest.fixture(scope="session")
def get_logger(setup_logger):
    log_file_path = f"api_testing.log"
    logger = setup_logger
    handler = logging.FileHandler(os.path.join("logs", log_file_path))
    formatter = logging.Formatter(f'%(name)s - %(levelname)s - %(message)s - {datetime.now().strftime("%d/%m %H:%M")}')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    # read_latest_logs(log_file_path)
    return logger


def read_latest_logs(log_file_path):
    with open(log_file_path, 'r') as log_file:
        lines = log_file.readlines()
        for line in reversed(lines):
            print(line.strip())


@pytest.fixture(scope="session")
def login_payload():
    yield read_file("user_login.json")


@pytest.fixture(scope="session")
def company_payload():
    yield read_file("create_company.json")


@pytest.fixture(scope="session")
def create_user_payload():
    yield read_file("create_user.json")


@pytest.fixture(scope="session")
def create_client():
    yield read_file("create_client.json")


@pytest.fixture(scope="session")
def update_client():
    yield read_file("udpate_client.json")


@pytest.fixture(scope="session")
def create_project():
    yield read_file("create_project.json")


@pytest.fixture(scope="session")
def update_project():
    yield read_file("update_project.json")


@pytest.fixture(scope="session")
def change_password():
    yield read_file("change_password.json")


@pytest.fixture(scope="session")
def change_email():
    yield read_file("change_email.json")


@pytest.fixture(scope="session")
def user_id():
    yield read_file("email.json")
