import pytest
import json
import requests

def test_login_valid():
    url = 'https://reqres.in/api/login'
    data = {'email':'eve.holt@reqres.in', 'password':'cityslicka'}
    response = requests.post(url, data=data)
    token = json.loads(response.text)
    print(response)
    print(response.text)
    if type(response.text) is str:
        print('Is string')
    if type(token) is dict:
        print("Is dictionary")
    print(token)
    assert token['token'] == 'QpwL5tke4Pnpja7X4'
    assert response.status_code == 200

#test_login_valid()

url = 'https://reqres.in/api/users?page=2'
data = {'email':'eve.holt@reqres.in', 'password':'cityslicka'}
response = requests.get(url)
print(response.json())
print(response.text)

users = json.loads(response.text)
print("Total:", users["total"])
print("User id 7:", users["data"][0]["first_name"], users["data"][0]["last_name"], "avatar: ", users["data"][0]["avatar"])
