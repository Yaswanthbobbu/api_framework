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
            logging.FileHandler(os.path.join(log_folder, "api_testing.log")),
            logging.StreamHandler(),
        ],
    )

    logger = logging.getLogger("api_testing")
    return logger


@pytest.fixture(scope="session")
def get_logger(setup_logger):
    log_file = f"api_testing.log"
    logger = setup_logger
    handler = logging.FileHandler(os.path.join("logs", log_file))
    formatter = logging.Formatter(f'%(name)s - %(levelname)s - %(message)s - {datetime.now().strftime("%d/%m %H:%M")}')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


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
