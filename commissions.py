sales = {}

for employee in ("Alice", "Bob", "Carol"):
    while True:
        entry = input(f"Enter sales amount for {employee}: ").strip()

        try:
            amount = float(entry)
        except ValueError:
            print("Please enter a valid number.")
            continue

        if amount < 0:
            print("Sales amount cannot be negative.")
            continue

        sales[employee] = amount
        break


def calculate_commission(sales_amount):
    return sales_amount * 0.10


leaderboard = sorted(
    sales.items(),
    key=lambda employee: calculate_commission(employee[1]),
    reverse=True,
)

print("Sales Commission Leaderboard")
print("----------------------------")
for rank, (employee, sales_amount) in enumerate(leaderboard, start=1):
    commission = calculate_commission(sales_amount)
    print(f"{rank}. {employee}: ${commission:.2f} commission")
