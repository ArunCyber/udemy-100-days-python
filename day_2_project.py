print("Welcome to the tip calculator!")

total_bill = input("What was the total bill? ")
print(total_bill)

interest_tip = input("How much tip would you like to give? 10, 12, or 15? ")
print(interest_tip)

no_of_people = input("How many people to split the bill? ")
print(no_of_people)

bill = float(total_bill) + float(interest_tip)

print(f"Each person should pay: {bill / int(no_of_people)}")


