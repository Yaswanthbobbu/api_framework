import requests
import logging
from colorama import Fore, Style, init
from config.endpoints import BASE_URL, LOGIN_ENDPOINT
from config.config import EMAIL, PASSWORD


def make_request(method, endpoint, headers=None, payload=None, verify=False):
    url = BASE_URL + endpoint
    response = requests.request(method, url, headers=headers, json=payload, verify=verify)
    return response


def get_access_token():
    login_url = BASE_URL + LOGIN_ENDPOINT
    login_payload = {
        "email": EMAIL,
        "password": PASSWORD
    }
    response = requests.post(login_url, json=login_payload, verify=False)
    if response.status_code == 200:
        access_token = response.headers['Authorization']
        return access_token
    else:
        raise Exception("Login failed. Status code:", response.status_code)


init(autoreset=True)  # Initialize colorama


class CustomFormatter(logging.Formatter):
    def format(self, record):
        log_message = super().format(record)
        if record.levelname == 'INFO':
            log_message = Fore.GREEN + log_message + Style.RESET_ALL
        centered_message = log_message.center(80)  # Adjust width as needed
        return centered_message


def setup_logger(name=__name__, level=logging.INFO):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)

    formatter = CustomFormatter('\n%(levelname)s - %(message)s - %(asctime)s')
    console_handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(console_handler)

    return logger
