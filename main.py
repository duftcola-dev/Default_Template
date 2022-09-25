# Deppendencies
from flask import Flask,request,current_app
from project.router import AppRouter
from project.config.config import AppConfig
from project.validator import AppValidator
from project.handlers import AppHandler
from datetime import datetime
# Routes
from applications.routes import routes

class App:
    """Creates the main app instance
    """

    def __init__(self) -> None:
        pass

    def init_app(self,testing=False)->Flask:
        """Initializes app and load deppendencies
        """
        app = Flask(__name__)
        if testing==True:
            app.testing=True
            app.config["ENV"] = "testing"
        app = self.__init(app)
        return app

    def __app_request_metadata(self):
        method = request.method
        base = request.base_url
        date = str(datetime.utcnow().strftime("%d/%m/%d-%H:%M:%S"))
        current_app.logger.info(f"{date} - {method} | {base}")
    
    def __init(self,app:Flask)->Flask:
        #request log metadata
        app.before_request(self.__app_request_metadata)
        #deppendencies
        app = AppRouter().init_app(app,routes)  
        app = AppConfig().init_app(app)
        app = AppValidator().init_app(app)
        app = AppHandler().init_app(app)
        return app



app = App().init_app()
