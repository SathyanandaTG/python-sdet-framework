def assert_successful_response(response):
    assert response.status_code == 200
    assert "application/json" in response.headers["Content-Type"]

def assert_user_data(user,expected_id):
    assert user["id"] == expected_id
    assert isinstance(user["name"], str)
    assert isinstance(user["username"], str) and user["username"]
    assert isinstance(user["email"], str) and user["email"]
    assert isinstance(user["id"], int)
    assert "@" in user["email"]
    assert isinstance(user["name"], str) and user["name"] 
