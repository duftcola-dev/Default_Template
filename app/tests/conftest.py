from ..App import *
import pytest


@pytest.fixture
def app():
    app = App().init_app()
    return app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()