revenue_by_year = [30, 50, 80]
scale = 10

print("Projected Revenue by Year")
print("-------------------------")

for year, revenue in enumerate(revenue_by_year, start=1):
    bar_length = round(revenue / scale)
    bar = ""
    for _ in range(bar_length):
        bar += "#"

    print(f"Year {year}: {bar} (${revenue})")
