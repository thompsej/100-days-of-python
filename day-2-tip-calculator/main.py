print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? "))
tip = input("How much of a tip do you want to give? 10%, 12%, or 15% ")
tip_in_percentage = float("1." +tip)
party_size = int(input("How big is your party? "))

tip_math = (total_bill / party_size) * (tip_in_percentage)
print(f"Each person should pay: ${tip_math:.2f}")