
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx

app = FastAPI(title="CodePulse Order Service")


USER_SERVICE_URL = "http://127.0.0.1:8000"
PAYMENT_SERVICE_URL = "http://127.0.0.1:8002"


class OrderRequest(BaseModel):
    product: str
    amount: float


@app.get("/")
def home():
    return {
        "service": "Order Service",
        "status": "Running"
    }


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


@app.post("/orders/create/{user_id}")
def create_order(user_id: int, order: OrderRequest):

    # Step 1: Verify the user
    try:
        user_response = httpx.get(
            f"{USER_SERVICE_URL}/users/{user_id}",
            timeout=5.0
        )
        user_response.raise_for_status()
        user_data = user_response.json()

    except httpx.TimeoutException:
        raise HTTPException(
            status_code=504,
            detail="User Service timed out"
        )

    except httpx.HTTPError:
        raise HTTPException(
            status_code=502,
            detail="Unable to contact User Service"
        )

    # Step 2: Process payment
    try:
        payment_response = httpx.post(
            f"{PAYMENT_SERVICE_URL}/payments/process",
            json={
                "order_id": 101,
                "amount": order.amount
            },
            timeout=5.0
        )
        payment_response.raise_for_status()
        payment_data = payment_response.json()

    except httpx.TimeoutException:
        raise HTTPException(
            status_code=504,
            detail="Payment Service timed out"
        )

    except httpx.HTTPError:
        raise HTTPException(
            status_code=502,
            detail="Unable to contact Payment Service"
        )

    # Step 3: Return combined result
    return {
        "order_id": 101,
        "product": order.product,
        "user": user_data,
        "payment": payment_data,
        "order_status": "Confirmed"
    }
