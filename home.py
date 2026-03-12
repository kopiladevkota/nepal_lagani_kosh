# Task 1: Take input from user
name = input("Enter investor name: ")
monthly_deposit = float(input("Enter monthly deposit: "))
years = int(input("Enter investment years: "))

print("\nInvestor Name:", name)
print("Monthly Deposit:", monthly_deposit)
print("Investment Years:", years)

# Task 2: Print data types
print("\nData Types")
print("Type of monthly_deposit:", type(monthly_deposit))
print("Type of years:", type(years))

# # Task 3: Calculate total investment
total_investment = monthly_deposit * 12 * years
print("\nTotal Investment:", total_investment)

# # Task 4: Display formatted investment report
print("\n----- Investment Report -----")
print("Investor Name:", name)
print("Monthly Deposit:", monthly_deposit)
print("Years:", years)
print("Total Investment:", total_investment)