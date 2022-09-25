from flask import Flask
class AppRouter:

    def __init__(self) -> None:
        pass
        
    def init_app(self,app:Flask,routes:list):
        """Register app blueprints and  endpoints

        Args:
            app (Flask): Flask class instance
        """
        for route in routes:
            app.register_blueprint(route)
        return app