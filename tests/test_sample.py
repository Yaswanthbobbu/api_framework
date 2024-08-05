from assertpy import assert_that, soft_assertions
from services.register_company_service import RegisterCompany

company = RegisterCompany()


def test_if_user_can_login(context, login_payload, get_logger):
    logger = get_logger
    logger.info('Test: User login starts')
    response = company.user_login(login_payload)
    with soft_assertions():
        assert_that(response.status_code).is_equal_to(200)
        logger.info(response.json())
        assert_that(response.json()).is_equal_to({'detail': 'Success'})
        if response.status_code == 200:
            logger.info('User login test passed')
        else:
            logger.error('User login test failed')


def test_if_user_change_password1(context, user_id, change_password, get_logger):
    logger = get_logger
    logger.info('Test: Change user password starts1')
    response = company.change_user_password(user_id, change_password)
    with soft_assertions():
        assert_that(response.status_code).is_equal_to(200)
        assert_that(response.json()).is_equal_to({'details': 'Success'})
        if response.status_code == 200:
            logger.info('Change user password test passed')
        else:
            logger.error('Change user password test failed')
