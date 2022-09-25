# --------------------------------------------------------------------
# - Applications deppendencies
# -- Any deppendency or library for your project can 
# -- be loaded here. Then in your application routes.py 
# -- use from deppendencies import *
# --------------------------------------------------------------------
import os 
import sys 
import json
from flask import (
    Blueprint,
    request,
    make_response,
    render_template,
    current_app,
    session,
    redirect,
    url_for,
    flash
)

# --------------------------------------------------------------------
# - APPLICATION FORMS
# -- Declare your forms instanes here.
# --------------------------------------------------------------------

from .models.form_models.forms import ExampleForm

# --------------------------------------------------------------------
# - APPLICATION MODELS
# -- Declare your applications models here.
# -- These shall be the models used for your database with SQLAlchemy
# --------------------------------------------------------------------

# --------------------------------------------------------------------
# - APPLICATION REQUEST MODELS
# -- Declare your request validation models here.
# --------------------------------------------------------------------
from .models.request_models.example_model import Example

# --------------------------------------------------------------------
# - APPLICATION RESPONSE MODELS
# -- Declare your response validation models here.
# --------------------------------------------------------------------

