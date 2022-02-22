import requests


def create_user(user_data):
    response = requests.post('https://petstore.swagger.io/v2/user', json=user_data)
    return response


def user_login(username, password):
    response = requests.get(f'https://petstore.swagger.io/v2/user/login?username={username}&password={password}')
    return response


def get_user_data(username):
    response = requests.get(f'https://petstore.swagger.io/v2/user/{username}')
    return response


def user_logout():
    response = requests.get('https://petstore.swagger.io/v2/user/logout')
    return response


def delete_user(username):
    response = requests.delete(f'https://petstore.swagger.io/v2/user/{username}')
    return response
