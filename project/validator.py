from pydantic import BaseModel,validator
from typing import Tuple
from flask import Flask
from typing import Callable


class Error:
    """Custom erro class.
       It is meant to carry the output of an Exception
       out of a function.
    """
    def __init__(self,error:str) -> None:
        self.error:str=str(error)

    def __call__(self):
        print("ERROR : "+self.error) 
        return self.error

    def __str__(self):
        print("ERROR : "+self.error)


class Validator:
    """Class/extension based on pydantic meant to
    facilitate validation of data comming from requests.
    """

    def __init__(self) -> None:
        self.error = Error

    def get_instance(self):
        """Return a Validator instance

        Returns:
            Validator: self instance
        """
        return Validator()


    def validate_field(self,field:str,validation_method:Callable)->Exception:
        """Validates a field within a model.
        Requires a model field name as argument and a function

        Args:
            field (str): model field name
            validation_method (Callable): function reference

        Returns:
            Exception: Raises an exception if the validation fails
            field : Returns the provided field id the validation passed.
        """
        return validator(field,allow_reuse=True)(validation_method)


    def validate_request(self,request,model:BaseModel)->Tuple[BaseModel,Error]:
        """Validates the json data from a request and assures 
        the schema matches with that which is defined in the model class.
        If the validation suceeds then returns:\n
            BaseModel, None \n
        else returns : \n
            None , Error
        Args:
            request (_type_): flask request object
            model (BaseModel): reference model for validation

        Returns:
            BaseModel: reference model object (basically a dataclass)
            Error : custom error class
        """
        try:
            return model(**request.json),None
        except Exception as err:
            return None,self.error(err)
    

    def validate_url_params(self,request,model:BaseModel)->Tuple[BaseModel,Error]:
        """Validates the url paramters from a request and assures
        the schema matches with that which is defined in the model class.
        If the validation suceeds then returns:\n
            BaseModel, None \n
        else returns : \n
            None , Error
        Args:
            request (_type_): flask request object
            model (BaseModel): reference model for validation

        Returns:
            BaseModel: reference model object (basically a dataclass)
            Error : custom error class
        """
        try:
            formated_params=request.args.to_dict()
            return model(**formated_params),None
        except Exception as err:
            return None,self.error(err)


class AppValidator:
    """
    Description : \n
    Validation class for requests .
    This class class checks the incoming data in a request 
    follows the same structure of predefined models using 
    pydantic.
    ---> more info at :  https://pydantic-docs.helpmanual.io/
    ---
    How to use it : \n
    The class is instanciated in app.py and the resulting object 
    becomes a property app = (__Flask__).
    In order to use this Validator use : \n
    
    from flask import current_app
    current_app.validator.methods...
    ---
    Methods : \n

    - get_instance():
        - Returns an instance of the Validator class to be used else where.
    - validate_request(request,model):
        - Can be used under any context. Takes as argument 
          a request object and Model.
          Only validates data in json format present in the body of
          the request.
        - If the json schema matches the defined model returns a dataclass 
          with the json data. This data can be extracted as dict using
          the method object.dict()
        - If the json schema doesn't match the model then returns a custom Erro object.
    - validate_field(field:str,validation_method:Callable):
        - It is meant to be used inside models to add extra validations 
          to fields inside models.
        - Takes as argument the name of the field being valiated and a function that will
          perform the logic of the validation
        - What the validation method returns is up to the developer.However it is advisable to
          raise an Exception("With some error message").
    - validate_url_params(request,model):
        - Works exactly as validate_request but validate the url parameters instead of 
          json data in the body.

    """
    def __init__(self) -> None:
        pass

    def init_app(self,app:Flask)->Validator:        
        app.validator = Validator()
        return app
