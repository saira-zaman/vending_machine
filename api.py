from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI(title="Vending Machine API")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return FileResponse("index.html")

@app.get("/health")
async def health_check():
    return JSONResponse({"status": "healthy"})

@app.get("/api/items")
async def get_items():
    items = [
        {"id": 1, "name": "Coke", "price": 1.50},
        {"id": 2, "name": "Pepsi", "price": 1.50},
        {"id": 3, "name": "Water", "price": 1.00},
        {"id": 4, "name": "Chips", "price": 0.75},
    ]
    return JSONResponse({"items": items})

@app.post("/api/purchase")
async def purchase_item(item_id: int, amount: float):
    return JSONResponse({
        "success": True,
        "item_id": item_id,
        "amount_paid": amount,
        "message": "Purchase successful!"
    })
