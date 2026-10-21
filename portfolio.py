import random

portfolio = {
    "AAPL": {"shares": 0, "price": 0},
    "TSLA": {"shares": 0, "price": 0},
    "AMZN": {"shares": 0, "price": 0},
}

for ticker, stock in portfolio.items():
    print(f"\nEnter details for {ticker}:")

    while True:
        try:
            shares = int(input("Number of shares: ").strip())
        except ValueError:
            print("Please enter a whole number of shares.")
            continue

        if shares < 0:
            print("Number of shares cannot be negative.")
            continue
        stock["shares"] = shares
        break

    while True:
        try:
            price = float(input("Price per share: $").strip())
        except ValueError:
            print("Please enter a valid price.")
            continue

        if price < 0:
            print("Price cannot be negative.")
            continue
        stock["price"] = price
        break


def calculate_total_value():
    total = 0
    for stock in portfolio.values():
        total += stock["shares"] * stock["price"]
    return total


print(f"Starting portfolio value: ${calculate_total_value():.2f}")

for day in range(1, 8):
    for stock in portfolio.values():
        daily_change = random.uniform(-0.05, 0.05)
        stock["price"] *= 1 + daily_change

    print(f"Day {day} portfolio value: ${calculate_total_value():.2f}")
