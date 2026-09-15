class InventoryError(Exception):
    pass

class InsufficientStockError(InventoryError):
    pass

class DuplicateItemError(InventoryError):
    pass

class ItemNotFoundError(InventoryError):
    pass 

