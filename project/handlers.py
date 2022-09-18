from flask import Flask,render_template
class AppHandler:
    """Define your generic and custom exeption here.
    """

    def __init__(self) -> None:
        pass

    def page_not_found(self,e):
        return render_template("error.html")

    def init_app(self,app:Flask)->Flask:
        app.register_error_handler(404,self.page_not_found)
        return app