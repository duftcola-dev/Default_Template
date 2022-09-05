from tests.utils import basic

def test_app_status(client):
    response = client.get("/")
    basic.check_200(response)

