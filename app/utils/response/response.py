from flask import make_response
import json
def create_response(content:dict,status:int,type = "application/json")->dict:
    response = make_response(content,status)
    response.mimetype = type
    response.content_encoding="utf-8"
    return response