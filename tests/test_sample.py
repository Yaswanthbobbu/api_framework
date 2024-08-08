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
        assert_that(response.content["details"]).contains("Success")
        if response.status_code == 200:
            logger.info('create client test passed')
        else:
            logger.error('create client test failed')
    # newID = '66b4c93941cda67aca2c4604'
    context["client_id"] = client.create_client(create_client).content["newID"]


def test_if_user_can_fetch_client(context, create_client, get_logger):
    logger = get_logger
    logger.info('Test: fetch client starts')
    newID = '66b4c93941cda67aca2c4604'
    context["client_id"] = client.create_client(create_client).content["newID"]
    response = client.fetch_client(context.get("client_id"))
    with soft_assertions():
        assert_that(response.status_code).is_equal_to(200)
        logger.info(response.content)
        assert_that(response.content["details"]).is_equal_to("Success")
        if response.status_code == 200:
            logger.info('fetch client test passed')
        else:
            logger.error('fetch client test failed')


def test_if_user_can_update_client(context, update_client, get_logger):
    logger = get_logger
    logger.info('Test: update client starts')
    y = context.get("client_id")
    response = client.update_client(context.get("client_id"), update_client)
    with soft_assertions():
        assert_that(response.status_code).is_equal_to(200)
        logger.info(response.content)
        assert_that(response.content).contains("Success")
        if response.status_code == 200:
            logger.info('update client test passed')
        else:
            logger.error('update client test failed')

