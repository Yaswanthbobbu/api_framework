from assertpy import assert_that, soft_assertions
from services.client_service import Client

client = Client()


def test_if_user_can_create_client(context, create_client, get_logger):
    logger = get_logger
    logger.info('Test: create client starts')
    response = client.create_client(create_client)
    with soft_assertions():
        assert_that(response.status_code).is_equal_to(201)
        logger.info(response.content)
        assert_that(response.content).contains("newID")
        assert_that(response.content["details"]).contains("Success")
        if response.status_code == 201:
            logger.info('create client test passed')
            if "newID" in response.content:
                context["client_id"] = response.content.get("newID")
            else:
                logger.error("'newID' key not found in response content")
        else:
            logger.error('create client test failed')
    context["client_id"] = response.content.get("newID")
    if context["client_id"] is None:
        logger.info('Failed to extract client ID from response')


def test_if_user_can_fetch_client(context, get_logger):
    logger = get_logger
    logger.info('Test: fetch client starts')
    response = client.fetch_client(context.get("client_id"))
    with soft_assertions():
        logger.info(response.content)
        assert_that(response.status_code).is_equal_to(201)
        assert_that(response.content).is_not_empty()
        assert_that(response.content["clientType"]).is_equal_to("Corporate")
        assert_that(response.content["clientName"]).is_equal_to("Tech Solutions Inc.")
        logger.info(response.content)
        if response.status_code == 201:
            logger.info('fetch client test passed')
        else:
            logger.error('fetch client test failed')


def test_if_user_can_update_client(context, update_client, get_logger):
    logger = get_logger
    logger.info('Test: update client starts')
    response = client.update_client(context.get("client_id"), update_client)
    with soft_assertions():
        logger.info(response.content)
        assert_that(response.status_code).is_equal_to(201)
        assert_that(response.content).is_not_empty()
        assert_that(response.content["clientName"]).is_equal_to("Tech Innovations Inc.")
        assert_that(response.content["postcode"]).is_equal_to("T1234C")
        if response.status_code == 201:
            logger.info('update client test passed')
        else:
            logger.error('update client test failed')


def test_if_user_can_upload_client_file(context, file_path, additional_data, get_logger):
    logger = get_logger
    logger.info('Test: upload client file starts')
    response = client.upload_client_file(context.get("client_id"), file_path, additional_data)
    with soft_assertions():
        logger.info(response.content)
        assert_that(response.status_code).is_equal_to(201)
        assert_that(response.text).is_empty()
        if response.status_code == 201:
            logger.info('Upload client file test passed')
        else:
            logger.error('Upload client file test failed')


def test_if_user_can_fetch_client_files(context, fetch_client_files, get_logger):
    logger = get_logger
    logger.info('Test: fetch client files starts')
    response = client.fetch_client_files(context.get("client_id"), fetch_client_files)
    with soft_assertions():
        logger.info(response.content)
        assert_that(response.status_code).is_equal_to(201)
        response.raise_for_status()
        assert_that(response.content).is_not_empty()
        assert_that(response.content).contains("client_id")
        for file in response.content.get("files", []):
            assert_that(file).contains("client_id")
        if response.status_code == 201:
            logger.info('Upload client file test passed')
        else:
            logger.error('Upload client file test failed')

