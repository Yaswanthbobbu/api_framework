import pytest
from assertpy import assert_that, soft_assertions
from services.register_company_service import RegisterCompany

company = RegisterCompany()


def test_if_admin_can_delete_user(context, user_id, get_logger):
    logger = get_logger
    logger.info('Test: Delete user starts')
    response = company.delete_user(user_id)
    with soft_assertions():
        assert_that(response.status_code).is_equal_to(200)
        assert_that(response.json()).is_equal_to({'details': 'Success'})
        if response.status_code == 200:
            logger.info('Delete user test passed')
        else:
            logger.error('Delete user test failed')
