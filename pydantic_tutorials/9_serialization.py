# How we can export pydantic model object as python dictionary or json.

# pydantic provides us a library to export pydantic model object as python dictionary or json.

from pydantic import BaseModel
class Address(BaseModel):

    city:str
    state:str
    pincode:str

class Patient(BaseModel):

    name:str
    gender:str = 'Male'
    age:int
    address:Address 

address_info = {"city":"Gurgaon", "state":"Haryana", "pincode":"204384"}

address1 = Address(**address_info)

patient_info1 = {"name":"nitish", "age":35, "address": address1}

patient1 = Patient(**patient_info1)

# exporting pydantic model object as python dictionary.
temp_dict = patient1.model_dump() 
print(temp_dict)
print(type(temp_dict))

# exporting pydantic model object as python json.
temp_json = patient1.model_dump_json() 
print(temp_json)
print(type(temp_json))

# If we want to export only specific fields from the model then we can use include parameter in model_dump method.
temp1 = patient1.model_dump(include=['name','gender'])
print(temp1)
print(type(temp1))

# If we want to export all fields except some specific fields from the model then we can use exclude parameter in model_dump method.
temp2 = patient1.model_dump(exclude=['name','gender'])
print(temp2)
print(type(temp2))

temp3 = patient1.model_dump(exclude={'address':['state']})
print(temp3)
print(type(temp3))



patient_info2 = {"name":"nitish", "age":35, "address": address1}

patient2 = Patient(**patient_info2)

# If we want to export only those fields which are not default values then we can set exclude_unset = True in model_dump method.
temp4 = patient2.model_dump(exclude_unset = True)
print(temp4)
print(type(temp4))
