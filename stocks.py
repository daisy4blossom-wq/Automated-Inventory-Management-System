from project2 import Inventory
from exception import  InventoryError, InsufficientStockError, DuplicateItemError, ItemNotFoundError
from database import Database_manager

class StockEngine:
    def __init__(self, db_manager: Database_manager):
        self.db = db_manager

    def add_new_item(self, item):
        self.db.add_item(item)

    def analyse_transaction(self, sku, quantity_change):
        
            items = self.db.get_all_items()
            target_item = None
            for item in items :
                if item.sku == sku:
                    target_item = item
                    break
            if target_item is None :
                raise ItemNotFoundError(f"item with SKU {sku} not found!")
            new_quantity = target_item.quantity + quantity_change
            if new_quantity < 0:
                 raise InsufficientStockError("Item is not available")
            self.db.update_stock(sku, new_quantity)   

    def check_reorder_alerts(self):
         all_items = self.db.get_all_items()
         return [item for item in all_items if item.quantity <= item.low_stock] 
                      

if __name__ == "__main__":
     db = Database_manager()
     engine = StockEngine(db)     

book = Inventory(
     sku = "PYTHON-101",
     name = "Introduction to python",
     category = "Education",
     quantity = 20,
     price = 1000,
     low_stock = 2
)

try:
     engine.add_new_item(book)
     print("Successfully added new item!")
except Exception as e:
     print(f"Notice: {e}")   

      
engine.analyse_transaction("PYTHON-101", -3)
print("Succesfully processed transaction!")
        


    

        