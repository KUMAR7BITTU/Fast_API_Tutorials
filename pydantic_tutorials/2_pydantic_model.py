from pydantic import BaseModel
from typing import List, Dict, Optional

# Bydefault all the fields in pydantic models are required.
class Patient(BaseModel):

    name:str # bydefault required field
    age:int
    weight:float
    married:bool
    allergies:List[str]
    contact_details:Dict[str,str]

patient_info1 = {"name":"nitish", "age":30, "weight":75.2, "married":True, "allergies":["pollen","dust"], "contact_details":{"email":"abc@gmail.com","phone":"8018830741"}}

patient1 = Patient(**patient_info1)
def insert_patient_data(patient:Patient):

    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("inserted successfully.")

insert_patient_data(patient1)

patient_info2 = {"age":30, "weight":75.2, "married":True, "allergies":["pollen","dust"], "contact_details":{"email":"abc@gmail.com","phone":"8018830741"}}

patient2 = Patient(patient_info2)
insert_patient_data(patient2) # here name is missing so it will throw error.

class PatientOptional(BaseModel):

    name:str 
    age:int
    weight:float
    married:bool = False # bydefault married is false .
    allergies:Optional[List[str]] = None # if we dont pass any value for allergies it will take none as default value.
    contact_details:Dict[str,str]


patient_info_optional = {"name":"nitish", "age":30, "weight":75.2,  "contact_details":{"email":"abc@gmail.com","phone":"8018830741"}}

patient_optional = PatientOptional(**patient_info_optional)

insert_patient_data(patient_optional)