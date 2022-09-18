from ..app import App
import pytest


@pytest.fixture
def app():
    app = App().init_app(testing=True)
    return app

@pytest.fixture
def client(app):
    return app.test_client()

# Use only if you have created commands with click
# and added them  to app.cli.add_command(command_method_name)
# @pytest.fixture
# def runner(app):
#     return app.test_cli_runner()