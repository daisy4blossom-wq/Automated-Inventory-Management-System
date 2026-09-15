import sqlite3
from project2 import Inventory
from exception import  InventoryError, InsufficientStockError, DuplicateItemError, ItemNotFoundError

class Database_manager:
    def __init__(self, db_name: str =  "inventory.db"):
        self.connection = sqlite3.connect(db_name)
        self.create_table()

        
    def create_table(self):
        creation = """
        CREATE TABLE IF NOT EXISTS inventory(
            sku TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL,
            low_stock INTEGER NOT NULL
         ) 
        """
        cursor = self.connection.cursor()
        cursor.execute(creation)
        self.connection.commit()

    def add_item(self, item: Inventory):
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "INSERT INTO VALUES(?,?,?,?,?)", 
                (item.sku, item.name, item.quantity, item.price, item.low_stock)
            )
            self.connection.commit()
        except sqlite3.IntegrityError:
            raise DuplicateItemError("item already exists")  

    def get_all_items(self):
        cursor = self.connection.cursor()
        cursor.execute("""SELECT * FROM Inventory""")
        records = cursor.fetchall()
        return [Inventory(sku = r[0], name = r[1], quantity = r[2], price = r[3], low_stock=r[4]) for r in records]

    def update_stock(self, sku: str, new_quantity: int):
         cursor = self.connection.cursor()
         cursor.execute(""" UPDATE inventory SET quantity = ? WHERE sku = ?""", (new_quantity, sku)) 
         self.connection.commit()

         if cursor.rowcount == 0:
             raise ItemNotFoundError( f"Item with SKU {sku} not found!")

if __name__ == "__main__":
    db = Database_manager()
    print("Database ran successfully!")