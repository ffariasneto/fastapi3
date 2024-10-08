from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, field_validator

products = [{"name_product": "Arroz", "price": 2.50, "stock": 2}, {"name": "Feijão", "price": 2.50, "stock": 2}]
class Products(BaseModel):
    name_product: str
    price: float
    stock: float

    @field_validator("name_product")
    def check_name_product(cls, value):
            if value != products["name"]:   
                raise HTTPException(status_code=400, detail="The product name cannot be less than 3 characters long!")
            return value
    
    @field_validator("price", "stock")
    def check_price_stock(cls, value):
            if value < 0:
                raise HTTPException(status_code=400, detail="the price and stock of the product cannot be less than zero.")
            return value

app  = FastAPI()

@app.post("/product")
def create_product(product: Products):
    products.append(product)
    return {
        "message": "Product ok", "products": products
    }

# @app.get("/product/{name_product}")
# def read_root(name_product: str):
#     for product in products:
#         if name_product == product["name"]:
#             return {
#                 products
#             }
#     return {
#         "message": "Product not found"
#     }

