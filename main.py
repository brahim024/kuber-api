from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

app = FastAPI(
    title="Kubernetes Test API",
    description="A simple FastAPI application for testing Kubernetes deployment",
    version="1.0.0"
)

# Sample data store
items = []

class Item(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None

@app.get("/")
async def root():
    return {"message": "Welcome to the Kubernetes Test API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/items", response_model=List[Item])
async def get_items():
    return items

@app.post("/items", response_model=Item)
async def create_item(item: Item):
    item.id = len(items) + 1
    items.append(item)
    return item

@app.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) 