from fastapi import FastAPI
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