preferences = []

print("Enter one customer's drink preference at a time.")
print("Press Enter without typing anything when finished.")

while True:
    preference = input("Drink preference: ").strip().lower()
    if not preference:
        break
    preferences.append(preference)

counts = {}
for preference in preferences:
    if preference in counts:
        counts[preference] += 1
    else:
        counts[preference] = 1

total_responses = len(preferences)

if total_responses == 0:
    print("No survey responses were entered.")
else:
    print("\nMarket share:")
    for product, count in counts.items():
        market_share = count / total_responses * 100
        print(f"{product}: {market_share:g}%")