import pytest
from assertpy import assert_that, soft_assertions
from services.register_company_service import RegisterCompany

company = RegisterCompany()


def test_if_new_company_can_be_registered(context, company_payload, get_logger):
    logger = get_logger
    logger.info('Test: Register company starts')
    response = company.register_company(company_payload)
    logger.info(response.json())
    with soft_assertions():
        assert_that(response.status_code).is_equal_to(200)
        assert_that(response.json()).is_equal_to({'detail': 'Success'})
        if response.status_code == 200:
            logger.info('Registering new company test passed')
        else:
            logger.error('Registering new company test failed')

# def test_if_user_change_password(context, change_password, user_id, get_logger):
#     logger = get_logger
#     logger.info('Test: Change user password starts')
#     response, response_json = company.change_user_password(change_password, admin=True, user_id=user_id)
#     logger.info(response.json)
#     with soft_assertions():
#         # assert_that(response.status_code).is_equal_to(200)
#         assert_that(response.json()).is_equal_to({'details': 'Success'})
#         if response.status_code == 200:
#             logger.info('Change user password test passed')
#         else:
#             logger.error('Change user password test failed')
