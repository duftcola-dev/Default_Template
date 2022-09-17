from flask import Blueprint,request,make_response,render_template
from .forms import ExampleForm

bp = Blueprint("status",__name__,url_prefix="/")

@bp.route("/")
def app_status():
    payload = {"OK":1}
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




