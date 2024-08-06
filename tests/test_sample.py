from assertpy import assert_that, soft_assertions
from services.register_company_service import RegisterCompany

company = RegisterCompany()


def test_if_user_can_logout(get_logger):
    logger = get_logger
    logger.info('Test: User logout starts')
    response = company.user_logout()
    with soft_assertions():
        logger = get_logger
        assert_that(response.status_code).is_equal_to(200)
        assert_that(response.json()).is_equal_to({'details': 'Success'})
        logger.info(response.json())
        if response.status_code == 200:
            logger.info('User logged out test passed')
        else:
            logger.error('User logged out test failed')

# def test_if_user_can_logout(get_logger):
#     logger = get_logger
#     logger.info('Test: User logout starts')
#     response = company.user_logout()
#     with soft_assertions():
#         logger = get_logger
#         assert_that(response.status_code).is_equal_to(200)
#         assert_that(response.json()).is_equal_to({'details': 'Success'})
#         logger.info(response.json())
#         if response.status_code == 200:
#             logger.info('User logged out test passed')
#         else:
#             logger.error('User logged out test failed')

