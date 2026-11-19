# ==========================================
# SMART GROCERY STORE MANAGEMENT SYSTEM
# ==========================================

products = [
    {"id": 101, "name": "Milk", "category": "Dairy", "price": 250.0, "stock": 20},
    {"id": 102, "name": "Bread", "category": "Bakery", "price": 120.0, "stock": 15},
    {"id": 103, "name": "Rice", "category": "Grains", "price": 180.0, "stock": 10},
    {"id": 104, "name": "Eggs", "category": "Dairy", "price": 300.0, "stock": 4},
]

sales_records = []


def find_product_by_id(product_id):
    for product in products:
        if product["id"] == product_id:
            return product
    return None


def display_product(product):
    print("-" * 40)
    print("Product ID :", product["id"])
    print("Name       :", product["name"])
    print("Category   :", product["category"])
    print("Price      : Rs.", product["price"])
    print("Stock      :", product["stock"])
    print("-" * 40)


def add_product():
    print("\n--- Add New Product ---")
    try:
        product_id = int(input("Enter product ID: "))
        if find_product_by_id(product_id) is not None:
            print("Error: Product ID already exists!")
            return

        name = input("Enter product name: ").strip()
        category = input("Enter product category: ").strip()
        price = float(input("Enter product price: "))
        stock = int(input("Enter available stock: "))

        if not name or not category:
            print("Error: Name and category cannot be empty!")
            return
        if price <= 0 or stock < 0:
            print("Error: Price must be positive and stock cannot be negative!")
            return

        new_product = {
            "id": product_id, "name": name, "category": category,
            "price": price, "stock": stock
        }
        products.append(new_product)
        print("Product added successfully!")
    except ValueError:
        print("Error: Please enter valid numeric values!")


def view_all_products():
    print("\n--- All Products ---")
    if not products:
        print("No products available.")
        return
    for product in products:
        display_product(product)


def search_product():
    print("\n--- Search Product ---")
    search_input = input("Enter product ID or name: ").strip()
    if not search_input:
        print("Search value cannot be empty.")
        return

    if search_input.isdigit():
        product = find_product_by_id(int(search_input))
        if product:
            display_product(product)
        else:
            print("Product not found!")
    else:
        found_products = [
            product for product in products
            if search_input.lower() in product["name"].lower()
        ]
        if found_products:
            for product in found_products:
                display_product(product)
        else:
            print("Product not found!")


def update_stock():
    print("\n--- Update Product Stock ---")
    try:
        product_id = int(input("Enter product ID: "))
        product = find_product_by_id(product_id)
        if product is None:
            print("Product not found!")
            return

        print("Current stock:", product["stock"])
        print("1. Add stock")
        print("2. Set new stock quantity")
        choice = input("Enter your choice: ")

        if choice == "1":
            quantity = int(input("Enter quantity to add: "))
            if quantity <= 0:
                print("Quantity must be greater than zero!")
                return
            product["stock"] += quantity
        elif choice == "2":
            new_stock = int(input("Enter new stock quantity: "))
            if new_stock < 0:
                print("Stock cannot be negative!")
                return
            product["stock"] = new_stock
        else:
            print("Invalid choice!")
            return

        print("Stock updated successfully!")
        print("Updated stock:", product["stock"])
    except ValueError:
        print("Error: Please enter valid numeric values!")


def process_sale():
    print("\n--- Process Customer Sale ---")
    try:
        product_id = int(input("Enter product ID: "))
        product = find_product_by_id(product_id)
        if product is None:
            print("Product not found!")
            return

        quantity = int(input("Enter purchase quantity: "))
        if quantity <= 0:
            print("Quantity must be greater than zero!")
            return
        if quantity > product["stock"]:
            print("Insufficient stock!")
            print("Available stock:", product["stock"])
            return

        total_amount = product["price"] * quantity
        product["stock"] -= quantity
        sale = {
            "id": product["id"], "name": product["name"],
            "quantity": quantity, "total": total_amount
        }
        sales_records.append(sale)

        print("\n===== PURCHASE SUMMARY =====")
        print("Product:", product["name"])
        print("Quantity:", quantity)
        print("Unit Price: Rs.", product["price"])
        print("Total Amount: Rs.", total_amount)
        print("Remaining Stock:", product["stock"])
        print("Sale completed successfully!")
    except ValueError:
        print("Error: Please enter valid numeric values!")


def view_sales_records():
    print("\n--- Sales Records ---")
    if not sales_records:
        print("No sales have been recorded.")
        return
    for sale in sales_records:
        print("-" * 40)
        print("Product ID   :", sale["id"])
        print("Product Name :", sale["name"])
        print("Quantity Sold:", sale["quantity"])
        print("Total Amount : Rs.", sale["total"])
        print("-" * 40)


def generate_store_report():
    print("\n========== STORE REPORT ==========")
    total_products = len(products)
    total_stock = sum(product["stock"] for product in products)
    total_transactions = len(sales_records)
    total_revenue = sum(sale["total"] for sale in sales_records)

    print("Total Products       :", total_products)
    print("Total Available Stock:", total_stock)
    print("Total Transactions   :", total_transactions)
    print("Total Revenue        : Rs.", total_revenue)

    low_stock_products = [product for product in products if product["stock"] < 5]
    print("\n--- Low Stock Products (Below 5) ---")
    if low_stock_products:
        for product in low_stock_products:
            print(product["name"], "- Stock:", product["stock"])
    else:
        print("No low-stock products.")

    if products:
        print("\n--- Highest Price Product ---")
        display_product(max(products, key=lambda p: p["price"]))
        print("\n--- Lowest Price Product ---")
        display_product(min(products, key=lambda p: p["price"]))
    else:
        print("No products available for price comparison.")
    print("==================================")


def main():
    while True:
        print("\n====================================")
        print("   SMART GROCERY STORE SYSTEM")
        print("====================================")
        print("1. Add New Product")
        print("2. View All Products")
        print("3. Search Product")
        print("4. Update Product Stock")
        print("5. Process Customer Sale")
        print("6. View Sales Records")
        print("7. Generate Store Report")
        print("8. Exit")
        print("====================================")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_product()
        elif choice == "2":
            view_all_products()
        elif choice == "3":
            search_product()
        elif choice == "4":
            update_stock()
        elif choice == "5":
            process_sale()
        elif choice == "6":
            view_sales_records()
        elif choice == "7":
            generate_store_report()
        elif choice == "8":
            print("Thank you for using Smart Grocery Store System!")
            break
        else:
            print("Invalid choice! Please select from 1 to 8.")


if __name__ == "__main__":
    main()
