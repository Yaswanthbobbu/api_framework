from assertpy import assert_that, soft_assertions
from services.project_service import Project
project = Project()


def test_if_user_can_create_project(context, create_project, get_logger):
    logger = get_logger
    logger.info('Test: create project starts')
    response = project.create_project(create_project)
    with soft_assertions():
        assert_that(response.status_code).is_equal_to(200)
        logger.info(response.content)
        assert_that(response.content["details"]).contains("Success")
        if response.status_code == 200:
            logger.info('create project test passed')
        else:
            logger.error('create project test failed')
    context["project_id"] = project.create_project(create_project).content["projectId"]


def test_if_user_can_fetch_project(context, get_logger):
    logger = get_logger
    logger.info('Test: fetch project starts')
    response = project.fetch_project(context.get("project_id"))
    with soft_assertions():
        assert_that(response.status_code).is_equal_to(200)
        logger.info(response.content)
        assert_that(response.content["details"]).is_equal_to("Success")
        if response.status_code == 200:
            logger.info('fetch project test passed')
        else:
            logger.error('fetch project test failed')


def test_if_user_can_update_project(context, update_project, get_logger):
    logger = get_logger
    logger.info('Test: update project starts')
    response = project.update_project(context.get("project_id"), update_project)
    with soft_assertions():
        assert_that(response.status_code).is_equal_to(200)
        logger.info(response.content)
        assert_that(response.content).contains("Success")
        if response.status_code == 200:
            logger.info('update project test passed')
        else:
            logger.error('update project test failed')


def test_if_user_can_upload_project_file(context, update_project_file, get_logger):
    logger = get_logger
    logger.info('Test: upload project file starts')
    response = project.upload_project_file(context.get("project_id"), update_project_file)
    with soft_assertions():
        assert_that(response.status_code).is_equal_to(201)
        logger.info(response.content)
        assert_that(response.content).is_empty()
        if response.status_code == 200:
            logger.info('upload project file test passed')
        else:
            logger.error('upload project file test failed')