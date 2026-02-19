from pydantic import BaseModel, constr

# Example Pydantic schemas for request and response validation
class Item(BaseModel):
    id: int
    name: constr(min_length=1)
    description: str = None
    price: float
    tax: float = None

class ItemResponse(BaseModel):
    item: Item
    message: str
    
class ItemListResponse(BaseModel):
    items: list[Item]
    total: int
    
# You can add more schemas as needed