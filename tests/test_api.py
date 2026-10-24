
import pytest
from  tests.api_helpers import assert_successful_response, assert_user_data

def test_get_user(api_client):
    response =api_client.get("/users/1")
    assert_successful_response(response)
    user = response.json()
    assert_user_data(user, 1)

def test_get_nonexistent_user(api_client):
    response = api_client.get("/users/9999")
    assert response.status_code == 404

@pytest.mark.parametrize("user_id", [1, 2, 3])
    
def test_get_multiple_users(user_id, api_client):
    response = api_client.get(f"/users/{user_id}")
    assert_successful_response(response)
    user = response.json()
    assert_user_data(user, user_id)