import os
import shutil
import pytest
from fastapi.testclient import TestClient
from main import app
from app.core.config import FAISS_INDEX_PATH

@pytest.fixture(scope="session")
def client():
    return TestClient(app)

@pytest.fixture(autouse=True)
def clean_faiss_index():
    # Run before EACH test
    if os.path.exists(FAISS_INDEX_PATH):
        shutil.rmtree(FAISS_INDEX_PATH)
    yield
    # Run after EACH test
    if os.path.exists(FAISS_INDEX_PATH):
        shutil.rmtree(FAISS_INDEX_PATH)
