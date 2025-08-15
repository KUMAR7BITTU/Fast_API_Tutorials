# If we are using one model as a field in another model, then it is called nested models.

# If any parameter has hierarchy then we can use the concept of nested models.

from pydantic import BaseModel
class Address(BaseModel):

    city:str
    state:str
    pincode:str

class Patient(BaseModel):

    name:str
    gender:str
    age:int
    address:Address # address is of Address data type

# creating raw dictionary for address
address_info = {"city":"Gurgaon", "state":"Haryana", "pincode":"204384"}

# creating object for address 
address1 = Address(**address_info)

print(address1)
print(address1.city)
print(address1.state)
print(address1.pincode)

# creating raw dictionary for patient
patient_info = {"name":"nitish", "gender":"male", "age":35, "address": address1}

patient1 = Patient(**patient_info)

print(patient1)
print(patient1.name)
print(patient1.gender)
print(patient1.address.city)
print(patient1.address.state)
print(patient1.address.pincode)

# Better organization of related data (e.g., vitals, address, insurance)
# Reusability : use Vitals in multiple models (e.g., Patient, MedicalRecord).
# Readability : Easier for developers and API consumers to understand.
# Validation : Nested models are validated automatically - no extra work needed.