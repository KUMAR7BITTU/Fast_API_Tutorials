from fastapi import FastAPI

app = FastAPI()  # FastAPI object

# creating route # Endpoint
@app.get("/")
def hello():
    return {"message":"Hello, everyone"}

@app.get("/about")
def about():
    return {"message":"Hello, this is a campusx website ."}

