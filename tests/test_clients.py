from assertpy import assert_that, soft_assertions
from services.client_service import Client

client = Client()


def test_if_user_can_create_client(context, create_client):
    response = client.create_client(create_client)
    with soft_assertions():
        assert_that(response.status_code).is_equal_to(200)
        assert_that(response.content["details"]).contains("Success")
    context["client_id"] = client.create_client(create_client).as_dict["clientId"]


def test_if_user_can_fetch_client(context):
    response = client.fetch_client(context.get("client_id"))
    with soft_assertions():
        assert_that(response.status_code).is_equal_to(200)
        assert_that(response.content["details"]).is_equal_to("Success")


def test_if_user_can_update_client(context, update_client):
    response = client.update_client(context.get("client_id"), update_client)
    with soft_assertions():
        assert_that(response.status_code).is_equal_to(200)
        assert_that(response.content).contains("Success")


def test_if_user_can_upload_client_file(context, update_client_file):
    response = client.upload_client_file(context.get("client_id"), update_client_file)
    with soft_assertions():
        assert_that(response.status_code).is_equal_to(201)
        assert_that(response.content).is_empty()


def test_if_user_can_fetch_client_files(context, fetch_client_files):
    response = client.upload_client_file(context.get("client_id"), fetch_client_files)
    with soft_assertions():
        assert_that(response.status_code).is_equal_to(201)
        assert_that(response.content).is_empty()
