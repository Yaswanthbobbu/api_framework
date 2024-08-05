from assertpy import assert_that, soft_assertions
from services.project_service import Project
project = Project()


def test_if_user_can_create_project(context, create_project):
    response = project.create_project(create_project)
    with soft_assertions():
        assert_that(response.status_code).is_equal_to(200)
        assert_that(response.as_dict).is_not_empty()
        assert_that(response.as_dict).contains("Success")
        assert_that(response.as_dict["details"]).is_not_none()
    context["project_id"] = project.create_project(create_project).as_dict["projectId"]


def test_if_user_can_fetch_project(context):
    response = project.fetch_project(context.get("project_id"))
    with soft_assertions():
        assert_that(response.status_code).is_equal_to(200)
        assert_that(response.as_dict).is_not_empty()
        # assert_that(response.as_dict["key"]).is_equal_to("value")


def test_if_user_can_update_project(context, update_project):
    response = project.update_project(context.get("project_id"), update_project)
    with soft_assertions():
        assert_that(response.status_code).is_equal_to(200)
        assert_that(response.as_dict).is_not_empty()
        assert_that(response.as_dict).contains("Success")


def test_if_user_can_upload_project_file(context, update_project_file):
    response = project.upload_project_file(context.get("project_id"), update_project_file)
    with soft_assertions():
        assert_that(response.status_code).is_equal_to(201)
        assert_that(response.as_dict).is_empty()
