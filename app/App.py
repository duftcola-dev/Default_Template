from flask import Flask
from .router.router import AppRouter
from .config.config import AppConfig
from datetime import datetime

class App:
    """Creates the main app instance
    """

    def __init__(self) -> None:
        pass

    def __app_initialized(self,app:Flask):
        date = str(datetime.utcnow().strftime("%Y/%m/%d-%H:%M:%S"))
        mode = app.config["ENV"]
        app.logger.info(f"{date} - APP RUNNING AS {mode}")

    def init_app(self)->Flask:
        """Initializes app
        """
        #deppendencies
        app = Flask(__name__)
        app_router = AppRouter()
        app_config = AppConfig()
        #initialization
        app = app_config.init_app(app)  
        app = app_router.init_app(app)
        #app
        self.__app_initialized(app)
        return app
