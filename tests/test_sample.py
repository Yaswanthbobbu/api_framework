from assertpy import assert_that, soft_assertions
from services.register_company_service import RegisterCompany

company = RegisterCompany()


def test_if_admin_can_login(context, admin_payload, get_logger):
    logger = get_logger
    logger.info('Test: Admin login starts')
    response = company.admin_login(admin_payload)
    with soft_assertions():
        assert_that(response.status_code).is_equal_to(200)
        assert_that(response.content).is_equal_to({'detail': 'Success'})
        if response.status_code == 200:
            logger.info('Admin login test passed')
        else:
            logger.error('Admin login test failed')


# def test_if_user_change_password(context, change_password, get_logger):
#     logger = get_logger
#     logger.info('Test: Change user password starts')
#     response = company.change_user_password(change_password, admin=False)
#     with soft_assertions():
#         assert_that(response.status_code).is_equal_to(200)
#         assert_that(response.content).is_equal_to({'detail': 'Success'})
#         logger.info(response.content)
#         if response.status_code == 200:
#             logger.info('Change user password test passed')
#         else:
#             logger.error('Change user password test failed')

