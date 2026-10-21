warehouses = [
    {"name": "Warehouse A", "inventory": {}},
    {"name": "Warehouse B", "inventory": {}},
]

products = ("apples", "bananas")

for warehouse in warehouses:
    print(f"\nEnter stock for {warehouse['name']}:")
    for product in products:
        while True:
            try:
                quantity = int(input(f"How many {product}? ").strip())
            except ValueError:
                print("Please enter a whole number.")
                continue

            if quantity < 0:
                print("Stock cannot be negative.")
                continue

            warehouse["inventory"][product] = quantity
            break

total_stock = {}

for warehouse in warehouses:
    print(f"\n{warehouse['name']}:")
    for product, quantity in warehouse["inventory"].items():
        print(f"{product}: {quantity}")

    for product, quantity in warehouse["inventory"].items():
        if product in total_stock:
            total_stock[product] += quantity
        else:
            total_stock[product] = quantity

print("Total stock across the supply chain:")
for product, quantity in total_stock.items():
    print(f"{product}: {quantity}")
