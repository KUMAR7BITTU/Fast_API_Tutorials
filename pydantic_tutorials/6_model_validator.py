# In model validator we can combine multiple fields to do the data validation . 
# model_validator works on entire pydantic model.

# example :- If age is greater than 60 then an emergency contact number should be stored in contact details.

from pydantic import BaseModel, model_validator, EmailStr, Field
from typing import List, Dict, Annotated, Optional

class Patient(BaseModel):

    name:str
    email:EmailStr
    age:int
    weight:float
    married:bool
    allergies:List[str]
    contact_details:Dict[str,str]

    # we don't pass any particular parameter in model_validator() because it works on entire model.
    @model_validator(mode="after")
    def validate_emergency_contact(cls,model):

        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError("patient older than 60 must have an emergency contact number .")
        
        return model
    
patient_info = {"name":"nitish", "email":"nitish@hdfc.com", "age":"65","weight":70.5, "married":False, "allergies":["pollen","dust"], "contact_details":{"pnone":"8018830741","emergency":"484004"}}

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