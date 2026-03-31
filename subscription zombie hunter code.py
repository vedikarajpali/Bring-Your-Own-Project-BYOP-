import datetime
from collections import defaultdict

# Sample transaction data (date, description, amount)
transactions = [
    ("2026-01-05", "Netflix", 499),
    ("2026-02-05", "Netflix", 499),
    ("2026-03-05", "Netflix", 499),
    ("2026-01-10", "Spotify", 119),
    ("2026-02-10", "Spotify", 119),
    ("2026-03-10", "Spotify", 119),
    ("2026-01-15", "Amazon Prime", 1499),
    ("2026-02-20", "Food Order", 300),
    ("2026-03-22", "Shopping", 1200),
]

# Step 1: Organize transactions by service
services = defaultdict(list)

for date, desc, amount in transactions:
    services[desc].append((date, amount))

# Step 2: Detect recurring services
recurring_services = {}

for service, entries in services.items():
    if len(entries) >= 2:
        amounts = [amt for _, amt in entries]
        if len(set(amounts)) == 1:  # same amount repeated
            recurring_services[service] = entries

# Step 3: Display recurring subscriptions
print("\n🔁 Recurring Subscriptions Detected:\n")

total_monthly_cost = 0

for service, entries in recurring_services.items():
    amount = entries[0][1]
    total_monthly_cost += amount
    print(f"{service} → ₹{amount} per cycle")

# Step 4: Total cost
print("\n💸 Total Estimated Recurring Cost per Month: ₹", total_monthly_cost)

# Step 5: Suggestions
print("\n💡 Suggestions:")
for service, entries in recurring_services.items():
    if service.lower() == "netflix":
        print("- Consider switching to a cheaper Netflix plan.")
    elif service.lower() == "spotify":
        print("- Try student discount for Spotify.")
    elif service.lower() == "amazon prime":
        print("- Evaluate if you use Prime benefits regularly.")

print("\n✅ Analysis Complete.")
