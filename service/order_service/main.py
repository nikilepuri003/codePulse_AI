
from fastapi import FastAPI

app = FastAPI(title="CodePulse Order Service")


@app.get("/")
def home():
    return {"message": "Order Service is working!"}


@app.get("/health")
def health():
    return {
        "service": "Order Service",
        "status": "Healthy"
    }


@app.get("/orders/{order_id}")
def get_order(order_id: int):
    return {
        "order_id": order_id,
        "product": "Laptop",
        "amount": 65000,
        "status": "Order Confirmed"
    }
