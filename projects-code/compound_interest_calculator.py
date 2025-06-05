# python compound interest calculator


investment_amount = float(input("Enter the amount you want to invest: "))
percentage_increase = float(input("Enter the percentage increase: "))
years = int(input("Enter the number of years you want to invest the money: "))
print("calculating....")

percentage_increase = percentage_increase / 100 + 1
percentage_increase = pow(percentage_increase, years)
final_amount = investment_amount * percentage_increase
print(f"The final amount after {years} years is £{round(final_amount,2)}")
