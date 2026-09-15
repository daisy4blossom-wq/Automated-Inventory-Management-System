# Automated Inventory management Engine

A automated inventory management system built with Python and SQLite. This project demonstrates clean backend architecture using a **Separation of Concerns** (MVC-like) design pattern, robust domain-specific error handling, parameterized SQL execution, and automated inventory monitoring.

---

## Architecture Overview

The system is split into distinct layers to ensure scalability, testability, and clean code maintenance:

- **`project2.py` (Data Models): Defines core domain entities (`Inventory`, `Transaction`) using Python `@dataclass` for type safety and clean object blueprints.
- **`exception.py` (Custom Errors): Implements domain-specific exceptions (`InsufficientStockError`, `ItemNotFoundError`, `DuplicateItemError`) to capture business rule violations cleanly.
- **`database.py` (Data Access Layer): Manages SQLite connections and CRUD operations using parameterized SQL queries (`?`) to prevent SQL injection vulnerabilities.
- **`stocks.py` (Business Logic Engine): Houses `StockEngine`, orchestrating inventory checks, transaction validations, and low-stock automated alerts via Dependency Injection.

---

## ✨ Key Features

- **Decoupled Architecture:** Business logic (`StockEngine`) is completely separated from persistent storage (`Database_manager`).
- **Data Integrity & Safety:** Built-in safeguards against negative stock levels and duplicate item entries.
- **Automated Reorder Alerts:** Scans current inventory against `low_stock` levels using Pythonic list comprehensions to flag low stock automatically.
- **Parameterized SQL:** All queries strictly use parameters to ensure database safety against injection attacks.

---
TECH STACK:
Language: Python 3
Database: SQLite3
Tools: Dataclasses, Custom Exceptions, Object-Oriented Programming(OOP)


