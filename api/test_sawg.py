from swag_req import create_user, user_login, get_user_data, user_logout, delete_user
import allure


@allure.story('User creation')
def test_create_user():
    user_data = {
        "id": 157,
        "username": "petstore_user",
        "firstName": "Natalia",
        "lastName": "Iv",
        "email": "petstore@test.com",
        "password": "Petstore",
        "phone": "12938476",
        "userStatus": 2
    }
    response = create_user(user_data)
    with allure.step('Check status code when creating user'):
        assert response.status_code == 200, "User not created"


@allure.story('User login')
def test_user_login():
    username = 'petstore_user'
    password = 'Petstore'
    response = user_login(username, password)
    with allure.step('Check status code when user login'):
        assert response.status_code == 200, "User not logged in"


@allure.story('Get user data')
def test_user_data():
    username = 'petstore_user'
    response = get_user_data(username)
    with allure.step('Check status code when getting user data'):
        assert response.status_code == 200, "User data not received"


@allure.story('User logout')
def test_user_logout():
    response = user_logout()
    with allure.step('Check status code when user logout'):
        assert response.status_code == 200, "User not logged out"


@allure.story('User deleting')
def test_delete_user():
    username = 'petstore_user'
    response = delete_user(username)
    with allure.step('Check status code when deleting a user'):
        assert response.status_code == 200, "User not deleted"
