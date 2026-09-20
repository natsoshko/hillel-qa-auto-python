import logging
import os

import pytest
import requests
from requests.auth import HTTPBasicAuth

BASE_URL = "http://127.0.0.1:8081"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE_DIR, "test_search.log")

# =========================================================
# Logging configuration
# =========================================================

logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

file_handler = logging.FileHandler(LOG_FILE, mode="a", encoding="utf-8")
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

# =========================================================
# Fixtures
# =========================================================

@pytest.fixture(scope="class")
def session():
    session = requests.Session()
    logger.info("Starting authentication...")

    response = session.post(f"{BASE_URL}/auth", auth=HTTPBasicAuth("test_user", "test_pass"))
    logger.info("POST /auth -> status: %s", response.status_code)
    assert response.status_code == 200
    access_token = response.json()["access_token"]
    session.headers.update({"Authorization": f"Bearer {access_token}"})
    logger.info("Authentication successful")
    yield session

    session.close()
    logger.info("Session closed")