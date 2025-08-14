# pydantic provides some custom data types that can be used to validate the input data. 

from pydantic import BaseModel, EmailStr, AnyUrl
from typing import List, Dict, Optional
class Patient(BaseModel):

    name:str
    email:EmailStr
    linkedin:AnyUrl
    age:int
    weight:float
    married:bool = False
    allergies:Optional[List[str]] = None
    contact_details:Dict[str,str]

patient_info = {"name":"nitish", "email":"bittuk@gmail.com", "linkedin":"http://linkedin.com/2345", "age":27, "weight":72.5, "contact_details":{"phone":"8018830741"}}

patient1 = Patient(**patient_info)

def insert_patient_data(patient:Patient):

    print(patient.name)
    print(patient.email)
    print(patient.linkedin)
    print(patient.age)
    print(patient.weight)
    print(patient.contact_details)

insert_patient_data(patient1)