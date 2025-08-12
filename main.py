from fastapi import FastAPI, Path, HTTPException
import json

app = FastAPI()  # FastAPI object

def load():
    with open("patients.json","r") as f:
        data = json.load(f)
    return data

# creating route # Endpoint
@app.get("/")
def hello():
    return {"message":"Patient Management System API ."}

@app.get("/about")
def about():
    return {"message":"A fully functional API, to manage your patient's record."}

@app.get("/view")
def view():
    data = load()
    return data

# Path parameter enhances the readability of path parameter.
# ... -> It tells that the mentioned field are required.
# description will give the description of the parameter.
# example will show us a sample example.
# ge is a condition for the parameter.
@app.get("/patient/{patient_id}")
def view_patient(patient_id:str = Path(..., description = "ID of the patient in DB",example="P001")):
    data = load()

    if patient_id in data:
        return data[patient_id]
    #return {"error" : "patient not found"}
    raise HTTPException(status_code = 400, detail = "Patient not found" )

