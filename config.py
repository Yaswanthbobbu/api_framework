

"""<<<<<<<<<<<<<<<<<<<<<<<<<<<<<--urls-->>>>>>>>>>>>>>>>>>>>>>>>>>>"""

base_url = 'https://devapi.iprosuite.com'

# Authentication
register_company_endpoint = '/auth/register-company'
verify_user_endpoint = '/auth/verify-user'
login_endpoint = '/auth/login'
logout_endpoint = '/auth/logout'
force_logout_endpoint = '/auth/force-logout'
create_user_endpoint = '/auth/create-user'
change_user_email_endpoint = '/auth/change-user-email'
change_user_password_endpoint = '/auth/change-password'
refresh_access_token_endpoint = '/auth/refresh-access-token'
delete_user_endpoint = '/delete-user'

# Clients
fetch_client_endpoint = '/clients/fetch-client/{client_id}'
create_client_endpoint = '/clients/create-client'
update_client_endpoint = '/clients/update-client/{client_id}'
upload_client_file_endpoint = '/clients/upload-file/{client_id}'
fetch_client_file_endpoint = '/clients/fetch-files/{client_id}'

# Users
fetch_user_endpoint = '/users/fetch-user/{user_id}'
fetch_current_user_endpoint = '/users/fetch-current-user'
update_user_endpoint = '/users/udpate-user/{user_id}'
upload_user_file_endpoint = '/users/upload-file/{user_id}'
fetch_user_file_endpoint = '/users/fetch-files/{user_id}'

# Projects
fetch_project_endpoint = '/projects/fetch-projects/{project_id}'
create_project_endpoint = '/projects/create-project'
update_project_endpoint = '/projects/update-project/{project_id}'
upload_project_file_endpoint = '/projects/upload-file/{project_id}'

# Estimates
fetch_estimate_endpoint = '/estimates/fetch-estimate/{estimate_id}'
create_estimate_endpoint = '/estimates/create-estimate'
update_estimate_endpoint = '/estimates/update-estimate/{estimate_id}'
upload_estimate_file_endpoint = '/estimates/upload-file/{estimate_id}'
fetch_estimate_file_endpoint = '/estimates/fetch-files/{estimate_id}'
