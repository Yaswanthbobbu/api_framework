import pytest
from assertpy import assert_that, soft_assertions
from services.register_company_service import RegisterCompany

company = RegisterCompany()


def test_if_user_can_login(context, login_payload, get_logger):
    logger = get_logger
    logger.info('Test: User login starts')
    response = company.user_login(login_payload)
    with soft_assertions():
        assert_that(response.status_code).is_equal_to(200)
        assert_that(response.json()).is_equal_to({'detail': 'Success'})
        if response.status_code == 200:
            logger.info('User login test passed')
        else:
            logger.error('User login test failed')


def test_if_user_can_logout(get_logger):
    logger = get_logger
    logger.info('Test: User logout starts')
    response = company.user_logout()
    with soft_assertions():
        logger = get_logger
        assert_that(response.status_code).is_equal_to(200)
        assert_that(response.json()).is_equal_to({'details': 'Success'})
        if response.status_code == 200:
            logger.info('User logged out test passed')
        else:
            logger.error('User logged out test failed')