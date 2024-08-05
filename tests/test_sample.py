from assertpy import assert_that, soft_assertions
from services.register_company_service import RegisterCompany
company = RegisterCompany()


def test_if_user_can_login(context,login_payload, get_logger):
    logger = get_logger
    logger.info('Test: User login starts')
    response = company.user_login(login_payload)
    with soft_assertions():
        assert_that(response.status_code).is_equal_to(200)
        assert_that(response.content).is_not_empty()
        if response.status_code == 200:
            logger.info('User login test passed')
        else:
            logger.error('User login test failed')


def test_if_admin_can_create_user(context, create_user_payload, get_logger):
    logger = get_logger
    logger.info('Test: Create user starts')
    response = company.create_user(create_user_payload)
    with soft_assertions():
        assert_that(response.status_code).is_equal_to(201)
        assert_that(response.content).is_empty()
        if response.status_code == 201:
            logger.info('Admin create user test passed')
        else:
            logger.error('Admin create user test failed')



