import os
import logging
from flask import Flask
from dotenv import dotenv_values
basedir = os.path.abspath(os.path.dirname(__file__))

class AppConfig:

    def __init__(self) -> None:
        pass

    def init_app(self,app:Flask)->Flask:
        self.path=os.getcwd()+"/app/config"
        app = self.__set_configuration(app)
        app = self.__set_gunicorn_logger(app)
        return app

    def __set_configuration(self,app:Flask)->Flask:
        """Set app configuration based on the current ENV

        Args:
            app (Flask): Flask class instance

        Returns:
            Flask: Flask class instance
        """
        if app.config["ENV"] == "development":
            values = dotenv_values(self.path+"/develop/.env")
        if app.config["ENV"] == "production":
            values = dotenv_values(self.path+"/production/.env")
        if app.config["ENV"] == "test":
            values = dotenv_values(self.path+"/test/.env")
        app.config.from_mapping(values)
        return app


    def __set_gunicorn_logger(self,app:Flask)->Flask:
        """Sets the flask app logger to the same level of the 
        the Gunicorn logger so every log of the app can be passed
        to the host wsgi and be seen in console during development.

        Args:
            app (Flask): Flask instance app

        Returns:
            Flask: Flask instance app
        """
        gunicorn_logger = logging.getLogger("gunicorn.error")
        app.logger.handlers = gunicorn_logger.handlers
        app.logger.setLevel(gunicorn_logger.level)
        return app 