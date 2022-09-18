from .status_codes import *

def test_app_status(client):
    response = client.get("/")
    assert check_200(response) == True

def test_app_home(client):
    response = client.get("/home")
    assert check_200(response) == True

def test_app_form(client):
    response = client.get("/form")
    assert check_200(response) == True

def test_app_login(client):
    response = client.post("/login")
    assert check_200(response) == True

def test_model(client):
    response = client.get("/url_params_model?id=1&name=robin")
    assert check_200(response) == True

