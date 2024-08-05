import pytest
from assertpy import assert_that, soft_assertions
from services.register_company_service import RegisterCompany

company = RegisterCompany()


def test_if_new_company_can_be_registered(context, company_payload):
    response = company.register_company(company_payload)
    with soft_assertions():
        assert_that(response.status_code).is_equal_to(200)
        assert_that(response.as_dict).is_not_empty()
        assert_that(response.as_dict).contains("Success")
        assert_that(response.as_dict["details"]).is_not_none()


def test_if_user_can_login(context):
    response = company.user_login(context)
    with soft_assertions():
        assert_that(response.status_code).is_equal_to(200)
        assert_that(response.as_dict).is_not_empty()


def test_user_verification(context, verify_user_payload):
    response = company.user_login(verify_user_payload)
    with soft_assertions():
        assert_that(response.status_code).is_equal_to(200)
        assert_that(response.as_dict).is_not_empty()


def test_if_admin_can_create_user(context, create_admin_payload):
    response = company.create_user(create_admin_payload)
    with soft_assertions():
        assert_that(response.status_code).is_equal_to(201)
        assert_that(response.as_dict).is_empty()


def test_if_admin_can_change_user_password(context, change_password_payload):
    response = company.change_user_password(context.get("user_id"), change_password_payload)
    with soft_assertions():
        assert_that(response.status_code).is_equal_to(201)
        assert_that(response.as_dict).is_empty()


def test_if_user_change_password(context, change_email_payload):
    response = company.change_user_password(context, change_email_payload)
    with soft_assertions():
        assert_that(response.status_code).is_equal_to(201)
        assert_that(response.as_dict).is_empty()


def test_if_admin_can_change_user_email(context, change_email_payload):
    response = company.change_user_email(context.get("user_id"), change_email_payload)
    with soft_assertions():
        assert_that(response.status_code).is_equal_to(201)
        assert_that(response.as_dict).is_empty()


def test_if_user_change_email(context, change_email_payload):
    response = company.change_user_email(context, change_email_payload)
    with soft_assertions():
        assert_that(response.status_code).is_equal_to(201)
        assert_that(response.as_dict).is_empty()


def test_refresh_access_token():
    response = company.refresh_access_token()
    with soft_assertions():
        assert_that(response.status_code).is_equal_to(201)
        assert_that(response.as_dict).is_empty()


def test_if_user_can_logout():
    response = company.user_logout()
    with soft_assertions():
        assert_that(response.status_code).is_equal_to(201)
        assert_that(response.as_dict).is_empty()


def test_admin_can_force_logout_user(context):
    response = context.force_logout_user(context.get("user_id"))
    with soft_assertions():
        assert_that(response.status_code).is_equal_to(201)
        assert_that(response.as_dict).is_empty()


def test_if_admin_can_delete_user(context):
    response = company.delete_user(context.get("user_id"))
    with soft_assertions():
        assert_that(response.status_code).is_equal_to(201)
        assert_that(response.as_dict).is_empty()
