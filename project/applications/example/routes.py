from flask import Blueprint,request,make_response,render_template,current_app
from .forms import ExampleForm
from .models.request_models.example_model import Example

bp = Blueprint("status",__name__,url_prefix="/")

@bp.route("/")
def app_status():
    payload = {"OK":1}
    return make_response(payload,200)

@bp.route("/body_json_model",methods=["GET","POST"])
def model():
    # It expects a json payload like this :
    # {id:1,name:some_name}
    result,error = current_app.validator.validate_request(request,Example)
    payload = result.dict()
    return make_response(payload,200)

@bp.route("/url_params_model",methods=["GET"])
def model2():
    # It expects an url with the following paramters :
    # ?id=1&name=some_name
    result,error = current_app.validator.validate_url_params(request,Example)
    payload = result.dict()
    return make_response(payload,200)

@bp.route("/home")
def index():
    return render_template("home.html")

@bp.route("/form")
def form():
    my_form=ExampleForm(request.form)
    return render_template("form.html",form=my_form)

@bp.route("/login",methods=["POST"])
def login():
    my_form=ExampleForm(request.form)
    if my_form.validate():
        print(my_form.data)
        return render_template("login.html")
    return render_template("form.html",form=my_form)




