expenses = {
    "Travel": [],
    "Meals": [],
    "Supplies": [],
}

for category in expenses:
    print(f"\nEnter amounts for {category}. Enter 0 when finished.")
    while True:
        entry = input(f"{category} expense amount: ").strip()

        try:
            amount = float(entry)
        except ValueError:
            print("Please enter a valid number.")
            continue

        if amount == 0:
            break
        if amount < 0:
            print("Expense amounts cannot be negative.")
            continue

        expenses[category].append(amount)

grand_total = 0

print("Expense Summary Report")
print("----------------------")

for category, amounts in expenses.items():
    category_total = sum(amounts)

    grand_total += category_total
    print(f"{category}: ${category_total:.2f}")

print("----------------------")
print(f"Grand total: ${grand_total:.2f}")
