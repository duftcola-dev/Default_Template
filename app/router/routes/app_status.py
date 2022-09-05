from flask import Blueprint,request,current_app
from app.utils.response.response import create_response
from datetime import datetime

bp = Blueprint("status",__name__,url_prefix="/")

@bp.before_app_request
def request_metadata():
    method = request.method
    base = request.base_url
    date = str(datetime.utcnow().strftime("%d/%m/%d-%H:%M:%S"))
    current_app.logger.info(f"{date} - {method}| {base}")

@bp.route("/")
def app_status():
    payload = {"OK":1}
    return create_response(payload,200)




