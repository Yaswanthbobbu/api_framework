"""<<<<<<<<<<<<<<<<<<<<<<<<<<<<<--CREDENTIALS-->>>>>>>>>>>>>>>>>>>>>>>>>>>"""

BASE_URL = 'https://devapi.iprosuite.com'

# Authentication
REGISTER_COMPANY_ENDPOINT = '/auth/register-company'
VERIFY_USER_ENDPOINT = '/auth/verify-user'
LOGIN_ENDPOINT = '/auth/login'
LOGOUT_ENDPOINT = '/auth/logout'
FORCE_LOGOUT_ENDPOINT = '/auth/force-logout/{userID}'
CREATE_USER_ENDPOINT = '/auth/create-user'
CHANGE_USER_EMAIL_ENDPOINT = '/auth/change-user-email/{admin}'
CHANGE_USER_PASSWORD_ENDPOINT = '/auth/change-password/{admin}'
REFRESH_ACCESS_TOKEN_ENDPOINT = '/auth/refresh-access-token'
DELETE_USER_ENDPOINT = '/delete-user/{userID}'

# Clients
FETCH_CLIENT_ENDPOINT = '/clients/fetch-client/{client_id}'
CREATE_CLIENT_ENDPOINT = '/clients/create-client'
UPDATE_CLIENT_ENDPOINT = '/clients/update-client/{client_id}'
CLIENT_UPLOAD_FILE_ENDPOINT = '/clients/upload-file/{client_id}'
CLIENT_FETCH_FILE_ENDPOINT = '/clients/fetch-files/{client_id}'

# Users
FETCH_USER_ENDPOINT = '/users/fetch-user/{user_id}'
FETCH_CURRENT_USER_ENDPOINT = '/users/fetch-current-user'
UPDATE_USER_ENDPOINT = '/users/udpate-user/{user_id}'
USER_UPLOAD_FILE_ENDPOINT = '/users/upload-file/{user_id}'
USER_FETCH_FILE_ENDPOINT = '/users/fetch-files/{user_id}'

# Projects
FETCH_PROJECT_ENDPOINT = '/projects/fetch-projects/{project_id}'
CREATE_PROJECT_ENDPOINT = '/projects/create-project'
UPDATE_PROJECT_ENDPOINT = '/projects/update-project/{project_id}'
PROJECT_UPLOAD_FILE_ENDPOINT = '/projects/upload-file/{project_id}'


# Estimates
FETCH_ESTIMATE_ENDPOINT = '/estimates/fetch-estimate/{estimate_id}'
CREATE_ESTIMATE_ENDPOINT = '/estimates/create-estimate'
UDPATE_ESTIMATE_ENDPOINT = '/estimates/update-estimate/{estimate_id}'
ESTIMATE_UPLOAD_FILE_ENDPOINT = '/estimates/upload-file/{estimate_id}'
ESTIMATE_FETCH_FILEENDPOINT = '/estimates/fetch-files/{estimate_id}'
