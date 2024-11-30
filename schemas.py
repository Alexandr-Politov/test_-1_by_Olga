from datetime import datetime

from pydantic import BaseModel, Field
from decimal import Decimal


class ProductBaseScheme(BaseModel):
    name: str = Field(..., description="The name of the product")
    description: str = Field(..., description="A detailed product description")
    price: Decimal = Field(..., gt=0, description="Product price, must be > 0")


class ProductCreateScheme(ProductBaseScheme):
    pass


class ProductRetrieveScheme(ProductBaseScheme):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
