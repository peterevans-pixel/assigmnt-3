customers = {}

print("Enter customer names and total purchases.")
print("Leave the customer name blank when finished.")

while True:
    name = input("\nCustomer name: ").strip()
    if not name:
        break

    while True:
        try:
            purchase_total = float(input(f"Total purchases for {name}: $").strip())
        except ValueError:
            print("Please enter a valid amount.")
            continue

        if purchase_total < 0:
            print("Purchase total cannot be negative.")
            continue

        customers[name] = purchase_total
        break

tiers = {"Bronze": 0, "Silver": 0, "Gold": 0}
customer_tiers = {}

for name, purchase_total in customers.items():
    if purchase_total < 1000:
        tier = "Bronze"
    elif purchase_total < 5000:
        tier = "Silver"
    else:
        tier = "Gold"

    customer_tiers[name] = tier
    tiers[tier] += 1

print("\nCustomer Loyalty Summary")
print("------------------------")
if customer_tiers:
    for name, tier in customer_tiers.items():
        print(f"{name}: {tier}")
else:
    print("No customers were entered.")

print("\nCustomers per tier:")
for tier, count in tiers.items():
    print(f"{tier}: {count}")
