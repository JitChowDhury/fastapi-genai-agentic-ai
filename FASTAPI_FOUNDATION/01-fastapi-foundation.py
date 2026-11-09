from fastapi import FastAPI
from fastapi import Request

import uvicorn
app = FastAPI(
    title="Swiggy order service",
    description=("Internal API"
                 "Handle Creation Tracking"),
    version="1.2.1",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"

)


@app.get("/")
def read_root():
    """Root Endpoint - Health Check"""
    #FastAPI coverts this dict into JSON
    return {
        "message":"welcome to swiggy order service",
        "status":"healthy"
    }

@app.get("/about")
def about():
    """Returns API Metadata"""
    return {
        "service":"order service",
        "team":"backend platform",
        "region":"ap-south-1",
        "version":"1.2.2"
    }

@app.get("/orders")
def list_orders():
    """List recent orders"""
    return {
        "orders":[
            {"id":1,"item":"Butter Chicken","status":"delivered"},
            {"id":2,"item":"Tandoori Roti","status":"Preparing"},
            {"id":1,"item":"Paneer Tikka","status":"OutForDelivery"}
        ]
    }

@app.get("/orders/status")
def order_status():
    """Get Order Status"""
    return{
        "total_today":2_540_23,
        "top_city":"Kolkata"
    }

@app.get("/debug/request-info")
async def request_info(request:Request):
    """Inspect the raw request object"""
    return {
        "method":request.method,
        "url":str(request.url),
        "headers":dict(request.headers),
        "path_params":request.path_params,
        "query_params":dict(request.query_params)
    }


@app.get(
    "/orders/active",
    summary="Get ACtive orders",
    description=(
        "Returns all orders that are currently being prepared"
        "or out for delivery"
    ),
    tags=["orders"],
    response_description="List of active order objects",
    deprecated=False
)
def get_active_order():
    """This docstring also appears in docs"""
    return{
        "active_orders":[
            {"id":1,"item":"Masala Dosa","status":"out_for_delivery"}
        ]
    }


@ app.get("/restaurents",tags=["Restaurents"])
def list_restro():
    """another docstring for another endpoint"""
    return {
        "restaurents":[
            {"test":"test"}
        ]
    }