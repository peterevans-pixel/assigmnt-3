def get_non_negative_number(prompt):
    while True:
        try:
            value = float(input(prompt).strip())
        except ValueError:
            print("Please enter a valid number.")
            continue

        if value < 0:
            print("Please enter a number that is at least 0.")
            continue

        return value


initial_revenue = get_non_negative_number("Initial annual revenue: $")
growth_rate = get_non_negative_number("Annual growth rate (%): ")

revenue = initial_revenue
print("\nBusiness Growth Projection")
print("--------------------------")
print(f"{'Year':<6}{'Projected Revenue':>20}")
print("-" * 26)

for year in range(1, 11):
    revenue *= 1 + growth_rate / 100
    print(f"{year:<6}${revenue:>19,.2f}")
