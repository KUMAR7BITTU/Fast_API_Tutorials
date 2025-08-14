# field function is used to validate the data of numerical and string type both.
# we can also use Field function to attach meta data .
from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional
class Patient(BaseModel):

    name:str = Field(max_length=50)
    email:EmailStr
    linkedin:AnyUrl
    age:int = Field(gt=0, lt=120)
    weight:float = Field(gt=0)
    married:bool = False
    allergies:Optional[List[str]] = Field(max_length=5)
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