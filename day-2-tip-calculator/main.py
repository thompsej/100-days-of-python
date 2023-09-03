print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? "))
tip = int(input("How much of a tip do you want to give? 10%, 12%, or 15% "))
party_size = int(input("How big is your party? "))
tip_in_percentage = tip / 100
total_tip = bill * tip_in_percentage
total_bill = bill + total_tip
splits = total_bill / party_size

print(f"Each person should pay: ${splits:.2f}")