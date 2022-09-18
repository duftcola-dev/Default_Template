from ..validator import *
from typing import Tuple
import json

v = Validator()

# Custom error class
class Error:
    def __init__(self,error:str) -> None:
        self.error=error 
    
    def __call__(self):
        print(self.error)
        return self.error

# Validation method for a model
def custom_validation_method(name:str)->bool:
    """Check if a string is n size"""
    if len(name) > 10:
        raise Exception("The field is bigger that size")
    return name

# Simple model
class Token(BaseModel):
    token:str 
    payload:str

# Complex model that include Token
class Example(BaseModel):
    id:int
    name:str 
    token:Token
    __token_length = v.validate_field("name",custom_validation_method)

def model(model,payload)->Tuple[dict,Error]:
    try:
        example = model(**payload).dict()
        return example,None
    except Exception as err:
        return None,Error(str(err))

def test_model():
    payload={'id': 1, 'name': 'Robin', 'token': {'token': 'Some token', 'payload': 'some payload'}}
    result,error = model(Example,payload)
    assert error is None 
    assert isinstance(result,dict)

def test_model_fail():
    payload={'id': 1, 'name': 'Robin', 'token': {'token': 'Some token'}}
    result,error = model(Example,payload)
    assert result is None 
    assert error is not None
    assert isinstance(error(),str) == True

def test_model_check_token_lenght_fail():
    payload={'id': 1, 'name': 'Some veryyyy loong name', 'token': {'token': 'Some token', 'payload': 'some payload'}}
    result,error = model(Example,payload)
    assert result is None
    assert error is not None

def test_get_instance():
    temp = v.get_instance()
    assert temp.__class__.__name__ == "Validator"
    assert isinstance(temp.get_instance,Callable) == True
    
def test_validate_request():
    payload={'id': 1, 'name': 'Robin', 'token': {'token': 'Some token', 'payload': 'some payload'}}
    class f_request:
        def __init__(self) -> None:
            pass
    r = f_request()
    r.json=payload
    result,error = v.validate_request(r,Example)
    assert error is None
    assert result.name is not None
    assert result.name == "Robin"
    assert isinstance(result.dict(),dict) == True
    assert result.dict()["name"] == "Robin"

def test_custom_error():
    e = Error("some error")
    assert isinstance(e.error,str) == True
    assert e.error == "some error"
    assert e() == "some error"



    
