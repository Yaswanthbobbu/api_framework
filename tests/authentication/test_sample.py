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
