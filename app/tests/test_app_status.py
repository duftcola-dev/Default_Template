from .utils.basic import *

def test_app_status(client):
    response = client.get("/")
    check_200(response)

