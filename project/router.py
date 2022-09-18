from flask import Flask
from .applications.example.routes import bp as app_status_bp

class AppRouter:

    def __init__(self) -> None:
        pass
        
    def init_app(self,app:Flask):
        """Register app blueprints and  endpoints

        Args:
            app (Flask): Flask class instance
        """
        
        app.register_blueprint(app_status_bp)
        return app