from flask import Flask,request,current_app
from .router import AppRouter
from .config.config import AppConfig
from datetime import datetime

class Deppendencies():

    def __init__(self) -> None:
        pass
    
    def __app_meta_info(self):
        method = request.method
        base = request.base_url
        date = str(datetime.utcnow().strftime("%d/%m/%d-%H:%M:%S"))
        current_app.logger.info(f"{date} - {method} | {base}")
    
    def load(self,app:Flask)->Flask:
        #app
        app.before_request(self.__app_meta_info)
        #deppendencies
        app = AppRouter().init_app(app)  
        app = AppConfig().init_app(app)
        return app

    
