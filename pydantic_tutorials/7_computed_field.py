# computer field is a field whose value is not provided by the user but computed from the other fields.

from pydantic import BaseModel, EmailStr, AnyUrl ,Field, computed_field
from typing import List, Dict, Annotated, Optional

class Patient(BaseModel):

    name:str
    email:EmailStr
    age:int
    weight:float
    height:float
    married:bool
    allergies: List[str]
    contact_details:Dict[str,str]

    @computed_field
    @property
    def calculate_bmi(self)->float:

        bmi = round(self.weight/(self.height**2),2)
        return bmi
    
patient_info = {"name":"nitish", "email":"nitish@gmail.com", "age":65, "weight":75.2, "height":1.75, "married":False, "allergies":["pollen","dust"], "contact_details":{"phone":"8018830741"}}

patient1= Patient(**patient_info)

def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.height)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print(patient.calculate_bmi)
    print("Patient data updated successfully")

update_patient_data(patient1)