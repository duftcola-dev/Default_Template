from ..deppendencies import *
bp = Blueprint("example",__name__,url_prefix="/")


@bp.route("/")
def app_status():
    print(os.environ.get("ENV"))
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
        session["username"]=request.form["user_name"]
        print(my_form.data)
        return render_template("login.html")
    return render_template("form.html",form=my_form)

@bp.route("/logout",methods=["GET"])
def log_out():
    session.pop("username",None)
    return redirect(url_for("example.app_status"))

@bp.route("/flash",methods=["GET"])
def send_flash_message():
    # Send flash messages
    flash("This is a flash message","info")
    flash("This is a flash message","ok")
    flash("This is a flash message","alert")
    return redirect(url_for("example.index"))

