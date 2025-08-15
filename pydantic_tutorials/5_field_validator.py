# field validator is used to validate the data according to some bussiness use cases.

# field validator is used to do some type of custom validations or transformations on given parameters .
# example :- to check whether the email_id belongs to hdfc.com or icici.com or not. And also convert all the names into uppercase.

# field validator operates on two modes :- before mode and after mode.

# field validator is used to perform data validation on a single field .

from pydantic import BaseModel, EmailStr,Field,field_validator
from typing import List, Dict,Optional,Annotated

class Patient(BaseModel):
    name:str
    email:EmailStr
    age:int
    weight:float
    married:bool
    allergies:List[str]
    contact_details:Dict[str,str]

    # make a decorator for email parameter. And field validator is a class method.
    # default mode is always after .
    @field_validator("email")
    @classmethod
    def email_validator(cls,value):

        # The use of class method is that if we want to access any other class method then we can call it using cls.methodname(value) .

        valid_domains = ['hdfc.com','icici.com']
        domain = value.split('@')[-1]

        if domain not in valid_domains:
            raise ValueError("not a valid domain")
        
        return value
    
    @field_validator("name")
    @classmethod
    def transform_name(cls,value):
        return value.upper()
    
    
    """@field_validator("age", mode="before")
    @classmethod
    def validate_age(cls,value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError("Age should be in between 0 to 100 .")""" # this will give error because we are validating the age before it gets converted into integer from string .

    @field_validator("age", mode="after")
    @classmethod
    def validate_age(cls,value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError("Age should be in between 0 to 100 .")

    

patient_info = {"name":"nitish", "email":"nitish@hdfc.com", "age":"24","weight":70.5, "married":False, "allergies":["pollen","dust"], "contact_details":{"pnone":"8018830741"}}

patient1 = Patient(**patient_info) # validation -> type coercion

def insert_patient_data(patient:Patient):

    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)

insert_patient_data(patient1)