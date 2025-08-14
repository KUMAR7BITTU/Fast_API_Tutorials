"""def insert_patient_data(name,age):

    print(name)
    print(age)
    print('inserted into databse successfully.')

insert_patient_data("bittu","thirty")"""
# python doesn't support static typing, rather it supports dynamic typing.We should have passed age as int but we passed age as string and it worked fine. This is the problem with python. So, to solve this issue we use pydantic library.

# We can use type hinting in python.
"""def insert_patient_data1(name:str, age:int):

    print(name)
    print(age)
    print("inserted into database successfully.")"""

"""insert_patient_data1("bittu",30)""" # here we are passing correct data types so no error will be thrown

"""insert_patient_data1("bittu","thirty")""" # here we are passing incorrect data types but no error is thrown .

# This means type hinting in python doesn't produce any error if we pass wrong data types. It will only give hint about the data type of a variable.


# We can manually write some lines of code using if - else to check the type validation.
"""def insert_patient_data2(name:str , age:int):

    if type(name) == str and type(age) == int:
        print(name)
        print(age)
        print("inserted into database successfully.")
    else:
        raise TypeError("Incorrect data type")
    
insert_patient_data2("bittu","thirty")"""

# if suppose we have to create another function update then also we have to do same thing again and again which is not good practice. To avoid this we use pydantic library.
"""def update_patient_data2(name:str , age:int):

    if type(name) == str and type(age) == int:
        print(name)
        print(age)
        print("inserted into database successfully.")
    else:
        raise TypeError("Incorrect data type")
    
update_patient_data2("bittu","thirty")"""

# Install pydantic v2 version not v1 .

from pydantic import BaseModel

# create pydantic model and define schema inside it
class Patient(BaseModel):

    name: str
    age: int

# create raw dictionary
# patient_info = {"name":"bittu", "age":30}
#patient_info = {"name":"bittu", "age":"thirty"}

# instantiate pydantic object with the help of raw dictionary
# create object of pydantic model or class and pass unpacked dictionary in it.
#patient1 = Patient(**patient_info) # The above rule (like name:str and age:int) will be applied on this raw dictionary and if it satified then an object will be created .

"""def insert_patient_data3(patient:Patient):

    print(patient.name)
    print(patient.age)
    print("inserted")

insert_patient_data3(patient1)"""


patient_info2  ={"name":"bittu", "age":"30"} # Here we are passing string value to age field but still it didn't throw any error because pydantic will automatically convert that string value to integer.
patient2 = Patient(**patient_info2)
def update_patient_data3(patient:Patient):

    print(patient.name)
    print(patient.age)
    print("updated successfully.")

update_patient_data3(patient2)