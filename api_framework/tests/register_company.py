from assertpy import assert_that, soft_assertions

from api_framework.services.class_service import RegisterCompany

company = RegisterCompany()


def test_if_new_company_can_be_registered(context, create_data):
    response = company.create_booking(create_data)
    with soft_assertions():
        assert_that(response.status_code).is_equal_to(200)
        assert_that(response.as_dict).is_not_empty()
        assert_that(response.as_dict).contains("bookingid")
        assert_that(response.as_dict["bookingid"]).is_not_none()
    context["booking_id"] = company.create_booking(create_data).as_dict["bookingid"]


def test_if_new_booking_can_be_fetched(context):
    response = company.get_booking(context.get("booking_id"))
    with soft_assertions():
        assert_that(response.status_code).is_equal_to(200)
        assert_that(response.as_dict).is_not_empty()
        assert_that(response.as_dict["firstname"]).is_equal_to("John")
        assert_that(response.as_dict["lastname"]).is_equal_to("Wick")


def test_if_new_booking_can_be_updated(context, update_data):
    response = company.update_booking(context.get("booking_id"), update_data)
    with soft_assertions():
        assert_that(response.status_code).is_equal_to(200)
        assert_that(response.as_dict).is_not_empty()
        assert_that(response.as_dict["additionalneeds"]).is_equal_to("Dinner")


def test_if_new_booking_can_be_deleted(context):
    response = company.delete_booking(context.get("booking_id"))
    with soft_assertions():
        assert_that(response.status_code).is_equal_to(201)
        assert_that(response.as_dict).is_empty()