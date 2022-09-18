from wtforms import *

class ExampleForm(Form):

    user_name=StringField("username")
    user_email=EmailField("email")
    text_area=TextAreaField("text")
