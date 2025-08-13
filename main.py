from fastapi import FastAPI, Path, HTTPException, Query
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


@app.get('/sort')
def sort_patients(sort_by:str = Query(...,description='sort on the basis of height, weight or bmi'), order_by:str = Query('asc',description='sort in asc or desc order')):

    valid_fields = ['height','weight','bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code = 400, detail = f'Invalid field selected from {valid_fields}')
    
    if order_by not in ['asc','desc']:
        raise HTTPException(status_code=400,detail='Invalid order selected between asc or desc')
    
    data = load()
    sort_order = True if order_by == 'desc' else False

    sorted_data = sorted(data.values(),key = lambda x : x.get(sort_by,0), reverse = sort_order)

    return sorted_data




    

    


