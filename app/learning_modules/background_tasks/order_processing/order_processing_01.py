from fastapi import APIRouter, BackgroundTasks
from pydantic import BaseModel
import time
from datetime import datetime

order_router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)

class OrderRequest(BaseModel):
    order_id: int
    product_name: str

# Background Task Function
def process_order(order_id: int, product_name: str):
    """
    This function runs AFTER the response is sent.
    It simulates order processing and saves data to a file.
    """

    # Simulate logng processing time
    time.sleep(5)

    # Prepare order log
    timestamp = datetime.now().isoformat()
    log_message = f"{timestamp} | OrderID: {order_id} | Product: {product_name}\n"

    # Write to file
    with open("orders.txt", "a") as file:
        file.write(log_message)

    print(f"✅ Order {order_id} processed successfully")


# API Endpoint
@order_router.post("/order/")
def create_order(
    order: OrderRequest,
    background_tasks: BackgroundTasks
):
    """
    API responds immediately.
    Background task runs independently.
    """

    # Register background task
    background_tasks.add_task(
        process_order,
        order.order_id,
        order.product_name
    )

    # Immediate response
    return {
        "message": "Order placed successfully",
        "order_id": order.order_id,
        "status": "Processing in background"
    }