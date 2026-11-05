from fastapi import FastAPI
app = FastAPI(title="CodePulse User Services")

@app.get("/")
def home():
    return{
        "project" : "CodePulse AI",
        "services": "User Services",
        "status" : "Running"
    }

@app.get("/health")
def health():
    return{
        "services": "User Services",
        "status" : "Healthy"
    }

@app.get("/users/{user_id}")
def get_user(user_id:int):
    return{
        "user_id":user_id,
        "name": "Nikil",
        "message": " User found successfully"
    }