print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill?$ "))
tip_percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
ppl_count = int(input("How many people to split the bill? "))

grand_total = total_bill * (100 + tip_percent) / 100
per_amount = round(grand_total / ppl_count, 2)
per_amount = "{:.2f}".format(per_amount)

print(f"Each person should pay: ${per_amount}")




