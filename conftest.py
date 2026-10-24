import httpx
import pytest 

@pytest.fixture
def saucedemo_url():
    return "https://www.saucedemo.com/"

@pytest.fixture
def api_base_url():
    return "https://jsonplaceholder.typicode.com"

@pytest.fixture
def api_client(api_base_url):
   with httpx.Client(base_url=api_base_url) as client:
       yield client