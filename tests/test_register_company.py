import pytest
from assertpy import assert_that, soft_assertions
from services.register_company_service import RegisterCompany

company = RegisterCompany()


@pytest.mark.skip(reason='only be created at once')
def test_if_new_company_can_be_registered(context, company_payload, get_logger):
    logger = get_logger
    logger.info('Test: Register company starts')
    response = company.register_company(company_payload)
    with soft_assertions():
        assert_that(response.status_code).is_equal_to(200)
        assert_that(response.content).is_equal_to({'detail': 'Success'})
        if response.status_code == 200:
            logger.info('Registering new company test passed')
        else:
            logger.error('Registering new company test failed')


@pytest.mark.skip(reason='configure flag/ manual check')
def test_user_verification(context, verify_user, get_logger):
    logger = get_logger
    logger.info('Test: User Verification starts')
    response = company.verify_user(verify_user)
    with soft_assertions():
        assert_that(response.status_code).is_equal_to(200)
        assert_that(response.content).is_equal_to({'detail': 'Success'})
        if response.status_code == 200:
            logger.info('User verification test passed')
        else:
            logger.error('User verification test failed')


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


def test_if_admin_can_create_user(context, create_user_payload, get_logger):
    logger = get_logger
    logger.info('Test: Create user starts')
    response = company.create_user(create_user_payload)
    with soft_assertions():
        assert_that(response.status_code).is_equal_to(201)
        assert_that(response.content['detail']).is_equal_to('Success')
        assert_that(response.content).contains('newID')
        # {'detail': 'Success', 'newID': '66b1985f24f81ef9cb14196d'}
        if response.status_code == 201:
            logger.info('Admin create user test passed')
        else:
            logger.error('Admin create user test failed')
    context['newID'] = company.create_user(create_user_payload).content["newID"]


def test_if_user_can_login(context, login_payload, get_logger):
    logger = get_logger
    logger.info('Test: User login starts')
    response= company.user_login(login_payload)
    with soft_assertions():
        assert_that(response.status_code).is_equal_to(200)
        logger.info(response.content)
        assert_that(response.content).is_equal_to({'detail': 'Success'})
        if response.status_code == 200:
            logger.info('User login test passed')
        else:
            logger.error('User login test failed')


def test_if_admin_can_change_user_password(context, change_password, get_logger):
    logger = get_logger
    logger.info('Test: Admin Changes user password starts')
    response = company.change_user_password(change_password, admin=True)
    with soft_assertions():
        assert_that(response.status_code).is_equal_to(200)
        assert_that(response.content).is_equal_to({'details': 'Success'})
        logger.info(response.content)
        if response.status_code == 200:
            logger.info('Admin Changes user password test passed')
        else:
            logger.error('Admin Changes user password test failed')


def test_if_user_change_password(context, change_password, get_logger):
    logger = get_logger
    logger.info('Test: Change user password starts')
    response = company.change_user_password(change_password, admin=False)
    with soft_assertions():
        assert_that(response.status_code).is_equal_to(200)
        assert_that(response.content).is_equal_to({'details': 'Success'})
        logger.info(response.content)
        if response.status_code == 200:
            logger.info('Change user password test passed')
        else:
            logger.error('Change user password test failed')


def test_if_admin_can_change_user_email(context, change_email, get_logger):
    logger = get_logger
    logger.info('Test: Admin Change user Email starts')
    response, response_json = company.change_user_email(change_email, admin=True)
    with soft_assertions():
        assert_that(response.status_code).is_equal_to(200)
        assert_that(response_json).is_equal_to({'details': 'Success'})
        logger.info(response_json)
        if response.status_code == 200:
            logger.info('Admin Change user Email test passed')
        else:
            logger.error('Admin Change user Email test failed')


def test_if_user_change_email(context, change_email, get_logger):
    logger = get_logger
    logger.info('Test: Change user Email starts')
    response, response_json = company.change_user_email(change_email, admin=False)
    with soft_assertions():
        assert_that(response.status_code).is_equal_to(200)
        assert_that(response_json).is_equal_to({'details': 'Success'})
        logger.info(response_json)
        if response.status_code == 200:
            logger.info('Change user Email test passed')
        else:
            logger.error('Change user Email test failed')


def test_refresh_access_token(context, get_logger):
    logger = get_logger
    logger.info('Test: Refresh access token starts')
    response = company.refresh_access_token()
    with soft_assertions():
        assert_that(response.status_code).is_equal_to(200)
        assert_that(response.content).is_equal_to({'detail': 'Success'})
        if response.status_code == 200:
            logger.info('Refresh access token test passed')
        else:
            logger.error('Refresh access token test failed')


def test_if_user_can_logout(get_logger):
    logger = get_logger
    logger.info('Test: User logout starts')
    response = company.user_logout()
    with soft_assertions():
        logger = get_logger
        assert_that(response.status_code).is_equal_to(200)
        assert_that(response.content).is_equal_to({'details': 'Success'})
        logger.info(response.content)
        if response.status_code == 200:
            logger.info('User logged out test passed')
        else:
            logger.error('User logged out test failed')


def test_admin_can_force_logout_user(context, user_id, get_logger):
    logger = get_logger
    logger.info('Test: Admin can force logout user starts')
    response = company.force_logout(user_id)
    with soft_assertions():
        assert_that(response.status_code).is_equal_to(200)
        assert_that(response.content).is_equal_to({'details': 'Success'})
        logger.info(response.content)
        if response.status_code == 200:
            logger.info('Admin can force logout user test passed')
        else:
            logger.error('Admin can force logout user failed')


@pytest.mark.skip(reason={'detail': 'Not Found'})
def test_if_admin_can_delete_user(context, user_id, get_logger):
    logger = get_logger
    logger.info('Test: Delete user starts')
    response = company.delete_user(user_id)
    with soft_assertions():
        assert_that(response.status_code).is_equal_to(200)
        assert_that(response.content).is_equal_to({'details': 'Success'})
        logger.info(response.content)
        if response.status_code == 200:
            logger.info('Delete user test passed')
        else:
            logger.error('Delete user test failed')
