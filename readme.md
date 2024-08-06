api-framework-python/

├─ logs/
├─ services/
│  ├─ base_service.py
│  ├─ client_service.py
│  ├─ project_service.py  
│  ├─ register_company_service.py
├─ tests/
│  ├─ data/
│  │  ├─ create_client.json
│  │  ├─ update_client.json
│  │  ├─ .....
│  ├─ test_clients.py
│  ├─ test_projects.py
│  ├─ test_register_company.py
├─ utils/
│  ├─ file_reader.py 
│  ├─ service_requests.py
├─ .env
├─ .gitignore
├─ config.py
├─ conftest.py
├─ pipfile
├─ pytest.ini
├─ readme.md
├─ requirements.txt


Test Execution 

# Run tests via pytest (single threaded verbose)
cd tests
pytest -v test.sample.py

# Run tests via pytest (print & verbose)
cd tests
pytest -s -v test.sample.py

# Run tests in parallel
pytest -n auto

# Report results to report portal
pytest -n auto ./tests --reports