
from fastapi import FastAPI

app = FastAPI(title="CodePulse Payment Service")


@app.get("/")
def home():
    return {
        "project": "CodePulse AI",
        "service": "Payment Service",
        "status": "Running"
    }


@app.get("/health")
def health():
    return {
        "service": "Payment Service",
        "status": "Healthy"
    }


@app.get("/payments/{payment_id}")
def get_payment(payment_id: int):
    return {
        "payment_id": payment_id,
        "amount": 65000,
        "payment_method": "UPI",
        "status": "Payment Successful"
    }
