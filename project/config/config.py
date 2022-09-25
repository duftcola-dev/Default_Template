import pathlib
import os
import logging
from flask import Flask
from dotenv import dotenv_values
ROOT=str(pathlib.Path(__file__).resolve().parent.parent)
CONFIG=str(pathlib.Path(__file__).resolve().parent)
ENV=os.environ.get("ENV")

class AppConfig:

    def __init__(self) -> None:
        pass

    def init_app(self,app:Flask)->Flask:
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
        values={}
        if ENV == "development":
            values = dotenv_values(CONFIG+"/develop/.env")
        if ENV == "production":
            values = dotenv_values(CONFIG+"/production/.env")
        if ENV == "testing" or app.testing==True:
            values = dotenv_values(CONFIG+"/testing/.env")
        app.config.from_mapping(values)
        app.template_folder=ROOT+"/"+values["TEMPLATE_FOLDER"]
        app.static_folder=ROOT+"/"+values["STATIC_FOLDER"]
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