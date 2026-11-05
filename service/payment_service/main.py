
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="CodePulse Payment Service")

class PaymentRequest(BaseModel):
    order_id: int
    amount: float

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
        "status": "Payment Successful"
    }

@app.post("/payments/process")
def process_payment(payment: PaymentRequest):
    return {
        "payment_id": 501,
        "order_id": payment.order_id,
        "amount": payment.amount,
        "payment_method": "UPI",
        "status": "Payment Successful"
    }
