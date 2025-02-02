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
    log_folder = os.path.abspath("../logs")
    os.makedirs(log_folder, exist_ok=True)
    log_file = os.path.join(log_folder, datetime.now().strftime("%d%m") + " - api_testing.log")

    logger = logging.getLogger("API_Testing")
    logger.setLevel(logging.INFO)

    if logger.hasHandlers():  # Remove existing handlers and avoid duplicates
        logger.handlers.clear()

    stream_handler = logging.StreamHandler()  # terminal output
    stream_handler.setLevel(logging.INFO)

    file_handler = logging.FileHandler(log_file, mode='a')  # FileHandler for log file
    file_handler.setLevel(logging.INFO)

    formatter = logging.Formatter(
        f'%(name)s - %(levelname)s - %(message)s - {datetime.now().strftime("%d%m %H:%M:%S")}')
    stream_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # logger.addHandler(stream_handler)  to print on terminal
    logger.addHandler(file_handler)

    for handler in logger.handlers:
        print(f"Handler: {handler}")

    return logger


@pytest.fixture(scope="session")
def get_logger(setup_logger):
    return setup_logger


@pytest.fixture(scope="session")
def company_payload():
    yield read_file("create_company.json")


@pytest.fixture(scope="session")
def verify_user():
    yield read_file("verify_user.json")


@pytest.fixture(scope="session")
def admin_payload():
    yield read_file("admin_login.json")


@pytest.fixture(scope="session")
def login_payload():
    yield read_file("user_login.json")


@pytest.fixture(scope="session")
def create_user_payload():
    yield read_file("create_user.json")


@pytest.fixture(scope="session")
def create_client():
    yield read_file("create_client.json")


@pytest.fixture(scope="session")
def update_client():
    yield read_file("update_client.json")


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
def user_mail():
    yield read_file("user_mail.json")


@pytest.fixture(scope="session")
def user_id():
    yield read_file("user_id.json")


@pytest.fixture(scope="session")
def file_path():
    file_name = "test_upload_file.txt"
    files = os.path.abspath("files")
    os.makedirs(files, exist_ok=True)
    file_path = os.path.join(files, file_name)
    with open(file_path, 'w') as f:
        f.write("{'client_id' : '66b4c93941cda67aca2c4604'}")
    # assert file_path.read() == '{client_id : '66b4c93941cda67aca2c4604'}'
    return file_path


@pytest.fixture(scope="session")
def fetch_client_files():
    yield read_file("client_id.json")

