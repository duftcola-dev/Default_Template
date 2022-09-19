from ..app import App
import pytest


@pytest.fixture
def app():
    app = App().init_app(testing=True)
    app.testing=True 
    app.config.from_mapping(
    SECRET_KEY="0537d44f1ff7b89501cba9b1b773e1ef368c0f5a98b20c38e0504c726e7f9404"
    )
    return app

@pytest.fixture
def client(app):
    return app.test_client()

# Use only if you have created commands with click
# and added them  to app.cli.add_command(command_method_name)
# @pytest.fixture
# def runner(app):
#     return app.test_cli_runner()