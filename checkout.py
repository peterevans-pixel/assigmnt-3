prices = []

while True:
    entry = input("Enter an item price (or 0 to finish): ").strip()

    try:
        price = float(entry)
    except ValueError:
        print("Please enter a valid number.")
        continue

    if price == 0:
        break
    if price < 0:
        print("Price cannot be negative. Please try again.")
        continue

    prices.append(price)

total = sum(prices)
item_count = len(prices)
average = total / item_count if item_count else 0

print(f"\nTotal purchase amount: ${total:.2f}")
print(f"Average item cost: ${average:.2f}")
print(f"Number of items bought: {item_count}")
