import logging
from colorama import Fore, Style, init

init(autoreset=True)


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
