# field function is used to validate the data of numerical and string type both.
# we can also use Field function to attach meta data .
from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

"""class Patient(BaseModel):

    name:str = Field(max_length=50)
    email:EmailStr
    linkedin:AnyUrl
    age:int = Field(gt=0, lt=120)
    weight:float = Field(gt=0)
    married:bool = False
    allergies:Optional[List[str]] = Field(max_length=5)
    contact_details:Dict[str,str]

patient_info1 = {"name":"nitish", "email":"bittuk@gmail.com", "linkedin":"http://linkedin.com/2345", "age":27, "weight":-72.5, "contact_details":{"phone":"8018830741"}}

patient1 = Patient(**patient_info1)

def insert_patient_data(patient:Patient):

    print(patient.name)
    print(patient.email)
    print(patient.linkedin)
    print(patient.age)
    print(patient.weight)
    print(patient.contact_details)

insert_patient_data(patient1)"""

class PatientOptional(BaseModel):

    name: Annotated[str, Field(max_length=50, title='Name of the patient', description='Give the name of the patient in less than 50 characters.', examples=['Nitish','Amit'])]
    email:EmailStr
    linkedin:AnyUrl
    age:int = Field(gt=0, lt=120)
    # weight:float = Field(gt=0)
    weight:Annotated[float, Field(gt=0, strict=True)] # if strict = True then type conversion will not be done.
    married:Annotated[bool,Field(default=None, description='Is the patient married or not.')]
    allergies:Annotated[Optional[List[str]], Field(default=None, max_length=5)]
    contact_details:Dict[str,str]

patient_info2 = {"name":"nitish", "email":"bittukumar30dec2002@gmail.com", "linkedin":"http://linkedlin.com/3245", "age":29, "weight":'74.5', "contact_details":{"phone":"8018830741"}}

patient2 = PatientOptional(**patient_info2)

def insert_patient_data(patient:PatientOptional):

    print(patient.name)
    print(patient.email)
    print(patient.linkedin)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)

insert_patient_data(patient2)