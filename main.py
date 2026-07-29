from typing import List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    price: float
    description: str | None = None


app = FastAPI(title="Product API", version="1.0.0")

products_db: List[Product] = [
    Product(id=1, name="Laptop", price=999.99, description="High-performance laptop"),
    Product(id=2, name="Smartphone", price=699.99, description="Latest model smartphone"),
    Product(id=3, name="Wireless Earbuds", price=149.99, description="Noise-cancelling earbuds"),
]


@app.get("/products", response_model=List[Product])
def list_products() -> List[Product]:
    """Return the full list of products."""
    return products_db


@app.get("/products/{product_id}", response_model=Product)
def get_product(product_id: int) -> Product:
    """Return a single product by its ID."""
    for product in products_db:
        if product.id == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")
