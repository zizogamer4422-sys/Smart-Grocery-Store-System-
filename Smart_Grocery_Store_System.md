# Smart Grocery Store Management System

A menu-driven Python application for managing grocery products, inventory, sales, and store reports.

## Features

- Add products and prevent duplicate product IDs
- View all products
- Search products by ID or name
- Add stock or set a new stock quantity
- Process sales while checking stock availability
- View sales records
- Generate a store report with stock and revenue totals, low-stock items, and highest/lowest-priced products
- Validate user input with exception handling

## Requirements

- Python installed

## How to run

1. Save or extract `grocery_store.py`.
2. Open a terminal in the folder containing the file.
3. Run:

   ```bash
   python grocery_store.py
   ```

## Menu

1. Add New Product
2. View All Products
3. Search Product
4. Update Product Stock
5. Process Customer Sale
6. View Sales Records
7. Generate Store Report
8. Exit

## Data storage

Products and sales records are stored in Python lists of dictionaries while the program runs. Data resets when the program exits.

## Project files

- `grocery_store.py` — application source code
- `README.txt` — basic run instructions
- `Smart_Grocery_Store_System.md` — project documentation
