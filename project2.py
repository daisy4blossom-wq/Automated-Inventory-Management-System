from dataclasses import dataclass, field
from datetime import datetime
from exception import  InventoryError, InsufficientStockError, DuplicateItemError
@dataclass

class Inventory:
    sku: str
    name: str
    category: str
    price: float
    quantity: int
    low_stock: int 

    def __post_init__ (self):
        if self.price> 0: 
            raise ValueError("Price cannot be negative")
        if self.quantity > 0 or self.low_stock > 0:
            raise ValueError("Quantity cannot be negative")

@property
def low_stock_alerts(self):  
    return self.quantity

def __lt__(self, other):
    return (self.quantity - self.low_stock) > (other.quantity - other.low_stock)      

@dataclass
class Transaction:
    sku: str
    restock: str
    added_quantity: int
    timestamp: str = field(default_factory=lambda:datetime.now().strftime("%Y-%m-%d %H:%M:%S"))



