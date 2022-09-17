from flask import Flask
from .deppendencies import Deppendencies

class App:
    """Creates the main app instance
    """

    def __init__(self) -> None:
        pass

    def init_app(self)->Flask:
        """Initializes app and load deppendencies
        """
        app = Flask(__name__)
        app = Deppendencies().load(app)
        return app
