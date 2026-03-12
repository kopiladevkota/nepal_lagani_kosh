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

# -----------------------------------------
# Task 3: Lagani Kosh Yearly Deposit Simulation
# -----------------------------------------

total_investment = 0

print("\nYearly Deposit Simulation")

for year in range(1, years + 1):
    yearly_deposit = monthly_deposit * 12
    total_investment += yearly_deposit
    print(f"Year {year}: Rs {yearly_deposit}")

print("\nTotal Investment:", total_investment)

'''# Task 4: Display formatted investment report
print("\n----- Investment Report -----")
print("Investor Name:", name)
print("Monthly Deposit:", monthly_deposit)
print("Years:", years)
print("Total Investment:", total_investment)'''