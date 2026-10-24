def assert_successful_response(response):
    assert response.status_code == 200

def assert_user_data(user,expected_id):
    assert user["id"] == expected_id
    assert user["name"]
    assert user["username"]
    assert user["email"]
    assert isinstance(user["id"], int)
    assert isinstance(user["name"], str)