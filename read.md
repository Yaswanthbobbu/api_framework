
this is api testing framework 

url : https://devapi.iprosuite.com/docs#/

pip install -r requirements.txt

PROJECT STRUCTURE 

api_testing/
│
├── config/
│   ├── __init__.py
│   ├── config.py
│   └── endpoints.py
├── data/
│   ├── register_company.json
│   └── ...
├── tests/
│   ├── __init__.py
│   ├── test_auth.py
│   ├── test_company.py
│   ├── test_user_management.py
│   ├── test_projects.py
│   ├── test_clients.py
│   ├── test_estimates.py
│   └── utils.py
├── pytest.ini
├── read.md
└── requirements.txt


Test Execution 

# Run tests via pytest (single threaded)
python -m pytest

# Run tests in parallel
python -m pytest -n auto

# Report results to report portal
python -m pytest -n auto ./tests --reports