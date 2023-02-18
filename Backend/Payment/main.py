from fastapi import FastAPI
from redis_om import get_redis_connection, HashModel
from fastapi.middleware.cors import CORSMiddleware
from starlette.requests import Request
import requests
import time
from fastapi.background import BackgroundTasks

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins= ['http://localhost:3000'],
    allow_methods=['*'],
    allow_headers=['*']

)

#each microservice need its own database
redis = get_redis_connection(
    host = #use your host here,
    port = #use your port,
    password = #use your password,
    decode_responses = True
)

class Order(HashModel):
    product_id: str
    price: float
    fee: float
    total: float
    quantity: int
    status: str #pending, completed, refund

    class Meta:
        database = redis


@app.get('/orders/{pk}')
def get(pk: str):
    return Order.get(pk)


@app.post('/orders')
async def create(request:Request, background_tasks: BackgroundTasks): #id, quantity
    body = await request.json()

    req = requests.get('http://localhost:8000/products/%s' %body['id'])
    product = req.json()

    order = Order(
        product_id=body['id'],
        price=product['price'],
        fee=0.2*product['price'],
        total = 1.2*product['price'],
        quantity = body['quantity'],
        status='pending'
    )
    order.save()

    background_tasks.add_task(order_completed, order)#make payment

    return order 

def order_completed(order:Order):
    time.sleep(5)
    order.status = 'completed'
    order.save()
    redis.xadd('order_completed', order.dict(),'*') #sending events to redis microservice
