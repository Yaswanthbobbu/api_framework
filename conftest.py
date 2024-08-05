import os

import pytest
import logging
from datetime import datetime

from utils.file_reader import *


@pytest.fixture(scope="session")
def context():
    return {}


# class ReverseFileHandler(logging.FileHandler):
#     def emit(self, record):
#         log_entry = self.format(record)
#         log_file_path = self.baseFilename
#
#         # read contents of log file
#         if os.path.exists(log_file_path):
#             with open(log_file_path, 'r') as f:
#                 existing_content = f.read()
#         else:
#             existing_content = ""
#
#         # new log entry + existing content
#         with open(log_file_path, 'w') as f:
#             f.write(log_entry + '\n' + existing_content)


@pytest.fixture(scope="session")
def setup_logger():
    log_folder = os.path.abspath("../logs")
    os.makedirs(log_folder, exist_ok=True)
    log_file = os.path.join(log_folder, "api_testing.log")

    logger = logging.getLogger("API_Testing")
    logger.setLevel(logging.INFO)

    if logger.hasHandlers():  # Remove existing handlers and avoid duplicates
        logger.handlers.clear()

    stream_handler = logging.StreamHandler()   # terminal output
    stream_handler.setLevel(logging.INFO)

    # FileHandler for log file
    file_handler = logging.FileHandler(log_file, mode='a')
    file_handler.setLevel(logging.INFO)

    formatter = logging.Formatter(f'%(name)s - %(levelname)s - %(message)s - {datetime.now().strftime("%d/%m %H:%M:%S")}')
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
def login_payload():
    yield read_file("user_login.json")


@pytest.fixture(scope="session")
def company_payload():
    yield read_file("create_company.json")


@pytest.fixture(scope="session")
def create_user_payload():
    yield read_file("create_user4.json")


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
